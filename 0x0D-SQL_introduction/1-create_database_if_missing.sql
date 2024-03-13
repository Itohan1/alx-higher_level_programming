#!/bin/bash
-- Write a script that creates the database

DROP DATABASE IF EXISTS hbtn_oc_0;
CREATE DATABASE hbtn_oc_0;
Use hbtn_oc_0;
CREATE TABLE datanames (
	names VARCHAR(500)
);

