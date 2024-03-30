-- 코드를 입력하세요
SELECT distinct car_id
from CAR_RENTAL_COMPANY_CAR c
where car_id in (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where month(start_date)=10
    )
    and car_type='세단'
order by car_id desc