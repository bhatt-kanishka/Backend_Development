# Eisenhower Todo

## Description

Eisenhower Todo is a server-side rendered Todo application developed using Node.js, Express.js, EJS, and MongoDB.

The application organizes tasks into four Eisenhower Matrix categories based on urgency and importance:

* Do: Urgent and Important
* Schedule: Not Urgent and Important
* Delegate: Urgent and Not Important
* Eliminate: Not Urgent and Not Important

## Technologies Used

* Node.js
* Express.js
* EJS
* MongoDB
* MongoDB Node.js Driver
* HTML
* CSS
* JavaScript

## Installation

Install the required packages:

```bash
npm install express ejs mongodb
```

## MongoDB Configuration

The application uses:

* MongoDB URL: `mongodb://127.0.0.1:27017`
* Database: `todo_lab`
* Collection: `tasks`

MongoDB must be running before starting the application.

## Running the Application

Run:

```bash
node app.js
```

The application will run at:

```text
http://localhost:3000
```

## Features

* Add tasks
* Edit tasks
* Delete tasks
* Mark tasks as completed
* Eisenhower Matrix categorization
* Urgent and Important checkboxes
* Task priority
* Due dates
* Search
* Filtering
* Sorting
* Dashboard statistics
* Dark mode
* Responsive CSS Grid layout

## Main Routes

| Method | Route                    | Purpose                                    |
| ------ | ------------------------ | ------------------------------------------ |
| GET    | `/`                      | Display all tasks in the Eisenhower Matrix |
| GET    | `/tasks/new`             | Display add-task form                      |
| POST   | `/tasks`                 | Add a new task                             |
| GET    | `/tasks/:id/edit`        | Display edit form                          |
| POST   | `/tasks/:id/edit`        | Update a task                              |
| POST   | `/tasks/:id/delete`      | Delete a task                              |
| POST   | `/tasks/:id/toggle`      | Complete/incomplete task                   |
| POST   | `/tasks/clear-completed` | Delete completed tasks                     |
