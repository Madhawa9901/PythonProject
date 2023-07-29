print("Heelo World!")

#num_1 = int(input("Enter a number:"))
#num_2 = int(input("Enter a number:"))
#sum = num_1 + num_2
#print(num_1 + num_2)

var_1 = 10
var_2 = 10.75
var_3 = 1+6j
var_4 = [2,3,4]
var_5 = {3,4,5}
var_6 = {"name":'Lemo'}
var_7 = (2,3,4)
var_8 = "Hello"



print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))
print(type(var_5))
print(type(var_6))
print(type(var_7))
print(type(var_8))

def test(a,b):
    """doc string"""
    print(a , "-" , b)

test(10,15)

print(test.__doc__)

list_1 = [2,3,'Hello',True,8+7j], 

print(list_1)

#membership operators
# in , not in

#print(2 in list_1)
a = 4
if a in list_1:
    print(a,"is in list_1")

#string slising

str_1 = "Hello_World"

print(str_1[2:5])
print(str_1[4:7])
print(str_1[8:])
print(str_1[9:])
print(str_1[:4])
print(str_1.upper())
print(str_1.lower())
print(str_1.swapcase())

print(str_1+str_1)
print(str_1*5)

a= 10
b = 20

print("a is ",a,"and ","b is ",b)
print(f'a is {a} and b is {b}')
print('a is {} and b is {}'.format(a,b))
print('a is {a} and b is {b}'.format(a = 10,b = 20))

a= 10
print

list_2 = [2,3,4]

list_3 = [5,6,7]
list_2.append("Hello")
print(list_2)
print("initial list 2",list_2,end=" --- ")
print("initial list 3",list_3)

dict_1 = {'name':"nimal",
        "marks":[23,24,25,20],
        "subjects":{0:"cs",1:"MT",3:"physics"},
        100:"hello"
        }
print(dict_1["marks"])
print(dict_1["marks"][1])
print(dict_1["subjects"][0])
print(dict_1.items())
print(dict_1.keys())
print(dict_1.values())

dict_1.update({"test":100})

print(dict_1)

for i in [1,2,3,4,5]:
    print(i,end =" -- ")
for i in "Hello":
    print(i,end =" -- ")

f= open("test.py","r")
content = f.read()
print(content)
f.close()

with open("test.py","r") as f:
    content_2 = f.read()
    print(content_2)





