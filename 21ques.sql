SELECT City, CompanyName, ContactName
	FROM
	Customers
	WHERE City like '%l%' 
	ORDER BY ContactName;
