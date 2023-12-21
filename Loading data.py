--creating a table
create or replace table vegetable_details_soil_type(
plant_name varchar (25),
soil_type number(1,0) 
);


--loading data from the S3 stage
copy into vegetable_details_soil_type
from @util_db.public.like_a_window_into_an_s3_bucket
files = ( 'VEG_NAME_TO_SOIL_TYPE_PIPE.txt')
file_format = ( format_name=GARDEN_PLANTS.VEGGIES.PIPECOLSEP_ONEHEADROW );