# Write your MySQL query statement below
select m.name from Employee e, Employee m where e.managerId=m.id
group by e.managerId
having count(*) >= 5

-- select m.name
-- from employee e
-- join employee m
-- where e.managerid=m.id
-- group by e.managerid
-- having count(*) >=5

-- select name
-- from Employee e where id in
-- (select managerId from employee group by managerId having count(*) >= 5) 

