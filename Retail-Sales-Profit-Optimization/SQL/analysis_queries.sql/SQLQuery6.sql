

SELECT [State],
       SUM([Sales]) AS Total_Sales,
       SUM([Profit]) AS Total_Profit
FROM dbo.superstore_clean
GROUP BY [State]
ORDER BY Total_Sales DESC;