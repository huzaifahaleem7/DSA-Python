# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem
arr = []

with open("nyc_weather.csv") as f:
    for line in f:
        tokens = line.split(",")
        print(tokens)
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature")

print(arr)

# What was the average temperature in first week of Jan
print(sum(arr[:7]) / len(arr[:7]))

# What was the maximum temperature in first 10 days of Jan
print(max(arr[:10]))

# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
# Figure out data structure that is best for this problem

weather = {}
with open("nyc_weather.csv") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather[day] = temperature
        except:
            print("Invalid temperature")
print(weather)

# What was the temperature on Jan 9
print(weather["Jan 9"])

# What was the temperature on Jan 4
print(weather["Jan 4"])

# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
#  'diverged': 2,
#  'in': 3,
#  'I': 8
word_count = {}
with open("poem.txt", "r") as f:
    for line in f:
        print(line)
        tokens = line.split(" ")
        print(tokens)
        for token in tokens:
            token = token.replace("\n", "")
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1

print(word_count)
print("Count of 'diverged':", word_count.get("diverged", 0))
