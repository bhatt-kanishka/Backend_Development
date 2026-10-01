/**
 * Lecture 15: Object Document Modeling (ODM) & Validation with Mongoose (Node.js)
 * Covers:
 *   - Section 4.2: Mongoose Basics & Student Schema
 *   - Section 5.2: Built-in Mongoose Validations (required, regex, enum, min/max)
 *   - Lab Exercise 4 & 5: Blog Application (Post & Comment Models with Validation)
 */

const mongoose = require('mongoose');

// ==============================================================================
// 1. Student Schema with Comprehensive Validations (Sections 4.2 & 5.2)
// ==============================================================================

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
      message: '{VALUE} is not a valid engineering branch'
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
  timestamps: true // Best practice from Section 6: adds createdAt and updatedAt
});

const Student = mongoose.model('Student', studentSchema);


// ==============================================================================
// 2. Blog Application: Post & Comment Models (Lab Exercise Tasks 4 & 5)
// ==============================================================================

// Subdocument Schema for Comments
const commentSchema = new mongoose.Schema({
  author: {
    type: String,
    required: [true, 'Comment author is required'],
    trim: true
  },
  content: {
    type: String,
    required: [true, 'Comment content cannot be empty'],
    minlength: [2, 'Comment must have at least 2 characters'],
    maxlength: [500, 'Comment cannot exceed 500 characters']
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

// Main Blog Post Schema
const postSchema = new mongoose.Schema({
  title: {
    type: String,
    required: [true, 'Post title is required'],
    trim: true,
    minlength: [3, 'Title must be at least 3 characters'],
    maxlength: [200, 'Title cannot exceed 200 characters']
  },
  slug: {
    type: String,
    lowercase: true,
    trim: true
  },
  content: {
    type: String,
    required: [true, 'Post content is required']
  },
  author: {
    type: String,
    required: [true, 'Author is required'],
    trim: true
  },
  category: {
    type: String,
    required: [true, 'Category is required'],
    enum: {
      values: ['Backend', 'Database', 'Cloud', 'Architecture', 'Tutorial'],
      message: '{VALUE} is not an accepted category'
    }
  },
  status: {
    type: String,
    enum: {
      values: ['draft', 'published', 'archived'],
      message: 'Status must be either draft, published, or archived'
    },
    default: 'draft'
  },
  tags: [{
    type: String,
    lowercase: true,
    trim: true
  }],
  comments: [commentSchema] // Embedded subdocuments
}, {
  timestamps: true // Data modeling best practice
});

const Post = mongoose.model('Post', postSchema);
const Comment = mongoose.model('Comment', commentSchema);


// ==============================================================================
// 3. Validation Test Suite (Runs offline via Mongoose Schema Validator)
// ==============================================================================

async function runMongooseValidationTests() {
  console.log('='.repeat(70));
  console.log('LECTURE 15: MONGOOSE DATA MODELING & VALIDATION TEST SUITE');
  console.log('='.repeat(70));

  // ----------------------------------------------------------------------------
  // Test 1: Valid Student Document
  // ----------------------------------------------------------------------------
  console.log('\n[TEST 1] Testing VALID Student Document:');
  const validStudent = new Student({
    name: 'Aarav Sharma',
    email: 'aarav@upes.ac.in',
    branch: 'CSE',
    age: 20
  });

  try {
    await validStudent.validate();
    console.log('[PASS] Valid Student passed all schema validations successfully!');
    console.log('  Document:', JSON.stringify(validStudent.toObject(), null, 2));
  } catch (err) {
    console.error('[FAIL] Unexpected validation error:', err.errors);
  }

  // ----------------------------------------------------------------------------
  // Test 2: Invalid Student Document (Testing Validation Rules)
  // ----------------------------------------------------------------------------
  console.log('\n' + '-'.repeat(70));
  console.log('[TEST 2] Testing INVALID Student Document (Catching Constraints):');
  const invalidStudent = new Student({
    name: '',                       // Fails: required & minlength: 1
    email: 'not-an-email',          // Fails: match regex /^\S+@\S+\.\S+$/
    branch: 'CIVIL',                // Fails: enum ['CSE', 'ECE', 'IT', 'ME', 'CE']
    age: 15                         // Fails: min: 17
  });

  try {
    await invalidStudent.validate();
    console.error('[FAIL] Invalid student unexpectedly passed validation!');
  } catch (studentErr) {
    console.log('[PASS] Mongoose correctly intercepted and rejected invalid data:');
    for (const [field, error] of Object.entries(studentErr.errors)) {
      console.log(`  * Field [${field}]: ${error.message} (Kind: ${error.kind})`);
    }
  }

  // ----------------------------------------------------------------------------
  // Test 3: Valid Blog Post with Embedded Comments (Lab Exercise 4 & 5)
  // ----------------------------------------------------------------------------
  console.log('\n' + '-'.repeat(70));
  console.log('[TEST 3] Testing VALID Blog Post with Embedded Comments:');
  const validPost = new Post({
    title: 'Mastering Database Modeling with Mongoose & SQLAlchemy',
    slug: 'mastering-database-modeling',
    content: 'Data modeling defines how software structures, persists, and validates business state.',
    author: 'Kanishka Bhatt',
    category: 'Backend',
    status: 'published',
    tags: ['mongodb', 'mongoose', 'orm', 'nodejs'],
    comments: [
      {
        author: 'Rohan',
        content: 'Clear explanation of conceptual vs logical models!'
      }
    ]
  });

  try {
    await validPost.validate();
    console.log('[PASS] Valid Blog Post and embedded comments passed validation!');
    console.log('  Post Title:', validPost.title);
    console.log('  Category:', validPost.category);
    console.log('  Status:', validPost.status);
    console.log('  Comments count:', validPost.comments.length);
  } catch (err) {
    console.error('[FAIL] Unexpected error on valid post:', err.errors);
  }

  // ----------------------------------------------------------------------------
  // Test 4: Invalid Blog Post (Testing enum and required rules)
  // ----------------------------------------------------------------------------
  console.log('\n' + '-'.repeat(70));
  console.log('[TEST 4] Testing INVALID Blog Post:');
  const invalidPost = new Post({
    title: 'AB',                     // Fails: minlength 3
    content: '',                     // Fails: required
    author: '',                      // Fails: required
    category: 'InvalidCategory',     // Fails: enum
    status: 'pending_approval'       // Fails: enum
  });

  try {
    await invalidPost.validate();
    console.error('[FAIL] Invalid post unexpectedly passed validation!');
  } catch (postErr) {
    console.log('[PASS] Mongoose correctly caught invalid blog post fields:');
    for (const [field, error] of Object.entries(postErr.errors)) {
      console.log(`  * Field [${field}]: ${error.message}`);
    }
  }

  console.log('\n' + '='.repeat(70));
  console.log('ALL MONGOOSE ODM & VALIDATION TESTS COMPLETED SUCCESSFULLY!');
  console.log('='.repeat(70));
}

// Export models and schemas for modular use
module.exports = {
  Student,
  studentSchema,
  Post,
  postSchema,
  Comment,
  commentSchema
};

if (require.main === module) {
  runMongooseValidationTests();
}
