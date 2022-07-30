SELECT CompanyName,ContactName,Fax
	FROM Customers
	WHERE Fax IS NULL AND Country = 'USA'
	ORDER BY ContactName;