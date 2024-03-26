select i.item_id,item_name,rarity
from item_info i
join item_tree t on i.item_id=t.item_id
where parent_item_id in (select item_id from item_info where rarity='RARE')
order by i.item_id desc