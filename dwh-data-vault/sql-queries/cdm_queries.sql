-- Number of Managers per Department
SELECT 
    d.Name AS DepartmentName, 
    COUNT(DISTINCT m.ManagerID) AS ManagerCount
FROM 
    HubDepartment d
JOIN 
    LinkManagerDepartment lmd ON d.DepartmentHashKey = lmd.DepartmentHashKey
JOIN 
    HubManager m ON lmd.ManagerHashKey = m.ManagerHashKey
GROUP BY 
    d.Name;


-- Number of Employees (Managers excluded) per Department
SELECT 
    d.Name AS DepartmentName, 
    COUNT(DISTINCT e.EmployeeID) AS EmployeeCount
FROM 
    HubDepartment d
JOIN 
    LinkCompanyDepartment lcd ON d.DepartmentHashKey = lcd.DepartmentHashKey
JOIN 
    HubCompany c ON lcd.CompanyHashKey = c.CompanyHashKey
JOIN 
    LinkPersonCompany lpc ON c.CompanyHashKey = lpc.CompanyHashKey
JOIN 
    HubPerson p ON lpc.PersonHashKey = p.PersonHashKey
JOIN 
    LinkPersonEmployee lpe ON p.PersonHashKey = lpe.PersonHashKey
JOIN 
    HubEmployee e ON lpe.EmployeeHashKey = e.EmployeeHashKey
LEFT JOIN 
    LinkManagerDepartment lmd ON d.DepartmentHashKey = lmd.DepartmentHashKey
LEFT JOIN 
    HubManager m ON lmd.ManagerHashKey = m.ManagerHashKey AND p.PersonHashKey = m.PersonHashKey
WHERE 
    m.ManagerHashKey IS NULL
GROUP BY 
    d.Name;
