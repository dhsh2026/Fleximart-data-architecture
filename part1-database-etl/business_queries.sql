-- Business Query 1: Total revenue by customer
SELECT 
    c.customer_id,
    c.name,
    SUM(o.order_amount) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;

-- Business Query 2: Customers with no orders
SELECT 
    c.customer_id,
    c.name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Business Query 3: Monthly revenue trend
SELECT 
    MONTH(order_date) AS month,
    SUM(order_amount) AS monthly_revenue
FROM orders
GROUP BY MONTH(order_date)
ORDER BY month;
