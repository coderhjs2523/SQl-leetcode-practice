-- WITH CTE_RANK AS(
--     SELECT num
--     FROM MyNumbers
--     GROUP BY num
--     HAVING COUNT(num) = 1
--     )

-- SELECT MAX(num) AS num
-- FROM CTE_RANK;

SELECT MAX(T.num) AS num
FROM
(
    SELECT 
    num,
    COUNT(num) OVER(PARTITION BY num) as total_count
    FROM MyNumbers
    ORDER BY total_count
) T
WHERE T.total_count = 1;