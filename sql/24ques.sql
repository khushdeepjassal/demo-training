
	SELECT OrderID, count(OrderID) as NumberofItems
	FROM [Order Details]
	GROUP BY OrderID
	ORDER BY NumberofItems DESC ;