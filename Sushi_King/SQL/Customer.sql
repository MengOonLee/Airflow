SELECT TOP 10
Id AS CustomerKey,
Name As CustomerName,
IC AS CustomerIdentityCard,
CASE
    WHEN Salutation IN ('MS', 'MRS') THEN 'female'
    WHEN Salutation IN ('MR') THEN 'male'
    ELSE 'unknown'
END AS CustomerGender,
CASE
    WHEN DOB IN ('19000101', '1900-01-01') THEN NULL
    ELSE YEAR(LastTransTS) - YEAR(DOB)
END AS CustomerAge,
CASE
    WHEN DOB IN ('19000101', '1900-01-01') THEN NULL
    ELSE DOB
END AS CustomerBirthdate,
Email As CustomerEmail,
Mobile AS CustomerMobile,
State AS CustomerState,
CASE
    WHEN Occupation=1 THEN 'executive'
    WHEN Occupation=2 THEN 'non-executive'
    WHEN Occupation=3 THEN 'managerial'
    WHEN Occupation=4 THEN 'professional'
    WHEN Occupation=5 THEN 'self-employed'
    WHEN Occupation=6 THEN 'student'
    WHEN Occupation=99 THEN 'others'
    ELSE 'unknown'
END AS CustomerOccupation,
MemberId AS CustomerMemberId,
CASE 
    WHEN MemberType=1 THEN 'app'
    WHEN MemberType=2 THEN 'card'
    ELSE 'unknown'
END AS CustomerMemberType,
CreatedTS AS CustomerRegisteredTimestamp,
CASE
    WHEN Status=1 THEN 'pending verification'
    WHEN Status=2 THEN 'active'
    WHEN Status=3 THEN 'suspend'
END AS CustomerMemberStatus,
Point AS CustomerMemberPoint,
CASE
    WHEN PreferredFestival=1 THEN 'Hari Raya Aidilfitri'
    WHEN PreferredFestival=2 THEN 'Chinese New Year'
    WHEN PreferredFestival=4 THEN 'Deepavali'
    ELSE 'Others'
END AS CustomerPreferredFestival,
LastTransDay AS CustomerRecency,
TransCnt AS CustomerFrequency,
GrandTotal AS CustomerMonetaryValue,
LastTransTS AS CustomerLatestTransaction
FROM dbo.SK_LOYALTYCUSTOMER