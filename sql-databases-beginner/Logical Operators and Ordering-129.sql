## 2. Returning Multiple Conditions With AND ##

select Major, ShareWomen, Employed
from recent_grads
where sharewomen > 0.5 and employed > 10000
limit 10;

## 3. Returning One of Several Conditions With OR ##

select Major, Median, Unemployed
from recent_grads
where Median >= 10000 or unemployed <=1000
limit 20;

## 4. Grouping Operators With Parentheses ##

select Major, Major_category, ShareWomen, Unemployment_rate
from recent_grads
where Major_category = "Engineering" and (Sharewomen > 0.5 or Unemployment_rate < 0.051)

## 5. Practice Grouping Operators ##

select Major, Major_category, Employed, Unemployment_rate
from recent_grads
where Major_category in ("Business", "Arts", "Health")
and (Employed > 20000 or unemployment_rate < 0.051);

## 6. Order Results With ORDER BY ##

select Major
from recent_grads
order by Major desc
limit 10;

## 7. Order Results Based on Multiple Columns ##

select Major_category, Median, Major
from recent_grads
order by Major, Median Desc
limit 20;