select i.item_id,item_name
from item_info i
join item_tree t on i.item_id=t.item_id
where isnull(t.parent_item_id)
order by i.item_id