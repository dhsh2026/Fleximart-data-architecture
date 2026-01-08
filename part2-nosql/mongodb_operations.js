// Insert product
db.products.insertOne({
  product_id: 101,
  name: "Wireless Mouse",
  category: "Electronics",
  price: 799,
  stock: 120
});

// Find products by category
db.products.find({ category: "Electronics" });

// Update stock
db.products.updateOne(
  { product_id: 101 },
  { $set: { stock: 100 } }
);

// Aggregate average price by category
db.products.aggregate([
  { $group: { _id: "$category", avgPrice: { $avg: "$price" } } }
]);
