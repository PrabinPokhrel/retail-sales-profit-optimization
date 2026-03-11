
SELECT TOP 10 [Product_Name],
       SUM([Sales]) AS Total_Sales,
       SUM([Profit]) AS Total_Profit
FROM dbo.superstore_clean
GROUP BY [Product_Name]
ORDER BY Total_Profit ASC;