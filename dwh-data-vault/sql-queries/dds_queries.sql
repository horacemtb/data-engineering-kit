-- HubPerson
CREATE TABLE HubPerson (
    PersonHashKey CHAR(64) PRIMARY KEY,
    BusinessKey_SocialSecurityID VARCHAR(255) NOT NULL,
    LoadTS TIMESTAMP,
    Source VARCHAR(50)
);

-- HubManager
CREATE TABLE HubManager (
    ManagerHashKey CHAR(64) PRIMARY KEY,
    BusinessKey_ManagerID INT NOT NULL,
    LoadTS TIMESTAMP,
    Source VARCHAR(50)
);

-- HubDepartment
CREATE TABLE HubDepartment (
    DepartmentHashKey CHAR(64) PRIMARY KEY,
    BusinessKey_DepartmentID INT NOT NULL,
    LoadTS TIMESTAMP,
    Source VARCHAR(50)
);

-- HubCompany
CREATE TABLE HubCompany (
    CompanyHashKey CHAR(64) PRIMARY KEY,
    BusinessKey_CompanyID INT NOT NULL,
    LoadTS TIMESTAMP,
    Source VARCHAR(50)
);

-- HubEmployee
CREATE TABLE HubEmployee (
    EmployeeHashKey CHAR(64) PRIMARY KEY,
    BusinessKey_EmployeeID INT NOT NULL,
    LoadTS TIMESTAMP,
    Source VARCHAR(50)
);


-- SatPerson
CREATE TABLE SatPerson (
    PersonHashKey CHAR(64),
    HashDiff CHAR(64),
    Name VARCHAR(255),
    Surname VARCHAR(255),
    LoadTS TIMESTAMP,
    Source VARCHAR(50),
    PRIMARY KEY (PersonHashKey, HashDiff),
    FOREIGN KEY (PersonHashKey) REFERENCES HubPerson(PersonHashKey)
);

-- SatDepartment
CREATE TABLE SatDepartment (
    DepartmentHashKey CHAR(64),
    HashDiff CHAR(64),
    Name VARCHAR(255),
    Description TEXT,
    LoadTS TIMESTAMP,
    Source VARCHAR(50),
    PRIMARY KEY (DepartmentHashKey, HashDiff),
    FOREIGN KEY (DepartmentHashKey) REFERENCES HubDepartment(DepartmentHashKey)
);

-- SatCompany
CREATE TABLE SatCompany (
    CompanyHashKey CHAR(64),
    HashDiff CHAR(64),
    Name VARCHAR(255),
    Location VARCHAR(255),
    LoadTS TIMESTAMP,
    Source VARCHAR(50),
    PRIMARY KEY (CompanyHashKey, HashDiff),
    FOREIGN KEY (CompanyHashKey) REFERENCES HubCompany(CompanyHashKey)
);

-- SatEmployee
CREATE TABLE SatEmployee (
    EmployeeHashKey CHAR(64),
    HashDiff CHAR(64),
    Position VARCHAR(255),
    LoadTS TIMESTAMP,
    Source VARCHAR(50),
    PRIMARY KEY (EmployeeHashKey, HashDiff),
    FOREIGN KEY (EmployeeHashKey) REFERENCES HubEmployee(EmployeeHashKey)
);


-- LinkPersonCompany
CREATE TABLE LinkPersonCompany (
    PersonCompanyHashKey CHAR(64) PRIMARY KEY,
    PersonHashKey CHAR(64),
    CompanyHashKey CHAR(64),
    LoadTS TIMESTAMP,
    Source VARCHAR(50),
    FOREIGN KEY (PersonHashKey) REFERENCES HubPerson(PersonHashKey),
    FOREIGN KEY (CompanyHashKey) REFERENCES HubCompany(CompanyHashKey)
);

-- LinkManagerDepartment
CREATE TABLE LinkManagerDepartment (
    ManagerDepartmentHashKey CHAR(64) PRIMARY KEY,
    ManagerHashKey CHAR(64),
    DepartmentHashKey CHAR(64),
    LoadTS TIMESTAMP,
    Source VARCHAR(50),
    FOREIGN KEY (ManagerHashKey) REFERENCES HubManager(ManagerHashKey),
    FOREIGN KEY (DepartmentHashKey) REFERENCES HubDepartment(DepartmentHashKey)
);

-- LinkCompanyDepartment
CREATE TABLE LinkCompanyDepartment (
    CompanyDepartmentHashKey CHAR(64) PRIMARY KEY,
    CompanyHashKey CHAR(64),
    DepartmentHashKey CHAR(64),
    LoadTS TIMESTAMP,
    Source VARCHAR(50),
    FOREIGN KEY (CompanyHashKey) REFERENCES HubCompany(CompanyHashKey),
    FOREIGN KEY (DepartmentHashKey) REFERENCES HubDepartment(DepartmentHashKey)
);

-- LinkPersonManager
CREATE TABLE LinkPersonManager (
    PersonManagerHashKey CHAR(64) PRIMARY KEY,
    PersonHashKey CHAR(64),
    ManagerHashKey CHAR(64),
    LoadTS TIMESTAMP,
    Source VARCHAR(50),
    FOREIGN KEY (PersonHashKey) REFERENCES HubPerson(PersonHashKey),
    FOREIGN KEY (ManagerHashKey) REFERENCES HubManager(ManagerHashKey)
);

-- LinkPersonEmployee
CREATE TABLE LinkPersonEmployee (
    PersonEmployeeHashKey CHAR(64) PRIMARY KEY,
    PersonHashKey CHAR(64),
    EmployeeHashKey CHAR(64),
    LoadTS TIMESTAMP,
    Source VARCHAR(50),
    FOREIGN KEY (PersonHashKey) REFERENCES HubPerson(PersonHashKey),
    FOREIGN KEY (EmployeeHashKey) REFERENCES HubEmployee(EmployeeHashKey)
);
