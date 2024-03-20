SELECT mcdp_cd as '진료과코드',count(mcdp_cd) as '5월예약건수'
from appointment
where month(apnt_ymd)=5
group by mcdp_cd
order by `5월예약건수` asc,`진료과코드` asc