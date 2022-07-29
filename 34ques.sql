SELECT CustomerID, sum(Freight) TotalFreight
	FROM Orders
	GROUP BY CustomerID
	HAVING sum(Freight) > 200; 