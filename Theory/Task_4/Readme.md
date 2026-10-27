# Task 4: Node.js Development Tooling & Process Watching with Nodemon

## Overview
In backend development, making frequent changes to server code requires constantly restarting the server process to apply updates. **Task 4** focuses on developer productivity tools in the Node.js ecosystem, specifically process watching and automated server reloading with **Nodemon**.

**Location:** [`Theory/Task_4/`](file:///d:/Desktop/Backend%20Development/Theory/Task_4/)

---

## What is Nodemon?

`nodemon` is a command-line utility that wraps your Node.js application, monitors the file system for any file modifications (such as `.js`, `.mjs`, `.json`), and automatically restarts the server process whenever changes are saved.

### Why is it Essential in Backend Development?
1. **Eliminates Manual Restarts**: Developers do not need to switch to the terminal, terminate the process (`Ctrl + C`), and re-run `node server.js` after every line of code.
2. **Speed & Efficiency**: Instant feedback loops during debugging and feature implementation.
3. **Crash Recovery**: Automatically watches files even if your script crashes due to an unhandled exception or syntax error.

---

## Installation & Setup

### Local Project Installation
```bash
npm install --save-dev nodemon
```
*(This is already installed in this directory under `node_modules/`)*

### Global Installation (Accessible across all projects)
```bash
npm install -g nodemon
```

---

## Usage Guide

### Basic Command
Instead of running:
```bash
node server.js
```
Run:
```bash
npx nodemon server.js
# Or if installed globally:
nodemon server.js
```

### Configuration (`nodemon.json` or `package.json`)
You can customize Nodemon behavior by specifying options:
```json
{
  "watch": ["src/", "views/"],
  "ext": "js,json,ejs,html",
  "ignore": ["node_modules/", "*.test.js"],
  "delay": "500"
}
```

### Sample npm Script Configuration
In your `package.json`, configure a `dev` script:
```json
{
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  }
}
```
Run with:
```bash
npm run dev
```
