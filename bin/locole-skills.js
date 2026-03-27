#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

function readVersion() {
  try {
    const pkg = JSON.parse(
      fs.readFileSync(path.join(__dirname, '..', 'package.json'), 'utf8')
    );
    return pkg.version || '0.0.0';
  } catch {
    return '0.0.0';
  }
}

const VERSION = readVersion();

function printHelp() {
  console.log([
    'locole-skills',
    '',
    'Usage:',
    '  locole-skills init [--force]',
    '  locole-skills --help',
    '  locole-skills --version',
    '',
    'Commands:',
    '  init      Bootstrap the Locole .agent toolkit and .codex/skills into the current project',
    '',
    'Options:',
    '  --force   Overwrite existing .agent and .codex/skills',
  ].join('\n'));
}

function shouldSkip(name) {
  return (
    name === '__pycache__' ||
    name.endsWith('.pyc') ||
    name === '.DS_Store'
  );
}

function copyDirectory(sourceDir, targetDir, overwrite) {
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  const entries = fs.readdirSync(sourceDir, { withFileTypes: true });

  for (const entry of entries) {
    if (shouldSkip(entry.name)) {
      continue;
    }

    const sourcePath = path.join(sourceDir, entry.name);
    const targetPath = path.join(targetDir, entry.name);

    if (entry.isDirectory()) {
      copyDirectory(sourcePath, targetPath, overwrite);
      continue;
    }

    if (!overwrite && fs.existsSync(targetPath)) {
      throw new Error(`File already exists: ${targetPath}`);
    }

    fs.copyFileSync(sourcePath, targetPath);
  }
}

function countSkillDirs(skillsRoot) {
  if (!fs.existsSync(skillsRoot)) return 0;
  return fs
    .readdirSync(skillsRoot, { withFileTypes: true })
    .filter((d) => d.isDirectory()).length;
}

function makeTempPath(parentDir, label) {
  const stamp = `${process.pid}-${Date.now()}-${Math.random()
    .toString(16)
    .slice(2, 10)}`;
  return path.join(parentDir, `.${label}.locole-${stamp}`);
}

function removePathIfExists(targetPath) {
  if (!targetPath || !fs.existsSync(targetPath)) {
    return;
  }

  fs.rmSync(targetPath, { recursive: true, force: true });
}

function restoreDestination(destinationDir, backupDir) {
  if (fs.existsSync(destinationDir)) {
    removePathIfExists(destinationDir);
  }

  if (backupDir && fs.existsSync(backupDir)) {
    fs.mkdirSync(path.dirname(destinationDir), { recursive: true });
    fs.renameSync(backupDir, destinationDir);
  }
}

function runInit(args) {
  const overwrite = args.includes('--force');
  const packageRoot = path.resolve(__dirname, '..');
  const sourceAgentDir = path.join(packageRoot, '.agent');
  const sourceCodexSkills = path.join(packageRoot, '.codex', 'skills');
  const cwd = process.cwd();
  const destinationAgentDir = path.resolve(cwd, '.agent');
  const destinationCodexSkillsDir = path.resolve(cwd, '.codex', 'skills');

  if (!fs.existsSync(sourceAgentDir)) {
    console.error('[X] Packaged .agent toolkit not found.');
    process.exit(1);
  }

  if (!fs.existsSync(sourceCodexSkills)) {
    console.error('[X] Packaged .codex/skills not found.');
    process.exit(1);
  }

  const skillCount = countSkillDirs(sourceCodexSkills);
  if (skillCount === 0) {
    console.error('[X] No skills under packaged .codex/skills.');
    process.exit(1);
  }

  if (!overwrite) {
    if (fs.existsSync(destinationAgentDir)) {
      console.error(
        '[X] .agent already exists in this project. Use --force to overwrite.'
      );
      process.exit(1);
    }
    if (fs.existsSync(destinationCodexSkillsDir)) {
      console.error(
        '[X] .codex/skills already exists in this project. Use --force to overwrite.'
      );
      process.exit(1);
    }
  }

  let stagedAgentDir = null;
  let stagedCodexSkillsDir = null;
  let agentBackupDir = null;
  let codexBackupDir = null;

  try {
    stagedAgentDir = makeTempPath(cwd, 'agent-stage');
    stagedCodexSkillsDir = makeTempPath(cwd, 'codex-skills-stage');

    copyDirectory(sourceAgentDir, stagedAgentDir, true);
    copyDirectory(sourceCodexSkills, stagedCodexSkillsDir, true);

    if (overwrite && fs.existsSync(destinationAgentDir)) {
      agentBackupDir = makeTempPath(cwd, 'agent-backup');
      fs.renameSync(destinationAgentDir, agentBackupDir);
    }

    if (overwrite && fs.existsSync(destinationCodexSkillsDir)) {
      const codexParentDir = path.dirname(destinationCodexSkillsDir);
      fs.mkdirSync(codexParentDir, { recursive: true });
      codexBackupDir = makeTempPath(codexParentDir, 'skills-backup');
      fs.renameSync(destinationCodexSkillsDir, codexBackupDir);
    }

    fs.renameSync(stagedAgentDir, destinationAgentDir);
    stagedAgentDir = null;

    fs.mkdirSync(path.dirname(destinationCodexSkillsDir), { recursive: true });
    fs.renameSync(stagedCodexSkillsDir, destinationCodexSkillsDir);
    stagedCodexSkillsDir = null;

    removePathIfExists(agentBackupDir);
    removePathIfExists(codexBackupDir);
    agentBackupDir = null;
    codexBackupDir = null;

    console.log('[OK] Locole toolkit initialized successfully.');
    console.log(`[i] Toolkit: ${destinationAgentDir}`);
    console.log(
      `[OK] Copied ${skillCount} Codex skills into project: ${destinationCodexSkillsDir}`
    );
    console.log(
      '[i] Commit .agent and .codex so the team shares the same Locole toolkit and Team-scoped skills in Cursor/Codex.'
    );
    console.log(
      '[i] Restart Cursor/Codex after pull if skills do not refresh.'
    );
  } catch (error) {
    removePathIfExists(stagedAgentDir);
    removePathIfExists(stagedCodexSkillsDir);
    restoreDestination(destinationAgentDir, agentBackupDir);
    restoreDestination(destinationCodexSkillsDir, codexBackupDir);
    console.error(`[X] Init failed: ${error.message}`);
    process.exit(1);
  }
}

function main() {
  const args = process.argv.slice(2);
  const command = args[0];

  if (!command || command === '--help' || command === '-h') {
    printHelp();
    return;
  }

  if (command === '--version' || command === '-v') {
    console.log(VERSION);
    return;
  }

  if (command === 'init') {
    runInit(args.slice(1));
    return;
  }

  console.error(`[X] Unknown command: ${command}`);
  printHelp();
  process.exit(1);
}

main();
