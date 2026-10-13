SELECT T.person_name AS person_name
FROM (
    SELECT person_name, 
    SUM(weight) OVER(ORDER BY turn) AS total_weight 
    FROM Queue
    ) T
WHERE T.total_weight <= 1000
ORDER BY T.total_weight DESC
LIMIT 1;