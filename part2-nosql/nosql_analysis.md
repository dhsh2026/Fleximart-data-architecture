## Why NoSQL for Fleximart

Fleximart deals with semi-structured product and catalog data such as varying attributes,
categories, discounts, and supplier-specific metadata. A document-based NoSQL database
like MongoDB is suitable because:

- Flexible schema for changing product attributes
- Faster reads for catalog browsing
- Horizontal scalability for high traffic
- Nested documents reduce joins

## Use Case

Product catalog management where each product can have different attributes
(e.g., electronics vs groceries).

## Comparison with Relational Database

| Feature | Relational DB | MongoDB |
|------|------|------|
| Schema | Fixed | Flexible |
| Joins | Expensive | Embedded docs |
| Scalability | Vertical | Horizontal |
| Use Case | Transactions | Catalogs & logs |
