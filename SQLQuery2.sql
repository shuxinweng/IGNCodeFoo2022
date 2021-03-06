USE IGNCodeFoo
GO

IF OBJECT_ID('IGNCodeFooData') IS NOT NULL
	DROP TABLE IGNCodeFooData;
GO

CREATE TABLE IGNCodeFooData (
	Media_Type NVARCHAR(10) NOT NULL,
	Name_	NVARCHAR(100) NOT NULL,
	Long_Description	NVARCHAR(255) NOT NULL,
	Created_At	DATETIME NOT NULL,
	Updated_At	DATETIME NOT NULL,
	Review_URL	NVARCHAR(100) NOT NULL,
	Review_Score	NVARCHAR(5) NOT NULL,
	Genres	NVARCHAR(10) NOT NULL,
	Created_By	NVARCHAR(20) NOT NULL,
	Published_By	NVARCHAR(20) NOT NULL,
	Franchises	NVARCHAR(10) NOT NULL,
	Regions	NVARCHAR(20) NOT NULL,
);
GO

SELECT *
FROM IGNCodeFooData