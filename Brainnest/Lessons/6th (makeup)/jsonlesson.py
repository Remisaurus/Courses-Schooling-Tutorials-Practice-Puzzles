
import json

# {key:value mapping}
a ={"name":"John",
"age":31,
	"Salary":25000}

# conversion to JSON done by dumps() function
b = json.dumps(a)

# printing the output
print(b)


import json

# JSON string
employee = '{"id":"09", "name": "Bob", "department":"Finance"}'

# Convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))


# Convert Python dict to JSON
employee = '{"id":"09", "name": "Bob", "department":"Finance"}'
employee_dict = json.loads(employee)
json_object = json.dumps(employee_dict, indent=4)
print(json_object)
print(type(json_object))

# data types

# string
{ "name":"User" }

# number
{ "age": 20 }
{ "percentage": 82.44}

# boolean 
{ "result" : true }

# null
{ "result" : null }

# object
{
"Student":{ "name":"Peter", "age":20, "score": 50.05}
}

# array
{
  "collection" : [
        {"id" : 101},
        {"id" : 102},
        {"id" : 103}
  ]
}


'''
Python object	JSON object
dict	        object
list, tuple	    array
str	            string
int, float	    numbers
True	        true
False	        false
None	        null
'''

# serialization (transformation of data into a series of bytes (hence serial) to be stored or transmitted across a network.)
import json

var = {
	"Subjects": {
				"Maths":85,
				"Physics":90
				}
	}

with open("Sample.json", "w") as p:
	json.dump(var, p)

# deserialization
import json

json_var ="""
{
    "Country": {
        "name": "null",
        "Languages_spoken": [
            {
                "names": ["English", "Spanish"]
            }
        ]
    }
}
"""
var = json.loads(json_var)

print(var)


