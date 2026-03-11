
SELECT [Year_Month],
       SUM([Sales]) AS Monthly_Sales,
       SUM([Profit]) AS Monthly_Profit
FROM dbo.superstore_clean
GROUP BY [Year_Month]
ORDER BY [Year_Month];