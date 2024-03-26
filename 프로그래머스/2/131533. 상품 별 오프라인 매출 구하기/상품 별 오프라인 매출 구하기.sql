-- 코드를 입력하세요
SELECT product_code,sum(s.sales_amount*p.price) sales
from product p
join offline_sale s on p.product_id=s.product_id
group by product_code
order by sales desc, product_code