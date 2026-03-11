

SELECT [Discount],
       SUM([Sales]) AS Total_Sales,
       SUM([Profit]) AS Total_Profit,
       AVG([Profit_Margin]) AS Avg_Profit_Margin
FROM dbo.superstore_clean
GROUP BY [Discount]
ORDER BY [Discount];