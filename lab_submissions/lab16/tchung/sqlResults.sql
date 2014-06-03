--What customers are from the UK?
SELECT count(*) from Customers
where Country = 'UK';
--Answer: 7

--What is the name of the customer who has the most orders?
SELECT CustomerName, Count(*) as count FROM Orders
LEFT JOIN Customers WHERE Customers.CustomerID = Orders.CustomerID
GROUP BY CustomerName
ORDER BY count DESC;
--Answer: Ernst Handel at 10

--What supplier has the highest average product price?
SELECT avg(Price) as avgPrice, count(Price) as count, SupplierName FROM Products
LEFT JOIN Suppliers ON (Suppliers.SupplierID = Products.SupplierID)
GROUP BY SupplierName
ORDER BY avgPrice DESC;
--Answer: Aux joyeux ecclésiastiques at 140.75

--What category has the most orders?
SELECT count(*) as 'count', CategoryName FROM OrderDetails
LEFT JOIN Products ON (Products.ProductID = OrderDetails.ProductID)
LEFT JOIN Categories ON (Categories.CategoryID = Products.CategoryID)
GROUP BY CategoryName
ORDER BY count DESC;
--Answer: Dairy Products, at 100

--What employee made the most sales (by number of sales)?
SELECT sum(Quantity) as quantity, LastName, FirstName FROM Orders
LEFT JOIN OrderDetails on (OrderDetails.OrderID = Orders.OrderID)
LEFT JOIN Employees on (Orders.EmployeeID = Employees.EmployeeID)
GROUP BY LastName, FirstName
ORDER BY quantity DESC;
--Answer: Margaret Peacock, at 3232

--What employee made the most sales (by value of sales)?
SELECT sum(Quantity*Price) as quantity, LastName, FirstName FROM Orders
LEFT JOIN OrderDetails on (OrderDetails.OrderID = Orders.OrderID)
LEFT JOIN Employees on (Orders.EmployeeID = Employees.EmployeeID)
LEFT JOIN Products on (Products.ProductID = OrderDetails.ProductID)
GROUP BY LastName, FirstName
ORDER BY quantity DESC;
--Answer: Margaret Peacock, at 105696.5

--What Employees have BS degrees? (Hint: Look at LIKE operator)
select LastName, FirstName from Employees
where (Notes like '%BS%')
--Answer: Janet Leverling and Steven Buchanan

--What supplier has the highest average product price assuming they have at least 2 products (Hint: Look at the HAVING operator)
SELECT avg(Price) as avgPrice, count(Price) as count, SupplierName FROM Products
LEFT JOIN Suppliers ON (Suppliers.SupplierID = Products.SupplierID)
GROUP BY SupplierName
HAVING count(Price) >= 2
ORDER BY avgPrice DESC;
--Answer: Aux joyeux ecclésiastiques at 140.75

