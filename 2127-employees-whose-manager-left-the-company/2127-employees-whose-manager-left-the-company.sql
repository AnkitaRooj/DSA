# Write your MySQL query statement below
-- select e.*
-- from Employees e join Employees m
-- on e.employee_id = m.manager_id
-- where e.salary < 30000 and  m.manager_id = NULL

select employee_id
from Employees where salary<30000 and manager_id not in (select employee_id from Employees)
order by employee_id