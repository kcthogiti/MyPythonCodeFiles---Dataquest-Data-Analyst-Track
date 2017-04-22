## 1. Probability basics ##

# Print the first two rows of the data.
print(flags.columns)

most_bars_country = flags["name"][flags["bars"].idxmax()]

highest_population_country = flags["name"][flags["population"].idxmax()]

## 2. Calculating probability ##

total_countries = flags.shape[0]

orange_probability = flags[flags["orange"] == 1].shape[0]/total_countries

stripe_probability = flags[flags["stripes"] > 1].shape[0]/total_countries



## 3. Conjunctive probabilities ##

five_heads = .5 ** 5

ten_heads = 0.5**10

hundred_heads = 0.5**100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
l = flags[flags["red"] == 1].shape[0]
L = flags.shape[0]

three_red = (l/L)*((l-1)/(L-1))*((l-2)/(L-2))


## 5. Disjunctive probability ##

start = 1
end = 18000

num = 0
num1 = 0
for x in range(1, 18001):
    if x%100 == 0:
        num += 1
    if x%70 == 0:
        num1 += 1

hundred_prob = num/18000
seventy_prob = num1/18000
        

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None
red = flags[flags["red"] == 1].shape[0] / flags.shape[0]
orange = flags[flags["orange"] == 1].shape[0] / flags.shape[0]
red_and_orange = flags[(flags["red"] == 1) & (flags["orange"] == 1)].shape[0] / flags.shape[0]

red_or_orange = red + orange - red_and_orange

stripes = flags[flags["stripes"] > 0].shape[0] / flags.shape[0]
bars = flags[flags["bars"] > 0].shape[0] / flags.shape[0]
stripes_and_bars = flags[(flags["stripes"] > 0) & (flags["bars"] > 0)].shape[0] / flags.shape[0]

stripes_or_bars = stripes + bars - stripes_and_bars

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None

heads_or = (1 - (1/8))