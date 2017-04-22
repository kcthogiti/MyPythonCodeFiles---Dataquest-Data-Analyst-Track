## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for car, ship in enumerate(ships):
    print(ship)
    print(cars[car])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i, elem in enumerate(things):
    elem.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]

apple_prices_doubled = [apple_price*2 for apple_price in apple_prices]
apple_prices_lowered = [apple_price-100 for apple_price in apple_prices]

## 5. Counting Female Names ##

name_counts = {}
for row in legislators:
    if (row[3] == "F" and row[7] > 1940):
        name = row[1]
        if name in name_counts:
            name_counts[name] = name_counts[name] + 1
        else:
            name_counts[name] = 1
    

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
for elem in values:
    chk =  elem is not None and elem > 30
    checks.append(chk)
        

## 8. Highest Female Name Count ##

max_value = None

for k in name_counts:
    count = name_counts[k]
    if (max_value is None or count > max_value):
        max_value = count


## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for p, t in plant_types.items():
    print(p)
    print(t)

## 10. Finding the Most Common Female Names ##

top_female_names = []

for k in name_counts:
    if (name_counts[k] == 2):
        top_female_names.append(k)