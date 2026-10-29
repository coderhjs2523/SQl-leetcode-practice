SELECT
T.product_id AS product_id, 
T.year AS first_year, 
T.quantity AS quantity,  
T.price AS price
FROM
    (
    SELECT
    product_id, 
    year, 
    quantity,  
    price,
    DENSE_RANK() OVER(PARTITION BY product_id ORDER BY year) AS rnk
    FROM Sales
    ) T
WHERE T.rnk = 1;