--Creating the sequence
create or replace sequence SEQ_AUTHOR_UID
     start = 1
     increment = 1
     comment = 'Use this to fill in AUTHOR_UID';

--Query the sequence
SELECT SEQ_AUTHOR_UID.nextval, SEQ_AUTHOR_UID.nextval;

--show the sequences existing
show sequences;