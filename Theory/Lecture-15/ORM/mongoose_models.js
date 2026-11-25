/**
 * Lecture 15: Mongoose ODM and Schema Validation
 * Student schema & Blog application (Post & Comment)
 */

const mongoose = require('mongoose');

// 1. Student Schema with validations
const studentSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, 'Name is required'],
    trim: true,
    minlength: [1, 'Name cannot be empty'],
    maxlength: [100, 'Name cannot exceed 100 characters']
  },
  email: {
    type: String,
    required: [true, 'Email is required'],
    unique: true,
    lowercase: true,
    trim: true,
    match: [/^\S+@\S+\.\S+$/, 'Invalid email format']
  },
  branch: {
    type: String,
    required: [true, 'Branch is required'],
    enum: {
      values: ['CSE', 'ECE', 'IT', 'ME', 'CE'],
      message: '{VALUE} is not an accepted branch'
    }
  },
  age: {
    type: Number,
    min: [17, 'Minimum age is 17'],
    max: [30, 'Maximum age is 30']
  },
  enrollmentDate: {
    type: Date,
    default: Date.now
  },
  courses: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Course'
  }]
}, {
  timestamps: true
});

const Student = mongoose.model('Student', studentSchema);

// 2. Blog Schemas (Post & Comment)
const commentSchema = new mongoose.Schema({
  author: { type: String, required: [true, 'Author is required'], trim: true },
  content: { type: String, required: [true, 'Comment cannot be empty'], minlength: 2, maxlength: 500 },
  createdAt: { type: Date, default: Date.now }
});

const postSchema = new mongoose.Schema({
  title: { type: String, required: true, minlength: 3, maxlength: 200, trim: true },
  slug: { type: String, lowercase: true, trim: true },
  content: { type: String, required: true },
  author: { type: String, required: true, trim: true },
  category: {
    type: String,
    required: true,
    enum: ['Backend', 'Database', 'Cloud', 'Architecture', 'Tutorial']
  },
  status: {
    type: String,
    enum: ['draft', 'published', 'archived'],
    default: 'draft'
  },
  tags: [{ type: String, lowercase: true, trim: true }],
  comments: [commentSchema]
}, {
  timestamps: true
});

const Post = mongoose.model('Post', postSchema);
const Comment = mongoose.model('Comment', commentSchema);

// Self-validation runner
async function validateSchemas() {
  // Test valid student
  const student = new Student({
    name: 'Aarav Sharma',
    email: 'aarav@upes.ac.in',
    branch: 'CSE',
    age: 20
  });
  await student.validate();
  console.log(`Validated student '${student.name}' schema successfully.`);

  // Test invalid student
  const invalidStudent = new Student({
    name: '',
    email: 'bad-email',
    branch: 'CIVIL',
    age: 15
  });
  try {
    await invalidStudent.validate();
  } catch (err) {
    console.log("Caught invalid student fields via Mongoose schema validation successfully:");
    for (const [key, val] of Object.entries(err.errors)) {
      console.log(`  - ${key}: ${val.message}`);
    }
  }

  // Test valid blog post
  const post = new Post({
    title: 'Data Modeling with Mongoose and SQLAlchemy',
    slug: 'data-modeling-mongoose-sqlalchemy',
    content: 'Data models bridge business requirements and database schemas.',
    author: 'Kanishka Bhatt',
    category: 'Backend',
    status: 'published',
    tags: ['mongodb', 'mongoose', 'nodejs'],
    comments: [{ author: 'Rohan', content: 'Great breakdown of conceptual and logical models!' }]
  });
  await post.validate();
  console.log(`Validated blog post '${post.title}' with ${post.comments.length} comment(s) successfully.`);

  // Test invalid blog post
  const invalidPost = new Post({
    title: 'Hi',
    content: '',
    author: '',
    category: 'InvalidCategory'
  });
  try {
    await invalidPost.validate();
  } catch (err) {
    console.log("Caught invalid blog post fields via Mongoose schema validation successfully:");
    for (const [key, val] of Object.entries(err.errors)) {
      console.log(`  - ${key}: ${val.message}`);
    }
  }
}

module.exports = { Student, Post, Comment };

if (require.main === module) {
  validateSchemas();
}
