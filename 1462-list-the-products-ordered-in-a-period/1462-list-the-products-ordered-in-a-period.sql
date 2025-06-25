# Write your MySQL query statement below
select product_name,unit 
from 
(select p.product_id,product_name,product_category,order_date,sum(unit) as unit from Products p join Orders od on p.product_id=od.product_id 
where order_date between '2020-02-01' and '2020-02-29'
group by product_name
) as d
where unit>=100

