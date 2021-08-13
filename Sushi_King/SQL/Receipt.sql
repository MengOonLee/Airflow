SELECT
Id AS ReceiptKey,
LoyaltyCustomer_ID AS CustomerKey,
Account_ID AS OutletKey,
DateTS AS EventTimestamp,
Name AS BillNo,
TotalPrice_BeforeTax AS EligibleAmountForPoint,
TotalPrice_GrandTotal AS PaidAmount,
Discount AS Discount,
PreviousPoint AS PreviousPoint,
CurrentPoint AS EarnPoint,
CASE
    WHEN RecStatus=0 THEN 'delete'
    WHEN RecStatus=1 THEN 'inactive'
    WHEN RecStatus=2 THEN 'active'
END AS ReceiptRecordStatus,
CASE
    WHEN Status=1 THEN 'active'
    WHEN Status=2 THEN 'refund'
END AS PaymentStatus,
CASE
    WHEN Type=1 THEN 'point of sale'
    WHEN Type=2 THEN 'self create point'
END AS OrderChannel
FROM dbo.SK_LOYALTYTRANSACTION