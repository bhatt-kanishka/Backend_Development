import os
import json

backend_dir = r'd:\Desktop\Backend_Development'
io_dir = r'd:\Desktop\bhatt-kanishka.github.io'

student_data = {
    'name': 'Kanishka Bhatt',
    'sapId': '590017366',
    'institute': 'University of Petroleum and Energy Studies (UPES)',
    'semester': '5th',
    'subject': 'Backend Development'
}

repo_info = {
    'name': 'EndpointCraft',
    'repoOwner': 'bhatt-kanishka',
    'repoName': 'Backend_Development',
    'githubUrl': 'https://github.com/bhatt-kanishka/Backend_Development',
    'pagesUrl': 'https://bhatt-kanishka.github.io/'
}

labs = [
    {
        'id': 'html5-elements-forms',
        'title': 'Semantic HTML5 Markup, Form Validation and Canvas Graphics',
        'shortTitle': 'HTML5 & Forms',
        'category': 'Frontend & Forms',
        'working': 'Constructs accessible semantic page structures, validates complex user input types, and renders programmatic 2D canvas graphics without external libraries.',
        'description': 'Semantic HTML5 structure, comprehensive form validation, native audio/video controls, and 2D canvas drawing.',
        'icon': '',
        'path': 'Lab',
        'readme': 'Lab/Experiment_1_Readme.md',
        'tree': 'Lab/\n├── Experiment-1.html\n└── Experiment_1_Readme.md',
        'files': [
            {'name': 'Experiment-1.html', 'path': 'Lab/Experiment-1.html', 'lang': 'html', 'purpose': 'Semantic HTML5 page, interactive form controls, and 2D canvas graphics'}
        ],
        'concepts': ['Semantic HTML5', 'Form Validation', 'Canvas 2D API', 'Native Audio/Video', 'Data Tables'],
        'dependencies': ['None — Pure HTML5 & CSS3'],
        'runCommand': 'Start-Process Experiment-1.html',
        'port': 'Web Browser'
    },
    {
        'id': 'es6-task-manager',
        'title': 'ES6+ Interactive Task Manager (Classes, Spread and Event Delegation)',
        'shortTitle': 'ES6 Task Manager',
        'category': 'Client-Side State',
        'working': 'Maintains an in-memory task collection utilizing ES6 class instantiation, immutable state transformations with array spread operators, and single-listener event delegation.',
        'description': 'Interactive client-side To-Do application built with ES6 classes, arrow functions, spread syntax, and event delegation.',
        'icon': '',
        'path': 'Lab/Lab_7_8',
        'readme': 'Lab/Lab_7_8/Readme.md',
        'tree': 'Lab/Lab_7_8/\n├── app.js\n├── index.html\n└── Readme.md',
        'files': [
            {'name': 'app.js', 'path': 'Lab/Lab_7_8/app.js', 'lang': 'javascript', 'purpose': 'ES6 Task class, immutable state mutations, and DOM event delegation'},
            {'name': 'index.html', 'path': 'Lab/Lab_7_8/index.html', 'lang': 'html', 'purpose': 'User interface layout with task input and styled action buttons'}
        ],
        'concepts': ['ES6 Classes', 'Spread Operator (...)', 'Arrow Functions', 'Event Delegation', 'DOM Manipulation'],
        'dependencies': ['None — Vanilla JavaScript (ES6+)'],
        'runCommand': 'Start-Process index.html',
        'port': 'Web Browser'
    },
    {
        'id': 'express-ejs-ssr-api',
        'title': 'Express.js RESTful API and Dynamic Server-Side Rendering (EJS)',
        'shortTitle': 'Express + EJS SSR',
        'category': 'REST API & SSR',
        'working': 'Initializes an Express backend web server featuring route parameter extraction, query string math calculator, JSON body parsing, and dynamic template compilation via EJS.',
        'description': 'Express.js backend server handling GET/POST endpoints, parameterized routes, query filters, and dynamic HTML page rendering with EJS.',
        'icon': '',
        'path': 'Lab/Experiment_12A',
        'readme': 'Lab/Experiment_12A/Readme.md',
        'tree': 'Lab/Experiment_12A/\n├── Readme.md\n└── nodejs-express-lab/\n    ├── app.js\n    ├── package.json\n    ├── script.js\n    └── views/\n        ├── home.ejs\n        ├── profile.ejs\n        └── users.ejs',
        'files': [
            {'name': 'app.js', 'path': 'Lab/Experiment_12A/nodejs-express-lab/app.js', 'lang': 'javascript', 'purpose': '12 REST routes, query parser, and EJS render handlers'},
            {'name': 'script.js', 'path': 'Lab/Experiment_12A/nodejs-express-lab/script.js', 'lang': 'javascript', 'purpose': 'Node.js runtime verification and array calculations'},
            {'name': 'package.json', 'path': 'Lab/Experiment_12A/nodejs-express-lab/package.json', 'lang': 'json', 'purpose': 'Node manifest with express and ejs dependencies'},
            {'name': 'home.ejs', 'path': 'Lab/Experiment_12A/nodejs-express-lab/views/home.ejs', 'lang': 'html', 'purpose': 'Dynamic greeting view with template variable interpolation'},
            {'name': 'users.ejs', 'path': 'Lab/Experiment_12A/nodejs-express-lab/views/users.ejs', 'lang': 'html', 'purpose': 'Tabular user view generated via EJS array iteration loops'},
            {'name': 'profile.ejs', 'path': 'Lab/Experiment_12A/nodejs-express-lab/views/profile.ejs', 'lang': 'html', 'purpose': 'User profile card template with bound object properties'}
        ],
        'concepts': ['Express.js Routing', 'Route Parameters (:id)', 'Query Strings (req.query)', 'EJS Templating', 'Body Parsing Middleware'],
        'dependencies': ['express: ^5.2.1', 'ejs: ^3.1.10'],
        'runCommand': 'cd Lab/Experiment_12A/nodejs-express-lab && npm install && node app.js',
        'port': 'http://localhost:3000'
    },
    {
        'id': 'state-cookies-sessions',
        'title': 'HTTP State Preservation via Client Cookies and Server Sessions',
        'shortTitle': 'Cookies & Sessions',
        'category': 'State Management',
        'working': 'Mitigates the stateless nature of HTTP by configuring cookie-parser for browser cookie lifecycles and express-session for secure, signed server-side session counters.',
        'description': 'Demonstration of client-side cookies (TTL, maxAge, clearCookie) and server-side sessions with signed connect.sid session cookies.',
        'icon': '',
        'path': 'Lab/Experiment12_B',
        'readme': 'Lab/Experiment12_B/Readme.md',
        'tree': 'Lab/Experiment12_B/\n├── Cookies_example.js\n├── session_example.js\n└── Readme.md',
        'files': [
            {'name': 'Cookies_example.js', 'path': 'Lab/Experiment12_B/Cookies_example.js', 'lang': 'javascript', 'purpose': 'Cookie setter, reader, and deleter with 15-minute TTL maxAge'},
            {'name': 'session_example.js', 'path': 'Lab/Experiment12_B/session_example.js', 'lang': 'javascript', 'purpose': 'Server-side session store, visit counter, and session destruction'}
        ],
        'concepts': ['HTTP Statelessness', 'Client Cookies', 'cookie-parser', 'Signed Server Sessions', 'express-session'],
        'dependencies': ['express: ^5.2.1', 'cookie-parser: ^1.4.7', 'express-session: ^1.18.1'],
        'runCommand': 'node Cookies_example.js  OR  node session_example.js',
        'port': 'http://localhost:3000'
    },
    {
        'id': 'django-task-manager',
        'title': 'Full-Stack Django MVT Task Manager with External API Integration',
        'shortTitle': 'Django MVT App',
        'category': 'Full-Stack Framework',
        'working': 'Implements a database-backed Django web application using SQLite ORM models, migration pipelines, function-based CRUD views, template inheritance, and HTTP requests to JSONPlaceholder external API with timeout and error handling.',
        'description': 'Full-stack Django web application featuring SQLite ORM models, migration pipelines, template inheritance, and external REST API consumption.',
        'icon': '',
        'path': 'Lab/Lecture 15',
        'readme': 'Lab/Lecture 15/README.md',
        'tree': 'Lab/Lecture 15/\n├── manage.py\n├── pyproject.toml\n├── README.md\n├── todo/\n│   ├── models.py\n│   ├── views.py\n│   ├── urls.py\n│   └── utils.py\n└── todo_project/\n    └── settings.py',
        'files': [
            {'name': 'models.py', 'path': 'Lab/Lecture 15/todo/models.py', 'lang': 'python', 'purpose': 'Django ORM Task model definition with title, completed, created_at'},
            {'name': 'views.py', 'path': 'Lab/Lecture 15/todo/views.py', 'lang': 'python', 'purpose': 'Function-based views for CRUD actions and external API consumption'},
            {'name': 'urls.py', 'path': 'Lab/Lecture 15/todo/urls.py', 'lang': 'python', 'purpose': 'App route dispatcher with parameterized integer path converters'},
            {'name': 'utils.py', 'path': 'Lab/Lecture 15/todo/utils.py', 'lang': 'python', 'purpose': 'External REST client fetching JSONPlaceholder posts with error safety'},
            {'name': 'manage.py', 'path': 'Lab/Lecture 15/manage.py', 'lang': 'python', 'purpose': 'Django administrative script for running migrations and local server'},
            {'name': 'pyproject.toml', 'path': 'Lab/Lecture 15/pyproject.toml', 'lang': 'toml', 'purpose': 'Modern Python packaging configuration specifying Python >=3.14'}
        ],
        'concepts': ['Django MVT Pattern', 'Django ORM', 'Schema Migrations', 'Template Inheritance', 'External API Client', '@require_POST'],
        'dependencies': ['python: >=3.14', 'django: 5.x', 'requests: ^2.31.0'],
        'runCommand': 'cd "Lab/Lecture 15" && python manage.py migrate && python manage.py runserver',
        'port': 'http://127.0.0.1:8000'
    },
    {
        'id': 'fastapi-student-orm-api',
        'title': 'Production Student Management REST API (FastAPI + SQLAlchemy)',
        'shortTitle': 'FastAPI Student API',
        'category': 'Enterprise REST API',
        'working': 'Delivers an enterprise-grade REST service for Students, Courses, and Enrollments with Pydantic v2 schemas, database session dependency injection, branch filtering, search, pagination, and cascade delete safeguards.',
        'description': 'Production-ready REST API built with FastAPI, SQLAlchemy ORM, and Pydantic validation, featuring full CRUD, pagination, filtering, and cascade integrity.',
        'icon': '',
        'path': 'Lab/student_api',
        'readme': 'Lab/student_api/README.md',
        'tree': 'Lab/student_api/\n├── database.py\n├── main.py\n├── models.py\n├── schemas.py\n├── requirements.txt\n├── .env\n└── README.md',
        'files': [
            {'name': 'main.py', 'path': 'Lab/student_api/main.py', 'lang': 'python', 'purpose': 'FastAPI route endpoints with status codes, query params, and DI'},
            {'name': 'database.py', 'path': 'Lab/student_api/database.py', 'lang': 'python', 'purpose': 'SQLAlchemy engine, sessionmaker, and get_db session generator'},
            {'name': 'models.py', 'path': 'Lab/student_api/models.py', 'lang': 'python', 'purpose': 'SQLAlchemy ORM models: Department, Student, Course, Enrollment'},
            {'name': 'schemas.py', 'path': 'Lab/student_api/schemas.py', 'lang': 'python', 'purpose': 'Pydantic v2 validation schemas with EmailStr and BranchEnum'},
            {'name': 'requirements.txt', 'path': 'Lab/student_api/requirements.txt', 'lang': 'text', 'purpose': 'Package dependency manifest for FastAPI and SQLAlchemy stack'},
            {'name': '.env', 'path': 'Lab/student_api/.env', 'lang': 'text', 'purpose': 'Environment configuration setting SQLite database URI'}
        ],
        'concepts': ['FastAPI Framework', 'SQLAlchemy ORM', 'Pydantic v2 Validation', 'Dependency Injection (Depends)', 'Pagination & Filtering', 'Cascade Deletion'],
        'dependencies': ['fastapi: ^0.115.0', 'uvicorn: ^0.30.0', 'sqlalchemy: ^2.0.0', 'python-dotenv: ^1.0.0', 'pydantic[email]: ^2.8.0'],
        'runCommand': 'cd Lab/student_api && pip install -r requirements.txt && python main.py',
        'port': 'http://127.0.0.1:8000 (Docs: /docs)'
    },
    {
        'id': 'eisenhower-matrix-todo',
        'title': 'Eisenhower Priority Decision Matrix Task System (Express + MongoDB)',
        'shortTitle': 'Eisenhower Matrix Todo',
        'category': 'Full-Stack Database App',
        'working': 'Organizes actionable tasks into 4 urgent/important decision quadrants using native MongoDB driver aggregations, dynamic EJS dashboards, priority scoring, due-date tracking, and dark mode.',
        'description': 'Full-stack task management application implementing the Eisenhower Decision Matrix with Express.js, native MongoDB driver, and EJS views.',
        'icon': '',
        'path': 'Lab/lab_Assessment_B',
        'readme': 'Lab/lab_Assessment_B/Readme.md',
        'tree': 'Lab/lab_Assessment_B/\n├── app.js\n├── package.json\n├── Readme.md\n├── public/\n│   ├── script.js\n│   └── style.css\n└── views/\n    ├── edit-task.ejs\n    ├── index.ejs\n    ├── new-task.ejs\n    └── task-card.ejs',
        'files': [
            {'name': 'app.js', 'path': 'Lab/lab_Assessment_B/app.js', 'lang': 'javascript', 'purpose': '730-line Express server with native MongoDB CRUD & quadrant calculations'},
            {'name': 'package.json', 'path': 'Lab/lab_Assessment_B/package.json', 'lang': 'json', 'purpose': 'Project manifest with express, ejs, and mongodb driver'},
            {'name': 'script.js', 'path': 'Lab/lab_Assessment_B/public/script.js', 'lang': 'javascript', 'purpose': 'Client-side interactions, modal popups, and dark mode theme toggler'},
            {'name': 'style.css', 'path': 'Lab/lab_Assessment_B/public/style.css', 'lang': 'css', 'purpose': 'Responsive CSS grid styling for Eisenhower quadrant dashboard'},
            {'name': 'index.ejs', 'path': 'Lab/lab_Assessment_B/views/index.ejs', 'lang': 'html', 'purpose': 'Main Eisenhower matrix view displaying all 4 prioritized quadrants'},
            {'name': 'new-task.ejs', 'path': 'Lab/lab_Assessment_B/views/new-task.ejs', 'lang': 'html', 'purpose': 'Task creation form with urgent/important switches and due dates'},
            {'name': 'edit-task.ejs', 'path': 'Lab/lab_Assessment_B/views/edit-task.ejs', 'lang': 'html', 'purpose': 'Task editor form pre-populated with existing document state'},
            {'name': 'task-card.ejs', 'path': 'Lab/lab_Assessment_B/views/task-card.ejs', 'lang': 'html', 'purpose': 'Reusable card partial with toggle, delete, and priority indicators'}
        ],
        'concepts': ['Native MongoDB Driver', 'ObjectId Manipulation', 'Eisenhower Decision Matrix', 'CRUD Operations', 'Quadrant Aggregations', 'Dark Mode UI'],
        'dependencies': ['express: ^4.19.2', 'ejs: ^3.1.10', 'mongodb: ^6.8.0'],
        'runCommand': 'cd Lab/lab_Assessment_B && npm install && node app.js',
        'port': 'http://localhost:3000'
    }
]

theory = [
    {
        'id': 'http-rest-foundations',
        'title': 'Core Backend Architecture and HTTP/REST Protocol Foundations',
        'shortTitle': 'HTTP & REST Foundations',
        'category': 'Architectural Principles',
        'working': 'Establishes foundational understanding of client-server separation, stateless request-response lifecycles, HTTP method idempotency, status code hierarchies, and REST architectural constraints.',
        'description': 'Theoretical foundations of backend web development, covering client-server architecture, HTTP/1.1 protocols, status code categories, and REST constraints.',
        'icon': '',
        'path': 'Theory/Unit-1',
        'readme': 'Theory/Unit-1/Readme.md',
        'files': [],
        'concepts': ['Client-Server Separation', 'HTTP Request/Response Cycle', 'Method Idempotency & Safety', 'Status Codes (1xx-5xx)', 'REST Architectural Constraints'],
        'dependencies': ['None — Architectural Theory'],
        'runCommand': 'Refer to documentation guidelines',
        'port': 'N/A'
    },
    {
        'id': 'flask-student-api',
        'title': 'Flask Microframework Student REST API with JSON Serialization',
        'shortTitle': 'Flask Student API',
        'category': 'Python Microframeworks',
        'working': 'Exposes synchronous RESTful endpoints using Flask, handling integer URL path variables for individual student lookups, JSON serialization with jsonify(), and explicit 404 status codes.',
        'description': 'Python Flask REST API illustrating microframework routing patterns, integer path variable casting, JSON response formatting, and 404 error handling.',
        'icon': '',
        'path': 'Theory/task-2',
        'readme': 'Theory/task-2/Readme.md',
        'files': [
            {'name': 'app.py', 'path': 'Theory/task-2/app.py', 'lang': 'python', 'purpose': 'Flask API server with GET /students and GET /students/<int:id> handlers'}
        ],
        'concepts': ['Flask Framework', 'Synchronous WSGI', 'Path Variable Casting', 'jsonify() Serialization', 'HTTP 404 Handling'],
        'dependencies': ['flask: 3.x'],
        'runCommand': 'cd Theory/task-2 && python app.py',
        'port': 'http://127.0.0.1:5000'
    },
    {
        'id': 'fastapi-async-swagger',
        'title': 'FastAPI Asynchronous Microservice with Interactive Swagger UI',
        'shortTitle': 'FastAPI Async API',
        'category': 'Asynchronous APIs',
        'working': 'Spins up a lightweight ASGI web service using FastAPI and Uvicorn, demonstrating asynchronous route handlers, JSON serialization, and auto-generated OpenAPI / Swagger UI at /docs.',
        'description': 'Modern high-performance asynchronous Python REST API built with FastAPI and Uvicorn, featuring auto-generated interactive OpenAPI documentation.',
        'icon': '',
        'path': 'Theory/Task_3',
        'readme': 'Theory/Task_3/Readme.md',
        'files': [
            {'name': 'main.py', 'path': 'Theory/Task_3/main.py', 'lang': 'python', 'purpose': 'FastAPI application instance with root endpoint and Uvicorn server runner'}
        ],
        'concepts': ['FastAPI', 'ASGI Architecture', 'Uvicorn Server', 'Automatic Swagger UI (/docs)', 'Type-Safe Handlers'],
        'dependencies': ['fastapi: ^0.115.0', 'uvicorn: ^0.30.0'],
        'runCommand': 'cd Theory/Task_3 && python main.py',
        'port': 'http://127.0.0.1:8000 (Docs: /docs)'
    },
    {
        'id': 'nodemon-dev-workflow',
        'title': 'Live-Reloading Developer Workflow with Nodemon and File Watchers',
        'shortTitle': 'Nodemon DX Watcher',
        'category': 'Developer Experience',
        'working': 'Leverages file system monitoring (via Chokidar/Nodemon) to detect source changes and automatically trigger process restarts, eliminating manual Node.js termination during development.',
        'description': 'Developer experience (DX) tooling exploring file system watchers, process termination, and automatic hot-reloading using Nodemon.',
        'icon': '',
        'path': 'Theory/Task_4',
        'readme': 'Theory/Task_4/Readme.md',
        'files': [],
        'concepts': ['Developer Experience (DX)', 'File System Watchers', 'Process Lifecycle', 'Nodemon Configuration', 'Hot Reloading'],
        'dependencies': ['nodemon: ^3.1.0'],
        'runCommand': 'npx nodemon <server-file>.js',
        'port': 'Development Tooling'
    },
    {
        'id': 'fastapi-jinja2-ssr',
        'title': 'Server-Side Rendering (SSR) with FastAPI and Jinja2 HTML Templates',
        'shortTitle': 'FastAPI + Jinja2 SSR',
        'category': 'Server-Side Templating',
        'working': 'Demonstrates server-side HTML rendering by injecting dynamic Python data lists into Jinja2 templates using template inheritance, iteration loops ({% for %}), and conditional blocks.',
        'description': 'Server-Side Rendering architecture using FastAPI and Jinja2 templates, exploring server HTML compilation versus client-side rendering (CSR).',
        'icon': '',
        'path': 'Theory/ssr_demmo_Task_5',
        'readme': 'Theory/ssr_demmo_Task_5/Readme.md',
        'files': [
            {'name': 'main.py', 'path': 'Theory/ssr_demmo_Task_5/main.py', 'lang': 'python', 'purpose': 'FastAPI application mounting Jinja2Templates directory and rendering HTMLResponse'},
            {'name': 'home.html', 'path': 'Theory/ssr_demmo_Task_5/Templates/home.html', 'lang': 'html', 'purpose': 'Base HTML view template with heading and introductory layout'},
            {'name': 'students.html', 'path': 'Theory/ssr_demmo_Task_5/Templates/students.html', 'lang': 'html', 'purpose': 'Dynamic table view iterating through student records using Jinja2 loops'}
        ],
        'concepts': ['Server-Side Rendering (SSR)', 'Jinja2 Template Engine', 'Template Context Injection', 'SSR vs CSR Comparison', 'HTMLResponse'],
        'dependencies': ['fastapi: ^0.115.0', 'jinja2: ^3.1.0', 'uvicorn: ^0.30.0'],
        'runCommand': 'cd Theory/ssr_demmo_Task_5 && python main.py',
        'port': 'http://127.0.0.1:8000'
    },
    {
        'id': 'client-web-storage',
        'title': 'Client-Side Data Persistence: localStorage vs sessionStorage',
        'shortTitle': 'Web Storage API',
        'category': 'Client-Side Storage',
        'working': 'Contrasts long-term persistent storage (localStorage) against browser tab-scoped storage (sessionStorage) through an interactive To-Do application with JSON serialization.',
        'description': 'Web Storage API practical demonstration comparing localStorage lifetime against sessionStorage lifecycle in a browser-based task application.',
        'icon': '',
        'path': 'Theory/Task-6',
        'readme': 'Theory/Task-6/Readme.md',
        'files': [
            {'name': 'script.js', 'path': 'Theory/Task-6/lecture7/script.js', 'lang': 'javascript', 'purpose': 'localStorage reading/writing, sessionStorage caching, and DOM task rendering'},
            {'name': 'index.html', 'path': 'Theory/Task-6/lecture7/index.html', 'lang': 'html', 'purpose': 'Task input UI with Delete and Clear Storage action controls'},
            {'name': 'style.css', 'path': 'Theory/Task-6/lecture7/style.css', 'lang': 'css', 'purpose': 'Responsive stylesheet with clean form cards and button states'}
        ],
        'concepts': ['localStorage (Persistent)', 'sessionStorage (Tab Lifecycle)', 'JSON.stringify / parse', 'DOM Mutation', 'Storage Quota Limits (~5MB)'],
        'dependencies': ['None — Native Web Storage API'],
        'runCommand': 'Start-Process Theory/Task-6/lecture7/index.html',
        'port': 'Web Browser'
    },
    {
        'id': 'express-server-routing',
        'title': 'Express.js Server Bootstrapping and Fundamental HTTP Routing',
        'shortTitle': 'Express Route Basics',
        'category': 'Server Bootstrapping',
        'working': 'Provides minimal initialization of an Express.js HTTP application, registering basic GET routes for index and student resources with custom port binding.',
        'description': 'Express.js HTTP server intro demonstrating application bootstrapping, endpoint registration, callback handlers, and port listening.',
        'icon': '',
        'path': 'Theory/express-demo',
        'readme': 'Theory/express-demo/Readme.md',
        'files': [
            {'name': 'server.js', 'path': 'Theory/express-demo/server.js', 'lang': 'javascript', 'purpose': 'Express app initialization, route registration (/students), and app.listen'},
            {'name': 'package.json', 'path': 'Theory/express-demo/package.json', 'lang': 'json', 'purpose': 'Project dependencies configuration specifying Express 5.x'}
        ],
        'concepts': ['Express Server Instantiation', 'GET Route Registration', 'HTTP Request/Response Handling', 'Local Port Listening'],
        'dependencies': ['express: ^5.2.1'],
        'runCommand': 'cd Theory/express-demo && node server.js',
        'port': 'http://localhost:3000'
    },
    {
        'id': 'relational-document-orm-odm',
        'title': 'Relational and Document Data Modeling (SQLAlchemy ORM + Mongoose ODM)',
        'shortTitle': 'SQLAlchemy & Mongoose ORM',
        'category': 'Data Modeling & ORM/ODM',
        'working': 'Architects conceptual, logical, and physical models, verifying bidirectional relationships and cascade deletions in SQLAlchemy, schema validations in Mongoose, and HTTP 422 interception via Pydantic.',
        'description': 'Comprehensive masterclass on data modeling across relational (SQLAlchemy/PostgreSQL) and document (Mongoose/MongoDB) databases, including Pydantic validation pipelines and an E-Commerce PBL activity.',
        'icon': '',
        'path': 'Theory/Lecture_15',
        'readme': 'Theory/Lecture_15/ORM/Readme.md',
        'files': [
            {'name': 'Database.py', 'path': 'Theory/Lecture_15/ORM/Database.py', 'lang': 'python', 'purpose': 'SQLAlchemy Student Management System with bidirectional relationships & cascade delete verification'},
            {'name': 'ecommerce_models.py', 'path': 'Theory/Lecture_15/ORM/ecommerce_models.py', 'lang': 'python', 'purpose': 'E-Commerce relational models (Customer, Product, Cart, Order) with order placement workflow'},
            {'name': 'fastapi_pydantic_validation.py', 'path': 'Theory/Lecture_15/ORM/fastapi_pydantic_validation.py', 'lang': 'python', 'purpose': 'FastAPI endpoint validating StudentCreate schemas with regex patterns and email checks'},
            {'name': 'test_fastapi_validation.py', 'path': 'Theory/Lecture_15/ORM/test_fastapi_validation.py', 'lang': 'python', 'purpose': 'Automated validation test suite asserting HTTP 201 Created and HTTP 422 Unprocessable Entity'},
            {'name': 'mongoose_models.js', 'path': 'Theory/Lecture_15/ORM/mongoose_models.js', 'lang': 'javascript', 'purpose': 'Mongoose schemas for Students and Blog (Posts & embedded Comments) with built-in validators'},
            {'name': 'ecommerce_mongoose.js', 'path': 'Theory/Lecture_15/ORM/ecommerce_mongoose.js', 'lang': 'javascript', 'purpose': 'E-Commerce document models in Mongoose with embedded items and schema validations'},
            {'name': 'physical_schema.sql', 'path': 'Theory/Lecture_15/ORM/physical_schema.sql', 'lang': 'sql', 'purpose': 'PostgreSQL DDL schema with primary keys, foreign key cascades, check constraints, and indexes'},
            {'name': 'save_to_mongodb.js', 'path': 'Theory/Lecture_15/ORM/save_to_mongodb.js', 'lang': 'javascript', 'purpose': 'Populator script connecting to MongoDB and seeding initial collections'},
            {'name': 'run_all.py', 'path': 'Theory/Lecture_15/ORM/run_all.py', 'lang': 'python', 'purpose': 'Master test orchestrator executing all ORM and validation modules sequentially'}
        ],
        'concepts': ['Conceptual / Logical / Physical Modeling', 'SQLAlchemy ORM (back_populates)', 'Cascade Deletion Integrity', 'Mongoose ODM Schemas', 'Pydantic v2 Request Validation', 'PostgreSQL Physical DDL'],
        'dependencies': ['sqlalchemy: ^2.0.0', 'mongoose: ^8.16.1', 'fastapi: ^0.115.0', 'pydantic[email]: ^2.8.0'],
        'runCommand': 'cd Theory/Lecture_15/ORM && python run_all.py',
        'port': 'CLI Output / Automated Tests'
    },
    {
        'id': 'database-crud-acid-pooling',
        'title': 'Database CRUD Operations Lifecycle, ACID Transactions and Connection Pooling',
        'shortTitle': 'Database CRUD & ACID',
        'category': 'Database Architecture',
        'working': 'Translates conceptual schemas into safe CRUD interactions, examining ACID transaction guarantees, rollback safety, connection pooling overhead mitigation, and pagination.',
        'description': 'Database operational architecture covering CRUD mapping across SQL and NoSQL, ACID transaction management, connection pool optimization, and memory-safe query pagination.',
        'icon': '',
        'path': 'Theory/Lecture_16',
        'readme': 'Theory/Lecture_16/Readme.md',
        'files': [],
        'concepts': ['CRUD Lifecycle (Create, Read, Update, Delete)', 'ACID Transactions & Rollbacks', 'Foreign Key Cascade Constraints', 'Connection Pooling', 'Pagination (LIMIT/OFFSET)'],
        'dependencies': ['None — Database Architecture Reference'],
        'runCommand': 'Refer to documentation guidelines',
        'port': 'N/A'
    },
    {
        'id': 'docker-compose-multi-db',
        'title': 'Containerized Multi-Database Environment with Docker Compose',
        'shortTitle': 'Docker Multi-DB Stack',
        'category': 'DevOps & Containers',
        'working': 'Orchestrates isolated PostgreSQL and MongoDB database engines with companion web administration GUIs (pgAdmin and Mongo Express) over a private Docker bridge network with persistent volumes.',
        'description': 'Multi-container database environment orchestrated via Docker Compose, provisioning PostgreSQL, MongoDB, pgAdmin, and Mongo Express with secure local port bindings.',
        'icon': '',
        'path': 'Theory/unit-4',
        'readme': 'Theory/unit-4/README.md',
        'tree': 'Theory/unit-4/\n└── docker/\n    └── docker-compose/\n        └── docker-compose.yml',
        'files': [
            {'name': 'docker-compose.yml', 'path': 'Theory/unit-4/docker/docker-compose/docker-compose.yml', 'lang': 'yaml', 'purpose': 'Multi-service configuration for PostgreSQL, MongoDB, pgAdmin, and Mongo Express'}
        ],
        'concepts': ['Docker Compose Orchestration', 'Internal Container Networking', 'Persistent Named Volumes', 'Localhost Host Port Binding', 'Environment Variable Defaults'],
        'dependencies': ['Docker Desktop: v20+', 'Docker Compose: v2+'],
        'runCommand': 'cd Theory/unit-4/docker/docker-compose && docker compose up -d',
        'port': 'pgAdmin: :8094 | Mongo Express: :8081'
    },
    {
        'id': 'express-docker-container',
        'title': 'Dockerized Express.js Microservice with Host Binding (0.0.0.0)',
        'shortTitle': 'Express in Docker',
        'category': 'DevOps & Containers',
        'working': 'Packages an Express API inside a containerized Linux runtime, demonstrating host interface binding (0.0.0.0) so Docker port forwarders can route inbound host requests.',
        'description': 'Express.js containerization demonstration highlighting network binding across 0.0.0.0 and port forwarding from host to container.',
        'icon': '',
        'path': 'Theory/Express_in_Docker',
        'readme': 'Theory/Express_in_Docker/README.md',
        'tree': 'Theory/Express_in_Docker/\n├── app.js\n├── package.json\n└── README.md',
        'files': [
            {'name': 'app.js', 'path': 'Theory/Express_in_Docker/app.js', 'lang': 'javascript', 'purpose': 'Express application binding to 0.0.0.0:3000 with GET / and /api/students'},
            {'name': 'package.json', 'path': 'Theory/Express_in_Docker/package.json', 'lang': 'json', 'purpose': 'Node manifest configuring nodemon live development workflow'}
        ],
        'concepts': ['Docker Containerization', 'Network Host Binding (0.0.0.0)', 'Port Mapping (-p 3000:3000)', 'Nodemon in Containers'],
        'dependencies': ['express: ^5.1.0', 'nodemon: ^3.1.0', 'docker: v20+'],
        'runCommand': 'cd Theory/Express_in_Docker && npm install && npm start',
        'port': 'http://localhost:3000'
    }
]

course_plan = {
    'title': 'Course Plan — Backend Development',
    'units': [
        {
            'name': 'Unit 1: Core Architecture & Web Protocols',
            'topics': [
                'Client-Server Architecture & Stateless Design',
                'HTTP Request/Response Lifecycle',
                'HTTP Methods: GET, POST, PUT, DELETE, PATCH',
                'Status Code Classes: 1xx, 2xx, 3xx, 4xx, 5xx',
                'REST Architectural Constraints',
                'Resource-Based URI Design'
            ]
        },
        {
            'name': 'Unit 2: Backend Frameworks & Routing',
            'topics': [
                'Flask Microframework — WSGI routing & JSON responses',
                'FastAPI — ASGI, async, Swagger UI auto-generation',
                'Express.js — Event loop, middleware, route parameters',
                'Nodemon — File-watcher developer experience',
                'Server-Side Rendering with EJS & Jinja2 templates',
                'Client-Side vs Server-Side Rendering comparison'
            ]
        },
        {
            'name': 'Unit 3: State Management & Storage',
            'topics': [
                'HTTP Statelessness and Mitigation Strategies',
                'Client-Side Cookies (cookie-parser)',
                'Server-Side Sessions (express-session)',
                'Web Storage API: localStorage vs sessionStorage',
                'JSON Serialization for Browser Storage'
            ]
        },
        {
            'name': 'Unit 4: Database Management & Data Modeling',
            'topics': [
                'Conceptual, Logical, Physical Data Models',
                'ER Diagram Design and Cardinality',
                'SQLAlchemy ORM — Models, Relationships, Cascades',
                'Mongoose ODM — Schemas, Validators, Subdocuments',
                'Pydantic Data Validation Pipelines',
                'CRUD Operations Lifecycle (Create, Read, Update, Delete)',
                'ACID Transactions & Connection Pooling',
                'Docker Compose for Database Environments',
                'PostgreSQL & MongoDB Administration'
            ]
        },
        {
            'name': 'Unit 5: Full-Stack Integration & Assessment',
            'topics': [
                'Full-Stack CRUD with Express + EJS + MongoDB',
                'Eisenhower Matrix Task Prioritization',
                'Django MVT Pattern — Models, Views, Templates',
                'FastAPI + SQLAlchemy Production API Architecture',
                'Pagination, Search, and Filtering',
                'Dependency Injection Patterns'
            ]
        }
    ]
}

syllabus = {
    'title': 'Syllabus — Backend Development',
    'subject': 'Backend Development',
    'code': 'CSXXX',
    'credits': 4,
    'courseOutcomes': [
        'CO1: Understand client-server architecture, HTTP protocols, and REST principles',
        'CO2: Design data models that translate business requirements into database structures',
        'CO3: Implement server-side applications using Node.js/Express, Python/FastAPI, and Python/Flask',
        'CO4: Build and consume RESTful APIs with proper status codes and validation',
        'CO5: Manage application state using cookies, sessions, and browser storage',
        'CO6: Perform CRUD operations using ORM (SQLAlchemy) and ODM (Mongoose) frameworks'
    ],
    'technologies': [
        {'name': 'Node.js', 'category': 'Runtime', 'role': 'Primary JavaScript execution environment', 'version': 'v20+'},
        {'name': 'Express.js', 'category': 'Framework', 'role': 'REST APIs & SSR routing', 'version': '^5.2.1'},
        {'name': 'Python', 'category': 'Runtime', 'role': 'Data modeling & modern backend services', 'version': '3.14'},
        {'name': 'FastAPI', 'category': 'Framework', 'role': 'High-performance ASGI REST APIs', 'version': '0.115+'},
        {'name': 'Flask', 'category': 'Framework', 'role': 'Microframework REST APIs', 'version': '3.x'},
        {'name': 'Django', 'category': 'Framework', 'role': 'Full-stack MVT applications', 'version': '5.x'},
        {'name': 'SQLAlchemy', 'category': 'ORM', 'role': 'Relational database mapping', 'version': '2.0+'},
        {'name': 'Mongoose', 'category': 'ODM', 'role': 'MongoDB document modeling', 'version': '^8.16.1'},
        {'name': 'PostgreSQL', 'category': 'Database', 'role': 'Production relational database', 'version': '16 / latest'},
        {'name': 'MongoDB', 'category': 'Database', 'role': 'NoSQL document database', 'version': '7.0'},
        {'name': 'SQLite', 'category': 'Database', 'role': 'Development & testing database', 'version': 'Built-in'},
        {'name': 'Docker Compose', 'category': 'DevOps', 'role': 'Multi-service containerization', 'version': 'v2+'},
        {'name': 'EJS / Jinja2', 'category': 'Templating', 'role': 'Server-side HTML rendering', 'version': 'Latest'},
        {'name': 'Pydantic', 'category': 'Validation', 'role': 'Request data validation with EmailStr', 'version': 'v2'}
    ]
}

# Cache all files
cache = {}
all_paths = set()
for lab in labs:
    if lab.get('readme'):
        all_paths.add(lab['readme'])
    for f in lab.get('files', []):
        all_paths.add(f['path'])

for th in theory:
    if th.get('readme'):
        all_paths.add(th['readme'])
    for f in th.get('files', []):
        all_paths.add(f['path'])

for p in all_paths:
    fp = os.path.join(backend_dir, p.replace('/', os.sep))
    if os.path.isfile(fp):
        with open(fp, 'r', encoding='utf-8', errors='replace') as f:
            cache[p] = f.read()

manifest = {
    'student': student_data,
    'repo': repo_info,
    'labs': labs,
    'theory': theory,
    'coursePlan': course_plan,
    'syllabus': syllabus,
    'cache': cache
}

# Write content.json in bhatt-kanishka.github.io
json_path_io = os.path.join(io_dir, 'content.json')
with open(json_path_io, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print('Wrote:', json_path_io)

# Write content.json in Backend_Development
json_path_bd = os.path.join(backend_dir, 'content.json')
with open(json_path_bd, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print('Wrote:', json_path_bd)

# Write js/content.js in bhatt-kanishka.github.io
raw_base_str = "https://raw.githubusercontent.com/" + repo_info['repoOwner'] + "/" + repo_info['repoName'] + "/main"
github_base_str = "https://github.com/" + repo_info['repoOwner'] + "/" + repo_info['repoName']

js_content = f"""// EndpointCraft Content Manifest & Embedded Cache
const REPO_OWNER = {json.dumps(repo_info['repoOwner'])};
const REPO_NAME = {json.dumps(repo_info['repoName'])};
const RAW_BASE = "{raw_base_str}";
const GITHUB_BASE = "{github_base_str}";

const STUDENT = {json.dumps(student_data, indent=2, ensure_ascii=False)};
const LABS = {json.dumps(labs, indent=2, ensure_ascii=False)};
const THEORY = {json.dumps(theory, indent=2, ensure_ascii=False)};
const COURSE_PLAN = {json.dumps(course_plan, indent=2, ensure_ascii=False)};
const SYLLABUS = {json.dumps(syllabus, indent=2, ensure_ascii=False)};
const EMBEDDED_CACHE = {json.dumps(cache, indent=2, ensure_ascii=False)};
"""

js_path_io = os.path.join(io_dir, 'js', 'content.js')
with open(js_path_io, 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Wrote:', js_path_io)

# Write js/content.js in Backend_Development
os.makedirs(os.path.join(backend_dir, 'js'), exist_ok=True)
js_path_bd = os.path.join(backend_dir, 'js', 'content.js')
with open(js_path_bd, 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Wrote:', js_path_bd)

print('Manifest generation complete!')
