SELECT DISTINCT T.num AS ConsecutiveNums
FROM (SELECT
    num,
    LAG(num, 1) OVER() AS prev_num,
    LEAD(num, 1) OVER() AS next_num
    FROM Logs
    ) T
WHERE num = T.prev_num AND num = T.next_num;