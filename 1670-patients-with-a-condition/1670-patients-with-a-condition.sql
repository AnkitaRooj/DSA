# Write your MySQL query statement below
-- select * from Patients;
-- select distinct conditions from Patients
select * from Patients where conditions like "DIAB1%" or conditions like "% DIAB1%"