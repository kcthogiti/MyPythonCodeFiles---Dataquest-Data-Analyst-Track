## 2. Use SELECT and LIMIT to Filter Results ##

select College_jobs, Median, Unemployment_rate
from recent_grads
limit 20;

## 3. Use WHERE to Filter Results ##

select Major
from recent_grads
where Major_category = "Arts"
limit 5;

## 4. Express Criteria With Operators ##

select major, total, median, unemployment_rate
from recent_grads
where (median <= 50000 or unemployment_rate > 0.065)
and Major_category != "Engineering"

## 5. Order Your Results ##

select Major
from recent_grads
where major_category != "Engineering"
order by Major Desc
limit 20;