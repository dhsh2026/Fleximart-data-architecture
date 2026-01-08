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
## Section A: Limitations of Relational Databases (RDBMS)

Relational databases like MySQL use fixed schemas, which makes them less suitable for handling highly diverse product catalogs. In FlexiMart’s case, different product categories such as electronics, clothing, and groceries have completely different attributes. Representing these variations in an RDBMS requires multiple nullable columns or additional tables, increasing complexity.

Frequent schema changes are another limitation. Adding new product attributes requires ALTER TABLE operations, which can be time-consuming and risky in production systems. This reduces agility when new product types are introduced.

Storing customer reviews is also inefficient in relational databases. Reviews require separate tables and multiple joins to fetch product data along with reviews, increasing query complexity and impacting performance, especially at scale.

---

## Section B: Benefits of MongoDB for Product Catalog

MongoDB uses a flexible, document-based schema that allows each product to store its own attributes without enforcing a rigid structure. This makes it ideal for FlexiMart’s diverse product catalog, where electronics may include specifications like RAM and storage, while apparel includes size and color.

MongoDB supports embedded documents, allowing customer reviews to be stored directly inside product documents. This improves read performance and simplifies data retrieval for catalog browsing.

Additionally, MongoDB offers horizontal scalability through sharding, making it well-suited for handling high traffic and large volumes of semi-structured data common in e-commerce platforms.

---

## Section C: Trade-offs of Using MongoDB

One disadvantage of MongoDB is weaker support for complex transactions compared to relational databases. While MongoDB supports transactions, they are less mature and efficient for highly relational operations.

Another drawback is data redundancy. Embedding documents can lead to duplicated data, increasing storage requirements and making updates more complex if the same data exists in multiple documents.
