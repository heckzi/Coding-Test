SELECT floor(price/10000)*10000 price_group, count(product_id)
from product
group by price_group
order by price_group