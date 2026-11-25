// Assignment 2 — Task 7: The same products in MongoDB
// Run with: mongosh products.mongodb.js

use backend_assignment2

db.products.insertMany([
  { name: "Clean Code", category: "Books", price: 499, attributes: { author: "Robert C. Martin", pages: 464 } },
  { name: "Atomic Habits", category: "Books", price: 399, attributes: { author: "James Clear", pages: 320 } },
  { name: "Wireless Mouse", category: "Electronics", price: 799, attributes: { wireless: true, dpi: 1600, discount_pct: 10 } },
  { name: "USB Keyboard", category: "Electronics", price: 999, attributes: { wireless: false, keys: 104 } },
  { name: "Cotton T-Shirt", category: "Clothing", price: 599, attributes: { size: "M", color: "Blue" } }
]);

db.products.find({ category: "Books", "attributes.author": "James Clear" }, { _id: 0, name: 1, "attributes.author": 1 });
db.products.find({ category: "Electronics", "attributes.dpi": { $gte: 1600 } }, { _id: 0, name: 1, "attributes.dpi": 1 });
db.products.find({ category: "Clothing", "attributes.size": "M" }, { _id: 0, name: 1, "attributes.size": 1 });
db.products.find({ "attributes.wireless": true }, { _id: 0, name: 1 });
