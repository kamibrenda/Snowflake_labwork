  
--creating Soil type data table 
CREATE OR REPLACE table LU_SOIL_TYPE(
SOIL_TYPE_ID number (2),
SOIL_TYPE varchar (15),
SOIL_DESCRIPTION varchar (75)
);

create or replace file format garden_plants.veggies.L8_CHALLENGE_FF 
    TYPE = 'CSV'--csv for comma separated files
    SKIP_HEADER = 1 --one header row  
    FIELD_DELIMITER='0x09',
    TRIM_SPACE=FALSE,
    FIELD_OPTIONALLY_ENCLOSED_BY=NONE,
    REPLACE_INVALID_CHARACTERS=TRUE,
    DATE_FORMAT=AUTO,
    TIME_FORMAT=AUTO,
    TIMESTAMP_FORMAT=AUTO
    ;    

copy into LU_SOIL_TYPE
from @util_db.public.like_a_window_into_an_s3_bucket
files = ( 'LU_SOIL_TYPE.tsv')
file_format = ( format_name='L8_CHALLENGE_FF' );