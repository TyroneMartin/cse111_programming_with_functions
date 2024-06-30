-- REMINDER: SQL is declarative programming. We declare what we want and the
-- application determines how to complete that task.

-- Author: Brother Keers
-- Copyright 2023 Brigham Young University Idaho.

-- This is SQLs equivalent to our python filter_data.py demo.
SELECT * FROM Customers
WHERE Country = 'USA' OR Country = "CAN"
ORDER BY Country ASC, Name ASC;

-- In SQL this could all be on one line.
SELECT * FROM Customers WHERE Country = 'USA' OR Country = "CAN" ORDER BY Country ASC, Name ASC;

-- You could also use this query in SQL which replaces the OR with IN.
SELECT * FROM customers
WHERE Country IN ('USA', 'CAN')
ORDER BY Country ASC, Name ASC;

-- In SQL this could all be on one line.
SELECT * FROM customers WHERE Country IN ('USA', 'CAN') ORDER BY Country ASC, Name ASC;


-- This is SQLs equivalent to our python map_data.py demo.

-- Get all customers names.
SELECT Name FROM Customers;

-- Get all customers names sorted in ascending (alphabetical) order.
SELECT Name FROM Customers ORDER BY Name ASC;

-- Get all customers names sorted in descending (reverse alphabetical) order.
SELECT Name FROM Customers ORDER BY Name DESC;