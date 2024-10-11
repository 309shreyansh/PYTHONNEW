#arithmetic operator
a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #used for remainder
print(a**b) #used for a^b

#relational operator
a=50
b=20

print(a==b) #False
print(a!=b) #True
print(a>=b) #True
print(a>b)  #True
print(a<=b) #False
print(a<b)  #False

#assignment operators

num = 10
num = num+10 #10+10=> 20
print("num:",num)

num=10
num+=10
print("num:",num)

num=10
num-=10
print("num:",num)

num=10
num*=10
print("num:",num)

num=10
num/=10
print("num:",num)

num=10
num%=10
print("num:",num)

#logical operators 

print(not False)
print(not True)

a=50
b=30
print(not(a>b))

val1=True
val2=True
print("AND operator:", val1 and val2)

val1=True
val2=False
print("AND operator:", val1 and val2)

print("OR operator:", (a == b)or (a > b))  