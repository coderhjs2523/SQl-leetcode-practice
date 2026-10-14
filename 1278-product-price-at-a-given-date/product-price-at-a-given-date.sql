SELECT product_id, 10 AS price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16'

UNION

SELECT T.product_id AS product_id, T.new_price AS price
FROM (
    SELECT 
    product_id, 
    new_price, 
    ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS row_num 
    FROM Products 
    WHERE change_date <= '2019-08-16'
    ) T
GROUP BY T.product_id;