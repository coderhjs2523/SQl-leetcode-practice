WITH Table_cte AS (
    SELECT *,
           id - ROW_NUMBER() OVER(ORDER BY id) AS diff
    FROM Stadium
    WHERE people >= 100
)
SELECT id, visit_date, people
FROM (
    SELECT *,
           COUNT(*) OVER(PARTITION BY diff) AS row_count
    FROM Table_cte
) T
WHERE row_count >= 3
ORDER BY visit_date;