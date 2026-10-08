SELECT T.id, sum(T.num) as num 
FROM
    (SELECT requester_id AS id, COUNT(distinct accepter_id) as num
    FROM RequestAccepted
    GROUP BY requester_id

    union all

    SELECT accepter_id AS id, COUNT(distinct requester_id) as num
    FROM RequestAccepted
    GROUP BY accepter_id) T

GROUP BY T.id
ORDER BY num DESC
LIMIT 1;