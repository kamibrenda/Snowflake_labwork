// Create a new database and set the context to use the new database
CREATE DATABASE LIBRARY_CARD_CATALOG COMMENT = 'DWW Lesson 9 ';
USE DATABASE LIBRARY_CARD_CATALOG;


// Create Author table
CREATE OR REPLACE TABLE AUTHOR (
   AUTHOR_UID NUMBER 
  ,FIRST_NAME VARCHAR(50)
  ,MIDDLE_NAME VARCHAR(50)
  ,LAST_NAME VARCHAR(50)
);

// Insert the first two authors into the Author table
INSERT INTO AUTHOR(AUTHOR_UID,FIRST_NAME,MIDDLE_NAME, LAST_NAME) 
Values
(1, 'Fiona', '','Macdonald')
,(2, 'Gian','Paulo','Faleschini');

// Look at your table with it's new rows
SELECT * 
FROM AUTHOR;
