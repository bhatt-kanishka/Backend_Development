/**
 * Lecture 15: PBL Activity - E-Commerce Mongoose ODM
 */

const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
  name: { type: String, required: [true, 'Product name is required'], trim: true },
  category: { type: String, required: true, enum: ['Electronics', 'Audio', 'Accessories', 'Fashion', 'Home'] },
  price: { type: Number, required: true, min: [0, 'Price must be positive'] },
  stock: { type: Number, required: true, min: [0, 'Stock cannot be negative'], default: 0 }
}, { timestamps: true });

const cartItemSchema = new mongoose.Schema({
  product: { type: mongoose.Schema.Types.ObjectId, ref: 'Product', required: true },
  quantity: { type: Number, required: true, min: 1, default: 1 }
});

const cartSchema = new mongoose.Schema({
  customerId: { type: String, required: true, unique: true },
  items: [cartItemSchema]
}, { timestamps: true });

const orderItemSchema = new mongoose.Schema({
  productId: { type: mongoose.Schema.Types.ObjectId, ref: 'Product', required: true },
  name: { type: String, required: true },
  quantity: { type: Number, required: true, min: 1 },
  priceAtPurchase: { type: Number, required: true, min: 0 }
});

const orderSchema = new mongoose.Schema({
  customerId: { type: String, required: true },
  customerEmail: { type: String, required: true, match: [/^\S+@\S+\.\S+$/, 'Invalid email address'] },
  items: [orderItemSchema],
  totalAmount: { type: Number, required: true, min: 0 },
  status: { type: String, enum: ['PENDING', 'PAID', 'SHIPPED', 'DELIVERED', 'CANCELLED'], default: 'PENDING' }
}, { timestamps: true });

const Product = mongoose.model('EcomProduct', productSchema);
const Cart = mongoose.model('EcomCart', cartSchema);
const Order = mongoose.model('EcomOrder', orderSchema);

async function runEcommerceValidation() {
  const prod = new Product({
    name: 'Sony WH-1000XM5 Headphones',
    category: 'Audio',
    price: 349.99,
    stock: 15
  });
  await prod.validate();
  console.log(`Validated e-commerce product '${prod.name}' ($${prod.price}) successfully.`);

  const order = new Order({
    customerId: 'CUST-1001',
    customerEmail: 'customer@example.com',
    items: [{
      productId: new mongoose.Types.ObjectId(),
      name: 'Sony WH-1000XM5 Headphones',
      quantity: 1,
      priceAtPurchase: 349.99
    }],
    totalAmount: 349.99,
    status: 'PAID'
  });
  await order.validate();
  console.log(`Validated e-commerce order for ${order.customerEmail} ($${order.totalAmount}) successfully.`);

  const badProd = new Product({
    name: 'Faulty Item',
    category: 'Audio',
    price: -10,
    stock: -5
  });
  try {
    await badProd.validate();
  } catch (err) {
    console.log("Caught invalid product constraints (negative price/stock) successfully:");
    for (const [key, val] of Object.entries(err.errors)) {
      console.log(`  - ${key}: ${val.message}`);
    }
  }
}

module.exports = { Product, Cart, Order };

if (require.main === module) {
  runEcommerceValidation();
}
