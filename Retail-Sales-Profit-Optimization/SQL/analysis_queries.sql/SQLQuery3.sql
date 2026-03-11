SELECT [Sub_Category],
       SUM([Sales]) AS Total_Sales,
       SUM([Profit]) AS Total_Profit
FROM dbo.superstore_clean
GROUP BY [Sub_Category]
ORDER BY Total_Profit ASC;