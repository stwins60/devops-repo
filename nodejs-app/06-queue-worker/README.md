# Message Queue Worker

Worker service using Bull queue.

## Features

- Job queue processing
- Redis-backed
- Job scheduling
- Retry logic
- Progress tracking

## Project Structure

```
06-queue-worker/
├── src/
│   ├── queues/
│   │   └── email.queue.js
│   ├── processors/
│   │   └── email.processor.js
│   ├── jobs/
│   │   └── sendEmail.js
│   └── server.js
├── package.json
└── README.md
```

## Installation

```bash
npm install
```

## Running

Requires Redis server running.

```bash
npm start
```
