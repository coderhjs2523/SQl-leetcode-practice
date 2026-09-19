SELECT E2.unique_id, E1.name
FROM Employees E1
LEFT JOIN EmployeeUNI E2 ON E1.id = E2.id;