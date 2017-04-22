## 2. Sets ##

gender = []
for elem in legislators:
    gender.append(elem[3])

gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

party = []
for elem in legislators:
    party.append(elem[6])
party = set(party)
print(party)
print(legislators)

## 4. Missing Values ##

for elem in legislators:
    if elem[3] == "":
        elem[3] = "M"


## 5. Parsing Birth Years ##

birth_years = []
for elem in legislators:
    parts = elem[2].split("-")
    birth_years.append(parts[0])

## 6. Try/except Blocks ##

try:
    float("hello")
except Exception:
    print("Error converting to float..")
    

## 7. Exception Instances ##

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
for elem in birth_years:
    year = elem
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)
    

## 9. Convert Birth Years to Integers ##

for elem in legislators:
    ls = elem[2].split("-")
    try:
        birth_year = int(ls[0])
    except:
        birth_year = 0
    elem.append(birth_year)


## 10. Fill in Years Without a Value ##

last_value = 1
for elem in legislators:
    if elem[7] == 0:
        elem[7] = last_value
    last_value = elem[7]