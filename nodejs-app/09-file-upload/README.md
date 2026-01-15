# File Upload Service

File upload service with Multer.

## Features

- File upload handling
- Multiple file support
- File type validation
- Storage management
- Image processing

## Project Structure

```
09-file-upload/
├── src/
│   ├── routes/
│   │   └── upload.js
│   ├── middleware/
│   │   └── multer.js
│   ├── uploads/
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

## Endpoints

- POST /upload - Upload single file
- POST /upload/multiple - Upload multiple files
