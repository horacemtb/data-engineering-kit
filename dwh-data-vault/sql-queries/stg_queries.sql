-- Create Person table в Staging area
CREATE TABLE STG_Person (
    PersonID INT PRIMARY KEY,
    Name VARCHAR(255),
    Surname VARCHAR(255),
    SocialSecurityID VARCHAR(255),
    CompanyID INT
);

-- Copy data into STG_Person
INSERT INTO STG_Person (PersonID, Name, Surname, SocialSecurityID, CompanyID)
SELECT PersonID, Name, Surname, SocialSecurityID, CompanyID
FROM Person;

-- Create Manager table in Staging area
CREATE TABLE STG_Manager (
    ManagerID INT PRIMARY KEY,
    PersonID INT,
    DepartmentID INT
);

-- Copy data into STG_Manager
INSERT INTO STG_Manager (ManagerID, PersonID, DepartmentID)
SELECT ManagerID, PersonID, DepartmentID
FROM Manager;

-- Create Department table in Staging area
CREATE TABLE STG_Department (
    DepartmentID INT PRIMARY KEY,
    Name VARCHAR(255),
    Description TEXT
);

-- Copy data into STG_Department
INSERT INTO STG_Department (DepartmentID, Name, Description)
SELECT DepartmentID, Name, Description
FROM Department;

-- Create Company table in Staging area
CREATE TABLE STG_Company (
    CompanyID INT PRIMARY KEY,
    Name VARCHAR(255),
    Location VARCHAR(255)
);

-- Copy data into STG_Company
INSERT INTO STG_Company (CompanyID, Name, Location)
SELECT CompanyID, Name, Location
FROM Company;

-- Create STG_CompanyDepartments table
CREATE TABLE STG_CompanyDepartments (
    CompanyID INT,
    DepartmentID INT,
    PRIMARY KEY (CompanyID, DepartmentID)
);

-- Copy data into STG_CompanyDepartments
INSERT INTO STG_CompanyDepartments (CompanyID, DepartmentID)
SELECT CompanyID, DepartmentID
FROM CompanyDepartments;

-- Create STG_Employee table
CREATE TABLE STG_Employee (
    EmployeeID INT PRIMARY KEY,
    PersonID INT,
    Position VARCHAR(255)
);

-- Copy data into STG_Employee
INSERT INTO STG_Employee (EmployeeID, PersonID, Position)
SELECT EmployeeID, PersonID, Position
FROM Employee;