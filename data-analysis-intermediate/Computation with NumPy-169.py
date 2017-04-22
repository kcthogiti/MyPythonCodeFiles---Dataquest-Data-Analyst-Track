## 2. Array Comparisons ##

countries_canada = world_alcohol[:,2] == "Canada"
years_1984 = world_alcohol[:,0] == "1984"

## 3. Selecting Elements ##

country_is_algeria = (world_alcohol[:,2] == "Algeria")
country_algeria = world_alcohol[country_is_algeria, :]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Algeria") 

rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986, :]

## 5. Replacing Values ##

a = (world_alcohol[:, 0] == "1986")
world_alcohol[a,0] = "2014"

b = (world_alcohol[:,3] == "Wine")
world_alcohol[b,3] = "Grog"

## 6. Replacing Empty Strings ##

is_value_empty = (world_alcohol[:,4] == "")
world_alcohol[is_value_empty, 4] = "0"

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]

alcohol_consumption = alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

is_canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == '1986')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = canada_1986[:,4]
empty_strings = canada_alcohol == ''
canada_alcohol[empty_strings] = "0"
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating Consumption for Each Country ##

totals = {}
year = "1989"
for row in countries:
    a = (world_alcohol[:,0] == year) & (world_alcohol[:,2] == row)
    country_consumption = world_alcohol[a, 4]
    print(country_consumption)
    b = (country_consumption == "")
    country_consumption[b] = "0"
    country_consumption = country_consumption.astype(float)
    total = country_consumption.sum()
    totals[row] = total

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for elem in totals:
    if (totals[elem] > highest_value):
        highest_value = totals[elem]
        highest_key = elem
