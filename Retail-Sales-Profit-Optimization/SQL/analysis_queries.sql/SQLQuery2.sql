

SELECT [Category],
       SUM([Sales]) AS Total_Sales,
       SUM([Profit]) AS Total_Profit
FROM dbo.superstore_clean
GROUP BY [Category]
ORDER BY Total_Profit ASC;