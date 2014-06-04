--What customers are from the UK?

SELECT *
FROM Customers
WHERE Country='UK'
;

--What is the name of the customer who has the most orders?

SELECT Orders.CustomerID, COUNT(*) AS 'Total_Count', Customers.CustomerName
FROM Orders
INNER JOIN Customers on (Orders.CustomerID = Customers.CustomerID)
GROUP BY Orders.CustomerID
ORDER BY Total_Count DESC
;

--What supplier has the highest average product price?

SELECT Products.SupplierID, COUNT(*) AS 'Count', AVG(Products.Price) AS 'Avg_Price', Suppliers.SupplierName
FROM Products
INNER JOIN Suppliers on (Products.SupplierID = Suppliers.SupplierID)
GROUP BY Products.SupplierID
ORDER BY Avg_Price DESC
;

--What category has the most orders?

SELECT Products.CategoryID, COUNT(*) AS 'Total_Orders', Categories.CategoryName
FROM OrderDetails
INNER JOIN Products on (OrderDetails.ProductID = Products.ProductID)
INNER JOIN Categories on (Products.CategoryID = Categories.CategoryID)
GROUP BY Products.CategoryID
ORDER BY Total_Orders DESC
;

--What employee made the most sales (by number of sales)?

SELECT Orders.EmployeeID, COUNT(*) AS 'Total_Sales', Employees.FirstName, Employees.LastName
FROM Orders
INNER JOIN Employees on (Orders.EmployeeID = Employees.EmployeeID)
GROUP BY Orders.EmployeeID
ORDER BY Total_Sales DESC
;

--What employee made the most sales (by value of sales)?

SELECT Orders.EmployeeID, SUM(Products.Price*OrderDetails.Quantity) AS 'TotalSales', Employees.FirstName, Employees.LastName
FROM OrderDetails
INNER JOIN Orders on (OrderDetails.OrderID = Orders.OrderID)
INNER JOIN Employees on (Orders.EmployeeID = Employees.EmployeeID)
INNER JOIN Products on (OrderDetails.ProductID = Products.ProductID)
GROUP BY Orders.EmployeeID
ORDER BY TotalSales DESC
;

--What Employees have BS degrees? (Hint: Look at LIKE operator)

SELECT FirstName, LastName, Notes
FROM Employees
WHERE Notes LIKE '%BS%'
;

--What supplier has the highest average product price *assuming they have at least 2 products* (Hint: Look at the HAVING operator)

SELECT Products.SupplierID, COUNT(*) AS 'Count', AVG(Products.Price) AS 'Avg_Price', Suppliers.SupplierName
FROM Products
INNER JOIN Suppliers on (Products.SupplierID = Suppliers.SupplierID)
GROUP BY Products.SupplierID
HAVING COUNT(Products.SupplierID) > 1
ORDER BY Avg_Price DESC
;
