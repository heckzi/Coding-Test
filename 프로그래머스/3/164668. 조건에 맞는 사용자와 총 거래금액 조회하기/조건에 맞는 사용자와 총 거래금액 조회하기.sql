-- 코드를 입력하세요
SELECT user_id,nickname,sum(price) as total_sales
from USED_GOODS_USER as u
join used_goods_board as b
on u.user_id = b.writer_id
where b.status='DONE'
group by user_id
having total_sales>=700000
order by total_sales
