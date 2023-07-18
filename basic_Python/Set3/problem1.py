# - *Input*: [("John", 25), ("Jane", 30)]
# - *Output*: "John is 25 years old. Jane is 30 years old."
data = [("John", 25), ("Jane", 30)]

output = ""
for item in data:
    name, age = item
    output += f"{name} is {age} years old. "

output = output.rstrip()  # Remove trailing whitespace
print(output)

