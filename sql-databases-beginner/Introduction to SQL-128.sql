## 4. Querying a SQLite Database ##

select Rank, Major
from recent_grads;

## 5. Specifying Column Order for Our Results ##

select Major, Rank
from recent_grads;

## 6. Practice: Selecting Columns With SELECT ##

select Rank, Major_code, Major, Major_category, Total
from recent_grads;

## 7. Filtering With the WHERE Statement ##

select Major, ShareWomen
from recent_grads
where sharewomen > 0.5

## 8. Practice: Filtering With WHERE Statements ##

select Major, Employed
from recent_grads
where Employed > 10000

## 9. Limiting the Number of Results ##

select Major
from recent_grads
where employed > 10000
limit 10;