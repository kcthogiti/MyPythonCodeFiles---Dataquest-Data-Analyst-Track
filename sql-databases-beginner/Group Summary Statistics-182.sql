## 1. Introduction ##

select *
from recent_grads
limit 5;

## 2. Calculating Group-Level Summary Statistics ##

SELECT Major_category, AVG(ShareWomen) FROM recent_grads GROUP BY Major_category;

## 3. Renaming Columns With the AS Statement ##

select sum(men) total_men, sum(women) total_women
from recent_grads

## 4. Practice: Using GROUP BY ##

select major_category, avg(employed)/avg(total) share_employed
from recent_grads
group by major_category;

## 5. Querying Virtual Columns With the HAVING Statement ##

select major_category, avg(low_wage_jobs)/avg(total) as share_low_wage
from recent_grads
group by major_category
having share_low_wage > 0.1

## 6. Rounding Results With the ROUND Function ##

SELECT ROUND(ShareWomen, 4), Major_category FROM recent_grads LIMIT 10;

## 7. Nesting functions ##

select Major_category, ROUND(AVG(College_jobs)/AVG(Total),3) share_degree_jobs
FROM recent_grads
GROUP BY Major_category
HAVING share_degree_jobs < 0.3;