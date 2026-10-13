SELECT T.customer_number
FROM (
    SELECT customer_number, COUNT(order_number) OVER(PARTITION BY customer_number) AS total_order 
    FROM Orders
    ) T
ORDER BY T.total_order DESC
LIMIT 1;