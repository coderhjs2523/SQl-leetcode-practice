-- WITH CTE_TOP_OREDER_CUSTOMER AS (
--     SELECT customer_number, 
--     COUNT(DISTINCT order_number) AS total_order
--     FROM Orders
--     GROUP BY customer_number
--     ORDER BY total_order DESC
--     LIMIT 1
--     )

-- SELECT customer_number FROM CTE_TOP_OREDER_CUSTOMER;

SELECT T.customer_number AS customer_number
FROM(
    SELECT 
    customer_number,
    COUNT(order_number) OVER(PARTITION BY customer_number) AS total_order
    FROM Orders
    ) T
ORDER BY T.total_order DESC
LIMIT 1;