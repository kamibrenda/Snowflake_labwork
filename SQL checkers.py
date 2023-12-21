--Using Code to Check Your Work
select * from GARDEN_PLANTS.INFORMATION_SCHEMA.SCHEMATA;

-- Checking for Schemas by Name
SELECT *
FROM GARDEN_PLANTS.INFORMATION_SCHEMA.SCHEMATA
WHERE SCHEMA_NAME IN ('FLOWERS', 'FRUITS','VEGGIES');

--Counting the Number of Correctly Named Schemas
SELECT count (*) as SCHEMAS_FOUND, '3' as SCHEMAS_EXPECTED
FROM GARDEN_PLANTS.INFORMATION_SCHEMA.SCHEMATA
WHERE SCHEMA_NAME IN ('flowers','fruits','Veggies');

