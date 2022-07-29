SELECT  ContactName, Address, City
from northwind.customers
where Country not in ('Germany','Mexico','Spain')