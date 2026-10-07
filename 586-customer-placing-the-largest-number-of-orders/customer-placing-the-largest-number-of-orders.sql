-- SELECT customer_number
-- FROM Orders
-- GROUP BY customer_number
-- ORDER BY COUNT(order_number) DESC
-- LIMIT 1;

SELECT customer_number 
FROM (
    SELECT customer_number, COUNT(order_number) AS T 
    FROM Orders 
    GROUP BY customer_number
) AS sub 
ORDER BY T DESC 
LIMIT 1;