SELECT
T.person_name as person_name
FROM
    (SELECT 
    person_name,
    SUM(weight) OVER(ORDER BY turn) AS toatl_weight
    FROM Queue
    ) T
WHERE T.toatl_weight <= 1000
ORDER BY T.toatl_weight DESC
LIMIT 1