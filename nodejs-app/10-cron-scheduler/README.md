# Cron Job Scheduler

Scheduled tasks using node-cron.

## Features

- Scheduled jobs
- Cron expressions
- Task management
- Job monitoring
- Email notifications

## Project Structure

```
10-cron-scheduler/
├── src/
│   ├── jobs/
│   │   ├── cleanup.js
│   │   ├── report.js
│   │   └── backup.js
│   ├── scheduler.js
│   └── server.js
├── package.json
└── README.md
```

## Installation

```bash
npm install
```

## Running

```bash
npm start
```

## Cron Schedule Examples

- `* * * * *` - Every minute
- `0 * * * *` - Every hour
- `0 0 * * *` - Every day at midnight
- `0 0 * * 0` - Every Sunday at midnight
