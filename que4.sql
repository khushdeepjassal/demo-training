SELECT OrderID, OrderDate, ShippedDate, CustomerID, Freight
from northwind.orders
order by Freight desc
limit 10;