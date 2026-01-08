# Database Schema Documentation

## Database Name
data_quality_db

## Tables Overview

### customers
| Column Name | Data Type | Description |
|------------|----------|-------------|
| customer_id | INT | Unique identifier for each customer |
| name | VARCHAR | Customer full name |
| email | VARCHAR | Customer email address |
| signup_date | DATE | Date the customer signed up |

### orders
| Column Name | Data Type | Description |
|------------|----------|-------------|
| order_id | INT | Unique identifier for each order |
| customer_id | INT | Linked customer ID |
| order_date | DATE | Date of the order |
| order_amount | DECIMAL | Value of the order |

## Relationships
- `customers.customer_id` → `orders.customer_id` (One-to-Many)
