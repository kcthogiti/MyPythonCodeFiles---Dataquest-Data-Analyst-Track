## 2. Calculating expected values ##

males_over50k = 0.669*0.241*32561
males_under50k = 0.669*0.759*32561

females_over50k = 0.331*0.241*32561
females_under50k = 0.331*0.759*32561

## 3. Calculating chi-squared ##

import numpy as np
from scipy.stats import chisquare
obs = np.array([6662, 1179, 15128, 9592])
exp = np.array([5249.8, 2597.4, 16533.5, 8180.3])


chisq_gender_income, p = chisquare(obs, exp)


## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare
obs = np.array([6662, 1179, 15128, 9592])
exp = np.array([5249.8, 2597.4, 16533.5, 8180.3])


chisq_gender_income, pvalue_gender_income = chisquare(obs, exp)


## 5. Cross tables ##

import pandas
table = pandas.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding expected values ##

import pandas
import numpy as np
from scipy.stats import chi2_contingency
table = pandas.crosstab(income["sex"], [income["race"]])

chisq_value, pvalue_gender_race, df, expected = chi2_contingency(table)