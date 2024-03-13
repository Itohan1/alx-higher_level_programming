#!/bin/bash
#sql credentials

mysql -h localhost -u root -p <<EOF
USE mysql;
DROP TABLE IF EXISTS datanames;
CREATE TABLE datanames(
	name VARCHAR(500)
);
INSERT INTO datanames (name) VALUES ('Database');
INSERT INTO datanames (name) VALUES ('hbtn_0c_0');
INSERT INTO datanames (name) VALUES ('information_schema');
INSERT INTO datanames (name) VALUES ('mysql');
INSERT INTO datanames (name) VALUES ('performance_schema');
INSERT INTO datanames (name) VALUES ('sys');
EOF
