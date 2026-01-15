#!/usr/bin/env node

const { program } = require('commander');

program
  .name('mycli')
  .description('CLI tool application')
  .version('1.0.0');

program
  .command('user')
  .description('User management')
  .option('-l, --list', 'List users')
  .option('-a, --add <name>', 'Add user')
  .action((options) => {
    if (options.list) {
      console.log('Listing users...');
    }
    if (options.add) {
      console.log(`Adding user: ${options.add}`);
    }
  });

program.parse();
