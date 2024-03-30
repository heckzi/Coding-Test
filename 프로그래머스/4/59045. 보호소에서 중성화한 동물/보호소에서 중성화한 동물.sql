-- 코드를 입력하세요
SELECT animal_id,animal_type,name
from animal_outs
where animal_id in
    (
    select animal_id 
    from animal_ins
    where SEX_UPON_INTAKE like ('%Intact%')
    )
    and SEX_UPON_OUTCOME not like('%Intact%')
order by animal_id