-- Write a script that deletes the database hbtn_0c_0 in your MySQL server

IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'hbtn_0c_0')THEN

	DROP DATABASE hbtn_oc_0;
END IF;

