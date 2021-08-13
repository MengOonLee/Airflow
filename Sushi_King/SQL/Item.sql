SELECT
LoyaltyTransaction_ID AS ReceiptKey,
Name AS ProductName,
PLUID AS ProductID,
Category AS ProductCategoryName,
CategoryId AS ProductCategoryID,
Quantity AS ProductQuantity,
Price AS ProductUnitPrice,
CASE
    WHEN RecStatus=0 THEN 'delete'
    WHEN RecStatus=1 THEN 'inactive'
    WHEN RecStatus=2 THEN 'active'
END AS ProductRecordStatus
FROM dbo.SK_LOYALTYTRANSACTIONITEM