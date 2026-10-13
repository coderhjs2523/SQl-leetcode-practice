SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
           LAG(num, 1) OVER () AS prev_num,
           LEAD(num, 1) OVER () AS next_num
    FROM Logs
) AS t
WHERE num = prev_num AND num = next_num;