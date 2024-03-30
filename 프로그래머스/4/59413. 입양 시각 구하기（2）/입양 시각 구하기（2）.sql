-- 코드를 입력하세요
with recursive t as(
select 0 as hour
union all
select hour +1
    from t
    where hour<23
)
SELECT t.hour hour, if(count(animal_id)>0,count(animal_id),0) count
from animal_outs o
right join t on hour(datetime)=t.hour
group by hour
order by hour