import json


numbers = [10, 20, 30, 70, 191, 23]  #create a set of numbers

filename = 'numbers.json'          #use the file extension .json

with open(filename, 'w') as file_object:  #open the file in write mode
    json.dump(numbers, file_object)   # json.dump() function to stores the set of numbers in numbers.json file

#========================================

#serailizing Data
data = {
    'Name' : 'Felix',
    'Occupation' : 'Doctor'
}
#print(type(data))
a = json.dumps(data) # converting dictionary to JSON
#print(type(a))
#print(a)


#=========================================
with open('student.json','r') as file_object:  
  data = json.load(file_object)  

#print(data)
#print(type(data))


#==================================
# deserailizing the data
json_var  = '{"Name" : "Felix", "status" : "married"}'
# parse dict_1:
y = json.loads(json_var)

# the result is a Python dictionary:
print(y) 
print(type(y))