const express = require("express");
const path = require("path");
const { MongoClient, ObjectId } = require("mongodb");

const app = express();
const PORT = 3000;

// ===============================
// MONGODB
// ===============================

const mongoURL = "mongodb://127.0.0.1:27017";
const client = new MongoClient(mongoURL);

let tasksCollection;


// ===============================
// CONNECT DATABASE
// ===============================

async function connectDB() {

    await client.connect();

    const database = client.db("todo_lab");

    tasksCollection = database.collection("tasks");

    console.log("MongoDB connected");
}


// ===============================
// EXPRESS CONFIGURATION
// ===============================

app.set("view engine", "ejs");

app.set(
    "views",
    path.join(__dirname, "views")
);

app.use(
    express.urlencoded({
        extended: true
    })
);

app.use(
    express.static(
        path.join(__dirname, "public")
    )
);


// ===============================
// HOME PAGE
// ===============================

app.get("/", async (req, res) => {

    try {

        const tasks = await tasksCollection
            .find()
            .sort({
                createdAt: -1
            })
            .toArray();


        // =========================
        // DASHBOARD COUNTS
        // =========================

        const counts = {

            total: tasks.length,

            completed: 0,

            pending: 0,

            overdue: 0,

            today: 0,

            do: 0,

            schedule: 0,

            delegate: 0,

            eliminate: 0
        };


        const today = new Date();

        today.setHours(
            0,
            0,
            0,
            0
        );


        tasks.forEach(task => {

            // Completed / Pending

            if (task.completed) {

                counts.completed++;

            } else {

                counts.pending++;

            }


            // Quadrants

            if (
                task.isUrgent &&
                task.isImportant
            ) {

                counts.do++;

            }

            else if (
                !task.isUrgent &&
                task.isImportant
            ) {

                counts.schedule++;

            }

            else if (
                task.isUrgent &&
                !task.isImportant
            ) {

                counts.delegate++;

            }

            else {

                counts.eliminate++;

            }


            // Date checks

            if (task.dueDate) {

                const dueDate = new Date(
                    task.dueDate
                );

                dueDate.setHours(
                    0,
                    0,
                    0,
                    0
                );


                // Overdue

                if (
                    dueDate < today &&
                    !task.completed
                ) {

                    counts.overdue++;

                }


                // Due today

                if (
                    dueDate.getTime() ===
                    today.getTime()
                ) {

                    counts.today++;

                }

            }

        });


        res.render(
            "index",
            {
                tasks: tasks,
                counts: counts
            }
        );


    } catch (error) {

        console.log(error);

        res.status(500)
            .send("Error loading tasks");

    }

});


// ===============================
// NEW TASK PAGE
// ===============================

app.get(
    "/tasks/new",
    (req, res) => {

        res.render(
            "new-task"
        );

    }
);


// ===============================
// ADD TASK
// ===============================

app.post(
    "/tasks",
    async (req, res) => {

        try {

            const title =
                req.body.title;

            const description =
                req.body.description;


            // Validation

            if (
                !title ||
                title.trim() === ""
            ) {

                return res
                    .status(400)
                    .send(
                        "Task title is required"
                    );

            }


            const task = {

                title: title.trim(),

                description:
                    description
                        ? description.trim()
                        : "",

                isUrgent:
                    req.body.isUrgent === "on",

                isImportant:
                    req.body.isImportant === "on",

                priority:
                    req.body.priority || "Medium",

                dueDate:
                    req.body.dueDate
                        ? new Date(
                            req.body.dueDate
                        )
                        : null,

                completed: false,

                createdAt: new Date()

            };


            await tasksCollection
                .insertOne(task);


            res.redirect("/");


        } catch (error) {

            console.log(error);

            res.status(500)
                .send(
                    "Error adding task"
                );

        }

    }
);


// ===============================
// EDIT TASK PAGE
// ===============================

app.get(
    "/tasks/:id/edit",
    async (req, res) => {

        try {

            const id =
                req.params.id;


            if (
                !ObjectId.isValid(id)
            ) {

                return res
                    .status(400)
                    .send(
                        "Invalid task ID"
                    );

            }


            const task =
                await tasksCollection
                    .findOne({
                        _id:
                            new ObjectId(id)
                    });


            if (!task) {

                return res
                    .status(404)
                    .send(
                        "Task not found"
                    );

            }


            res.render(
                "edit-task",
                {
                    task: task
                }
            );


        } catch (error) {

            console.log(error);

            res.status(500)
                .send(
                    "Error loading task"
                );

        }

    }
);


// ===============================
// UPDATE TASK
// ===============================

app.post(
    "/tasks/:id/edit",
    async (req, res) => {

        try {

            const id =
                req.params.id;


            if (
                !ObjectId.isValid(id)
            ) {

                return res
                    .status(400)
                    .send(
                        "Invalid task ID"
                    );

            }


            const title =
                req.body.title;

            const description =
                req.body.description;


            if (
                !title ||
                title.trim() === ""
            ) {

                return res
                    .status(400)
                    .send(
                        "Task title is required"
                    );

            }


            await tasksCollection
                .updateOne(

                    {
                        _id:
                            new ObjectId(id)
                    },

                    {
                        $set: {

                            title:
                                title.trim(),

                            description:
                                description
                                    ? description.trim()
                                    : "",

                            isUrgent:
                                req.body.isUrgent === "on",

                            isImportant:
                                req.body.isImportant === "on",

                            priority:
                                req.body.priority ||
                                "Medium",

                            dueDate:
                                req.body.dueDate
                                    ? new Date(
                                        req.body.dueDate
                                    )
                                    : null

                        }
                    }
                );


            res.redirect("/");


        } catch (error) {

            console.log(error);

            res.status(500)
                .send(
                    "Error updating task"
                );

        }

    }
);


// ===============================
// DELETE TASK
// ===============================

app.post(
    "/tasks/:id/delete",
    async (req, res) => {

        try {

            const id =
                req.params.id;


            if (
                !ObjectId.isValid(id)
            ) {

                return res
                    .status(400)
                    .send(
                        "Invalid task ID"
                    );

            }


            await tasksCollection
                .deleteOne({

                    _id:
                        new ObjectId(id)

                });


            res.redirect("/");


        } catch (error) {

            console.log(error);

            res.status(500)
                .send(
                    "Error deleting task"
                );

        }

    }
);


// ===============================
// COMPLETE / INCOMPLETE
// ===============================

app.post(
    "/tasks/:id/toggle",
    async (req, res) => {

        try {

            const id =
                req.params.id;


            if (
                !ObjectId.isValid(id)
            ) {

                return res
                    .status(400)
                    .send(
                        "Invalid task ID"
                    );

            }


            const task =
                await tasksCollection
                    .findOne({

                        _id:
                            new ObjectId(id)

                    });


            if (!task) {

                return res
                    .status(404)
                    .send(
                        "Task not found"
                    );

            }


            await tasksCollection
                .updateOne(

                    {
                        _id:
                            new ObjectId(id)
                    },

                    {
                        $set: {

                            completed:
                                !task.completed

                        }
                    }

                );


            res.redirect("/");


        } catch (error) {

            console.log(error);

            res.status(500)
                .send(
                    "Error changing task status"
                );

        }

    }
);


// ===============================
// CLEAR COMPLETED TASKS
// ===============================

app.post(
    "/tasks/clear-completed",
    async (req, res) => {

        try {

            await tasksCollection
                .deleteMany({

                    completed: true

                });


            res.redirect("/");


        } catch (error) {

            console.log(error);

            res.status(500)
                .send(
                    "Error clearing completed tasks"
                );

        }

    }
);


// ===============================
// REDIRECT /tasks
// ===============================

app.get(
    "/tasks",
    (req, res) => {

        res.redirect("/");

    }
);


// ===============================
// START SERVER
// ===============================

async function startServer() {

    try {

        await connectDB();


        app.listen(
            PORT,
            () => {

                console.log(
                    `Server running at http://localhost:${PORT}`
                );

            }
        );


    } catch (error) {

        console.log(
            "Failed to start server:",
            error
        );

    }

}


startServer();