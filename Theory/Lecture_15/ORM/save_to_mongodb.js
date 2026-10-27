/**
 * Script to insert Lecture 15 data into MongoDB so you can view it in MongoDB Compass.
 * Database name: student_management
 * Collections: students, posts, products
 */

const mongoose = require('mongoose');

// Default local MongoDB connection URI (standard port 27017)
// If you use MongoDB Atlas, replace this URI with your Atlas connection string.
const MONGO_URI = process.env.MONGO_URI || 'mongodb://127.0.0.1:27017/student_management';

// 1. Schemas
const studentSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  branch: { type: String, enum: ['CSE', 'ECE', 'IT', 'ME', 'CE'] },
  age: { type: Number, min: 17, max: 30 },
  enrollmentDate: { type: Date, default: Date.now }
}, { timestamps: true });

const postSchema = new mongoose.Schema({
  title: { type: String, required: true },
  content: { type: String, required: true },
  author: { type: String, required: true },
  category: { type: String, enum: ['Backend', 'Database', 'Cloud', 'Tutorial'] },
  status: { type: String, default: 'published' },
  comments: [{
    author: String,
    content: String,
    createdAt: { type: Date, default: Date.now }
  }]
}, { timestamps: true });

const Student = mongoose.model('CompassStudent', studentSchema, 'students');
const Post = mongoose.model('CompassPost', postSchema, 'posts');

async function main() {
  console.log(`Connecting to MongoDB at ${MONGO_URI}...`);

  try {
    await mongoose.connect(MONGO_URI, {
      serverSelectionTimeoutMS: 3000
    });
    console.log("Connected to MongoDB successfully.");

    // Clean existing sample demo data
    await Student.deleteMany({});
    await Post.deleteMany({});

    // 1. Insert Students
    const students = await Student.insertMany([
      { name: 'Aarav Sharma', email: 'aarav@upes.ac.in', branch: 'CSE', age: 20 },
      { name: 'Priya Patel', email: 'priya@upes.ac.in', branch: 'ECE', age: 21 },
      { name: 'Rohan Verma', email: 'rohan@upes.ac.in', branch: 'IT', age: 19 }
    ]);
    console.log(`Inserted ${students.length} students into 'students' collection successfully.`);

    // 2. Insert Blog Post with Comments
    const post = await Post.create({
      title: 'Lecture 15: Data Modeling with Mongoose & SQLAlchemy',
      content: 'Data models bridge business requirements and database schemas.',
      author: 'Kanishka Bhatt',
      category: 'Backend',
      status: 'published',
      comments: [
        { author: 'Rohan', content: 'Great lecture on conceptual and logical models!' },
        { author: 'Aarav', content: 'Loved the cascade deletion example.' }
      ]
    });
    console.log(`Inserted blog post '${post.title}' into 'posts' collection successfully.`);

    console.log("\nAll data written to MongoDB successfully!");
    console.log("How to view in MongoDB Compass:");
    console.log("1. Open MongoDB Compass on your computer.");
    console.log("2. In the connection string box, paste: mongodb://localhost:27017");
    console.log("3. Click 'Connect'.");
    console.log("4. On the left sidebar, click on 'student_management'.");
    console.log("5. Click on 'students' or 'posts' to view your documents visually.");

  } catch (error) {
    console.log("\nCould not connect to MongoDB on localhost:27017.");
    console.log("Reason: The local MongoDB service (mongod) is not running on your computer.");
    console.log("\nTo start it:");
    console.log("- If MongoDB Community Server is installed, start the service in Windows Services or run 'net start MongoDB'.");
    console.log("- Or if you use MongoDB Atlas (Cloud), pass your connection URI:");
    console.log("  $env:MONGO_URI=\"mongodb+srv://<username>:<password>@cluster.mongodb.net/student_management\"");
    console.log("  node save_to_mongodb.js");
  } finally {
    await mongoose.disconnect();
  }
}

main();
