--looking for all the files in S3 bucket stage
list @like_a_window_into_an_S3_bucket;
--looking for a file in an S3(Have to be specific with the cases i.e File was in uppercase)
list @like_a_window_into_an_S3_bucket/THIS_;
--looking for a file in an S3(Have to be specific with the cases i.e File was in lowercase)
list @like_a_window_into_an_S3_bucket/this_;