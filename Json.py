// JSON DDL Scripts
USE LIBRARY_CARD_CATALOG;

// Create an Ingestion Table for JSON Data
CREATE TABLE LIBRARY_CARD_CATALOG.PUBLIC.AUTHOR_INGEST_JSON 
(
  RAW_AUTHOR VARIANT
);

//Create File Format for JSON Data
CREATE FILE FORMAT LIBRARY_CARD_CATALOG.PUBLIC.JSON_FILE_FORMAT 
TYPE = 'JSON' 
COMPRESSION = 'AUTO' 
ENABLE_OCTAL = FALSE
ALLOW_DUPLICATE = FALSE 
STRIP_OUTER_ARRAY = TRUE
STRIP_NULL_VALUES = FALSE
IGNORE_UTF8_ERRORS = FALSE; 

//see the full file path
list  @util_db.public.like_a_window_into_an_s3_bucket;

copy into AUTHOR_INGEST_JSON
from @util_db.public.like_a_window_into_an_s3_bucket
files = ( 'author_with_header.json')
file_format = ( format_name='JSON_FILE_FORMAT' );

//view the json files
select raw_author
from AUTHOR_INGEST_JSON;
