SELECT R.contest_id, ROUND(
    COUNT(DISTINCT U.user_id)/ (SELECT COUNT(user_id) FROM Users) * 100
    ,2) AS percentage
FROM Users U
JOIN Register R ON U.user_id = R.user_id
GROUP BY R.contest_id
ORDER BY percentage DESC, contest_id ASC ;