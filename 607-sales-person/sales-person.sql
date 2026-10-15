SELECT S.name
FROM SalesPerson S
WHERE S.sales_id not in (SELECT O.sales_id
FROM Orders O
JOIN Company C ON O.com_id = C.com_id AND C.name = 'RED')