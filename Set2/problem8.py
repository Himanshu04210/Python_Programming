# input
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Expected output
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

employeee = {};

for i in range(len(employees)) :
    employeee[employees[i]] = defaults;
    
print(employeee);