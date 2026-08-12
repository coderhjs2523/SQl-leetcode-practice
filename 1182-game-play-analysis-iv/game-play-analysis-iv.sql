SELECT ROUND(
    COUNT(DISTINCT A2.player_id) / COUNT(DISTINCT A1.player_id),
    2
) AS fraction
FROM Activity A1
LEFT JOIN Activity A2
    ON A1.player_id = A2.player_id
    AND DATEDIFF(A2.event_date, A1.event_date) = 1
WHERE A1.event_date = (
    SELECT MIN(event_date)
    FROM Activity A3
    WHERE A3.player_id = A1.player_id
);