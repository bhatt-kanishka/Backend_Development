/**
 * Lecture 15: PBL Activity - E-Commerce System ODM Modeling with Mongoose
 * Demonstrates document modeling for Product, Cart, and Order in MongoDB/Node.js
 */

const mongoose = require('mongoose');

// 1. Product Schema
const productSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, 'Product name is required'],
    trim: true
  },
  category: {
    type: String,
    required: [true, 'Category is required'],
    enum: ['Electronics', 'Audio', 'Accessories', 'Fashion', 'Home']
  },
  price: {
    type: Number,
    required: [true, 'Price is required'],
    min: [0, 'Price must be positive']
  },
  stock: {
    type: Number,
    required: [true, 'Stock quantity is required'],
    min: [0, 'Stock cannot be negative'],
    default: 0
  }
}, { timestamps: true });

// 2. Shopping Cart Schema
const cartItemSchema = new mongoose.Schema({
  product: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Product',
    required: true
  },
  quantity: {
    type: Number,
    required: true,
    min: [1, 'Quantity must be at least 1'],
    default: 1
  }
});

const cartSchema = new mongoose.Schema({
  customerId: {
    type: String,
    required: [true, 'Customer ID is required'],
    unique: true
  },
  items: [cartItemSchema]
}, { timestamps: true });

// 3. Order Schema with Embedded Snapshot of Purchased Items
const orderItemSchema = new mongoose.Schema({
  productId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Product',
    required: true
  },
  name: { type: String, required: true },
  quantity: { type: Number, required: true, min: 1 },
  priceAtPurchase: { type: Number, required: true, min: 0 }
});

const orderSchema = new mongoose.Schema({
  customerId: {
    type: String,
    required: [true, 'Customer ID is required']
  },
  customerEmail: {
    type: String,
    required: [true, 'Customer email is required'],
    match: [/^\S+@\S+\.\S+$/, 'Invalid email address']
  },
  items: [orderItemSchema],
  totalAmount: {
    type: Number,
    required: true,
    min: [0, 'Total amount cannot be negative']
  },
  status: {
    type: String,
    enum: ['PENDING', 'PAID', 'SHIPPED', 'DELIVERED', 'CANCELLED'],
    default: 'PENDING'
  }
}, { timestamps: true });

const Product = mongoose.model('EcomProduct', productSchema);
const Cart = mongoose.model('EcomCart', cartSchema);
const Order = mongoose.model('EcomOrder', orderSchema);

// Demonstration / Self-Test
async function runEcommerceTest() {
  console.log('='.repeat(70));
  console.log('PBL ACTIVITY: MONGOOSE E-COMMERCE DOCUMENT VALIDATION TEST');
  console.log('='.repeat(70));

  // Valid Product
  const prod = new Product({
    name: 'Sony WH-1000XM5 Headphones',
    category: 'Audio',
    price: 349.99,
    stock: 15
  });

  try {
    await prod.validate();
    console.log('[PASS] Valid Product passed Mongoose schema validation!');
    console.log('  Product:', prod.name, `($${prod.price})`);
  } catch (err) {
    console.error('[FAIL]', err);
  }

  // Valid Order
  const order = new Order({
    customerId: 'CUST-1001',
    customerEmail: 'customer@example.com',
    items: [
      {
        productId: new mongoose.Types.ObjectId(),
        name: 'Sony WH-1000XM5 Headphones',
        quantity: 1,
        priceAtPurchase: 349.99
      }
    ],
    totalAmount: 349.99,
    status: 'PAID'
  });

  try {
    await order.validate();
    console.log('[PASS] Valid Order document passed schema validation!');
    console.log('  Order Customer:', order.customerEmail, '| Status:', order.status, '| Total:', `$${order.totalAmount}`);
  } catch (err) {
    console.error('[FAIL]', err);
  }

  // Invalid Product (negative price & negative stock)
  const badProd = new Product({
    name: 'Faulty Product',
    category: 'Audio',
    price: -50,
    stock: -5
  });

  try {
    await badProd.validate();
    console.error('[FAIL] Bad product unexpectedly passed!');
  } catch (err) {
    console.log('[PASS] Successfully rejected invalid product with negative values:');
    for (const [key, val] of Object.entries(err.errors)) {
      console.log(`  * ${key}: ${val.message}`);
    }
  }

  console.log('='.repeat(70));
}

module.exports = { Product, Cart, Order };

if (require.main === module) {
  runEcommerceTest();
}
