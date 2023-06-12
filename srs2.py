#1
numbers = [4, -9, 8, -11, 8]

negative_count = len(list(filter(lambda x: x < 0, numbers)))

print("Count of negative numbers:", negative_count)

#2
players = ['Ashleigh Barty', 'Simona Halep', 'Naomi Osaka', 'Karolina Pliskova', 'Elina Svitolina']

# Swap the first and last players
players[0], players[-1] = players[-1], players[0]

print(players)

#3
quote = "The reasonable man adapts himself to the world; the unreasonable one persists in trying to adapt the world to himself."

# Split the quote into words
words = quote.split()

# Iterate through the words and swap "reasonable" and "unreasonable"
for i in range(len(words)):
	if words[i] == "reasonable": words[i] = "unreasonable"
	elif words[i] == "unreasonable": words[i] = "reasonable"

# Join the words back into a string
swapped_quote = ' '.join(words)

print(swapped_quote)

