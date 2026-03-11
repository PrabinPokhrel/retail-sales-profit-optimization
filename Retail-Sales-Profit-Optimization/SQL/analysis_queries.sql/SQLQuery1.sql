
SELECT [Region],
       SUM([Sales]) AS Total_Sales,
       SUM([Profit]) AS Total_Profit
FROM dbo.superstore_clean
GROUP BY [Region]
ORDER BY Total_Sales DESC;