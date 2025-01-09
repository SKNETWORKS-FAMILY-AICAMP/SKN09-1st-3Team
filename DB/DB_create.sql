-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS CarRegistrationDB;
USE CarRegistrationDB;

-- 브랜드 정보 테이블
CREATE TABLE BrandInfo (
    BrandID INT AUTO_INCREMENT PRIMARY KEY,
    BrandName VARCHAR(255) NOT NULL,
    BrandLogo BLOB NULL 
);

-- 국내 차량 등록 데이터 테이블
CREATE TABLE DomesticCarRegistration (
    YearID YEAR, 
    TotalRegistrations INT NOT NULL,
    PRIMARY KEY (YearID)
);

-- 브랜드별 등록 현황 테이블
CREATE TABLE BrandRegistration (
    BrandID INT,
    BrandName VARCHAR(255) NOT NULL,
    YearID YEAR, -- YEAR 타입으로 변경
    Registrations INT NOT NULL,
    MarketShare FLOAT NOT NULL,
    PRIMARY KEY (BrandID, YearID),
    FOREIGN KEY (BrandID) REFERENCES BrandInfo(BrandID),
    FOREIGN KEY (YearID) REFERENCES DomesticCarRegistration(YearID)
);

-- 브랜드 FAQ 테이블
CREATE TABLE BrandFAQ (
    FAQID INT AUTO_INCREMENT PRIMARY KEY,
    BrandID INT,
    Question TEXT,
    Answer TEXT,
    FOREIGN KEY (BrandID) REFERENCES BrandInfo(BrandID)
);