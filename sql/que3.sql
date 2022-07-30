select upper(FirstName) as FirstName, upper(LastName) as LastName, HireDate
FROM northwind.employees
order by HireDate;