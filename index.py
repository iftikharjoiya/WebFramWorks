print("hello world")

# sum 
variable1=7
variable2=3
sum=variable1+variable2
print(sum)
# Difference 
variable1=7
variable2=3
sum=variable1-variable2
print(sum)
# Multiply 
variable1=7
variable2=3
sum=variable1*variable2
print(sum)
# Divide 
variable1=7
variable2=3
sum=variable1/variable2
print(sum)
#cheking data type
a="31"
print(type(a))
#input from user
myStr=input("enter String")
#strings
myStr="First String"
print(myStr)
#string slicing
sl=myStr[:9]
print(sl)
#functions of string
length=len(myStr)
print(length)
bol=myStr.endswith("que")
print(bol)
#lists
cars=["Vigo","Mehran","Toyota"]
print(cars)
id=cars[1:]
print(id)
integer_List=[1,3,7,5,6,8,2,9]
print(integer_List)
integer_List.sort()
print(integer_List)
integer_List.reverse()
print(integer_List)
integer_List.append(0)
print(integer_List)
integer_List.insert(4,7)
print(integer_List)
# tupples
integer_Touple=(1,2,3,7,1)
print(integer_Touple)
count=integer_Touple.count(1)
print(count)
#dictionary
class_result={"name":"eisha","marks":23}
print(class_result)
print(class_result.items())
print(class_result.keys())
#sets
MySet = {"apple", "banana", "cherry"}
print(MySet)
MySet = {"apple", "banana", "cherry"}
print(len(MySet))
MySet = {"apple", "banana", "cherry"}
MySet.add("orange")
print(MySet)
#conditinal expressions
num1 = 33
num2 = 200
if num1 > num2:
  print("num2 is greater than num1")
  
numb=30
if numb > 20:
    print("it is true")
elif age > 35:
    print ("it is my age")
else:
    print("it is wrong")
#loops
#while loop
i = 1
while i < 10:
  print(i)
  i += 1
# for loop 
integer_List=[1,3,7,5,6,8,2,9]
for x in integer_List:
  print(x)
 #break 
integer_List=[1,3,7,5,6,8,2,9]
for x in integer_List:
  print(x)
  if x == 7:
    break
#continue
integer_List=[1,3,7,5,6,8,2,9]
for x in veg:
  if x == 8:
    continue
  print(x)
    