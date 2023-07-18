# input

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

finalOutput = {};

for i in range(len(keys)) :
    finalOutput[keys[i]] = sample_dict[keys[i]];
    
print(finalOutput);

