const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const test = require('node:test');

const repoRoot = path.resolve(__dirname, '..');
const cliPath = path.join(repoRoot, 'bin', 'locole-skills.js');
const packageJson = JSON.parse(
  fs.readFileSync(path.join(repoRoot, 'package.json'), 'utf8')
);

function runCli(args, cwd, options = {}) {
  return spawnSync(process.execPath, [cliPath, ...args], {
    cwd,
    encoding: 'utf8',
    env: {
      ...process.env,
      ...options.env,
    },
  });
}

function makeProjectDir(t) {
  const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'locole-skills-'));
  const projectDir = path.join(tempRoot, 'project');
  fs.mkdirSync(projectDir);
  t.after(() => {
    fs.rmSync(tempRoot, { recursive: true, force: true });
  });
  return projectDir;
}

test('prints help output', () => {
  const result = runCli(['--help'], repoRoot);

  assert.equal(result.status, 0);
  assert.match(result.stdout, /Usage:/);
  assert.match(result.stdout, /locole-skills init \[--force\]/);
  assert.equal(result.stderr, '');
});

test('prints the package version', () => {
  const result = runCli(['--version'], repoRoot);

  assert.equal(result.status, 0);
  assert.equal(result.stdout.trim(), packageJson.version);
  assert.equal(result.stderr, '');
});

test('rejects unknown commands', () => {
  const result = runCli(['wat'], repoRoot);

  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /Unknown command/);
});

test('initializes toolkit and codex skills into a target project', (t) => {
  const projectDir = makeProjectDir(t);
  const result = runCli(['init'], projectDir);

  assert.equal(result.status, 0);
  assert.ok(fs.existsSync(path.join(projectDir, '.agent', 'ARCHITECTURE.md')));
  assert.ok(
    fs.existsSync(path.join(projectDir, '.codex', 'skills', 'locole-kit', 'SKILL.md'))
  );

  const installedSkills = fs
    .readdirSync(path.join(projectDir, '.codex', 'skills'), { withFileTypes: true })
    .filter((entry) => entry.isDirectory());
  assert.ok(installedSkills.length > 0);
});

test('refuses to overwrite an existing install without --force', (t) => {
  const projectDir = makeProjectDir(t);

  assert.equal(runCli(['init'], projectDir).status, 0);

  const secondRun = runCli(['init'], projectDir);
  assert.notEqual(secondRun.status, 0);
  assert.match(secondRun.stderr, /\.agent already exists/);
});

test('replaces an existing install with --force', (t) => {
  const projectDir = makeProjectDir(t);

  assert.equal(runCli(['init'], projectDir).status, 0);

  const markerPath = path.join(projectDir, '.agent', 'stale-marker.txt');
  fs.writeFileSync(markerPath, 'stale');
  assert.ok(fs.existsSync(markerPath));

  const forceRun = runCli(['init', '--force'], projectDir);

  assert.equal(forceRun.status, 0);
  assert.ok(!fs.existsSync(markerPath));
  assert.ok(fs.existsSync(path.join(projectDir, '.agent', 'ARCHITECTURE.md')));
  assert.ok(
    fs.existsSync(path.join(projectDir, '.codex', 'skills', 'locole-kit', 'SKILL.md'))
  );
});

test('restores the previous install if --force fails mid-flight', (t) => {
  const projectDir = makeProjectDir(t);
  const hookPath = path.join(projectDir, 'rename-hook.cjs');

  assert.equal(runCli(['init'], projectDir).status, 0);

  const originalAgentMarker = path.join(projectDir, '.agent', 'restore-agent.txt');
  const originalCodexMarker = path.join(
    projectDir,
    '.codex',
    'skills',
    'restore-codex.txt'
  );
  fs.writeFileSync(originalAgentMarker, 'keep-agent');
  fs.writeFileSync(originalCodexMarker, 'keep-codex');

  fs.writeFileSync(
    hookPath,
    `
const fs = require('node:fs');
const path = require('node:path');
const originalRenameSync = fs.renameSync;

fs.renameSync = function patchedRenameSync(source, target) {
  const sourcePath = String(source);
  const targetPath = String(target);
  const targetSuffix = path.join('.codex', 'skills');

  if (
    sourcePath.includes('.codex-skills-stage.locole-') &&
    targetPath.endsWith(targetSuffix)
  ) {
    throw new Error('simulated codex rename failure');
  }

  return originalRenameSync.apply(this, arguments);
};
`.trim()
  );

  const failedForceRun = runCli(['init', '--force'], projectDir, {
    env: {
      NODE_OPTIONS: `--require=${hookPath}`,
    },
  });

  assert.notEqual(failedForceRun.status, 0);
  assert.match(failedForceRun.stderr, /simulated codex rename failure/);
  assert.ok(fs.existsSync(originalAgentMarker));
  assert.ok(fs.existsSync(originalCodexMarker));
  assert.ok(
    fs.existsSync(path.join(projectDir, '.agent', 'ARCHITECTURE.md')),
    'original .agent install should be restored'
  );
  assert.ok(
    fs.existsSync(path.join(projectDir, '.codex', 'skills', 'locole-kit', 'SKILL.md')),
    'original .codex skills should be restored'
  );
});
