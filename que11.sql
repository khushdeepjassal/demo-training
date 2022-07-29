SELECT FirstName, LastName, Country
FROM northwind.employees
where Country not in ('USA')