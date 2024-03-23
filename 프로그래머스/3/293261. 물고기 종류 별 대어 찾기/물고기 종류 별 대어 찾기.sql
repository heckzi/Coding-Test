-- 코드를 작성해주세요

select f.id,n.fish_name,f.length length
from fish_info f
join fish_name_info n on f.fish_type=n.fish_type
where (f.fish_type,f.length) in (
    select fish_type,max(f.length)
    from fish_info f
    group by fish_type
)
order by f.id