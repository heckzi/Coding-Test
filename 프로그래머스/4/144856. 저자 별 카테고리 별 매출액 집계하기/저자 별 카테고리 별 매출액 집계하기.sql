-- 코드를 입력하세요
SELECT b.author_id, author_name,b.category,sum(s.sales*b.price) as total_sales
from book as b
join book_sales as s on b.book_id = s.book_id
join author as a on b.author_id = a.author_id
where year(s.sales_date)='2022' and month(s.sales_date)='01'
group by a.author_id,b.category
order by a.author_id,category desc