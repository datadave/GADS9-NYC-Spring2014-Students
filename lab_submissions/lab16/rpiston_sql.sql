--What customers are from the UK?
SELECT CustomerName 
FROM Customers
WHERE Country = "UK";

--What is the name of the customer who has the most orders?
SELECT CustomerName, COUNT(*) AS 'Count' FROM Customers
INNER JOIN Orders on (Orders.CustomerID = Customers.CustomerID)
GROUP BY CustomerName
ORDER BY Count DESC
LIMIT 1;

--What supplier has the highest average product price?
SELECT SupplierName, AVG(Products.Price) FROM Suppliers
INNER JOIN Products ON (Suppliers.SupplierID = Products.SupplierID)
GROUP BY SupplierName;

--What category has the most orders?
SELECT CategoryName, COUNT(*) as 'Count' FROM Categories
INNER JOIN Products on (Products.CategoryID = Categories.CategoryID)
INNER JOIN OrderDetails on (OrderDetails.ProductID = Products.ProductID)
GROUP BY CategoryName
ORDER BY Count DESC

--What employee made the most sales (by number of sales)?
SELECT LastName, FirstName, COUNT(*) as 'Count' FROM Employees
INNER JOIN Orders on (Orders.EmployeeID = Employees.EmployeeID)
GROUP BY FirstName
ORDER BY Count DESC

--What employee made the most sales (by value of sales)?
SELECT FirstName, LastName, SUM(OrderDetails.Quantity * Products.Price) as 'Sales' FROM Employees
INNER JOIN Orders on (Orders.EmployeeID = Employees.EmployeeID)
INNER JOIN OrderDetails on (OrderDetails.OrderID = Orders.OrderID)
INNER JOIN Products on (Products.ProductID = OrderDetails.ProductID)
GROUP BY FirstName
ORDER BY Sales DESC

--What Employees have BS degrees? (Hint: Look at LIKE operator)
SELECT * FROM Employees
WHERE Notes LIKE '%BS%'

--What supplier has the highest average product price *assuming they have at least 2 products* (Hint: Look at the HAVING operator)
SELECT SupplierName, AVG(Products.Price) as 'AveragePrice' FROM Suppliers
INNER JOIN Products ON (Products.SupplierID = Suppliers.SupplierID)
GROUP BY SupplierName
HAVING COUNT(*) > 1
ORDER BY AveragePrice DESC
