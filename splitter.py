import re

# Define the string to be split
text = "Hello, world! This is a test."

# Define the delimiters (e.g., comma, space, exclamation mark, period)
delimiters = r'[,\s!\.]+'

# Split the string using the delimiters
tokens = re.split(delimiters, text)

# Remove any empty strings from the result
tokens = [token for token in tokens if token]

print(tokens)