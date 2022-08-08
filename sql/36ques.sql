SELECT a.EmployeeID,
	CONCAT (a.LastName, ' ' ,a.FirstName ) AS Employee,
	CONCAT (b.LastName,' ', b.FirstName ) AS Manager
	FROM Employees a
	LEFT JOIN Employees b
	ON b.EmployeeID = a.ReportsTo
	ORDER BY a.EmployeeID;