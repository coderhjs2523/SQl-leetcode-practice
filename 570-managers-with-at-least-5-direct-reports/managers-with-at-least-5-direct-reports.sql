-- SELECT E1.name
-- FROM Employee E1
-- LEFT JOIN Employee E2 ON E2.managerId = E1.id
-- GROUP BY E2.managerId
-- HAVING count(E2.managerId)>=5;

SELECT E1.name
FROM Employee E1
LEFT JOIN Employee E2 ON E1.id = E2.managerId
GROUP BY E1.id
HAVING COUNT(E1.id) >= 5;