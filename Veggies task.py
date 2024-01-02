--creation of table for data loading
create or replace table LU_SOIL_TYPE(
SOIL_TYPE_ID number,	
SOIL_TYPE varchar(15),
SOIL_DESCRIPTION varchar(75)
 );

 --create file format 'L8_CHALENGE_FF'
 CREATE FILE FORMAT L8_CHALLENGE_FF
--loading data from the file with the file format to the created table
copy into LU_SOIL_TYPE
from @util_db.public.like_a_window_into_an_s3_bucket
files = ( 'LU_SOIL_TYPE.tsv')
file_format = ( format_name=GARDEN_PLANTS.VEGGIES.PIPECOLSEP_ONEHEADROW );
