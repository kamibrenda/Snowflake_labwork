--creation of table for data loading
CREATE OR REPLACE table VEGETABLE_DETAILS_PLANT_HEIGHT (
plant_name	varchar (25),
UOM	varchar (1),
Low_End_of_Range	Number(30),
High_End_of_Range Number(30)
);

--loading data from the file with the file format to the created table
COPY INTO VEGETABLE_DETAILS_PLANT_HEIGHT
FROM '@util_db.public.like_a_window_into_an_s3_bucket'
FILES = ('veg_plant_height.csv')
FILE_FORMAT = (
    TYPE='CSV',
    SKIP_HEADER=1,
    FIELD_DELIMITER=',',
    TRIM_SPACE=FALSE,
    FIELD_OPTIONALLY_ENCLOSED_BY='"',
    REPLACE_INVALID_CHARACTERS=TRUE,
    DATE_FORMAT=AUTO,
    TIME_FORMAT=AUTO,
    TIMESTAMP_FORMAT=AUTO
)
ON_ERROR=ABORT_STATEMENT
PURGE=TRUE
