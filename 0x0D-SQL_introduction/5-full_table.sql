-- This script  that prints the full description of the table first_table from the database hbtn_0c_0
SELECT 
    TABLE_NAME AS 'Table',
    COLUMN_NAME AS 'Column',
    DATA_TYPE AS 'Data Type',
    IS_NULLABLE AS 'Is Nullable',
    COLUMN_DEFAULT AS 'Default Value'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0' AND 
    TABLE_NAME = 'first_table';
