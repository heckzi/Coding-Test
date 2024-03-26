-- 코드를 입력하세요
SELECT o.animal_id,o.name
from animal_outs o
where o.animal_id not in
    (
    select animal_id from animal_ins
    )
order by animal_id