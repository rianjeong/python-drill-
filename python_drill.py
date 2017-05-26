#define variables
t = 11
x = 8
y = 19
z = 'Rian'

#use operators =,+,-,*,%,+= and float variable
print (x + y)
print (x * y)
print (y - x)
print float(y) / x
print(x % y) 
    
t += x
print "The value of t is ", t


#create a number list
number_list=[1,2,3,4,5,6,7,8,9]
print number_list

#for loop iterating and printing on different lines
for x in number_list:
 print x + 100




# if, elif, else statement  
if number_list[6]  <= 4:
    print "this number {}".format(number_list[6]) + " is less then 4"
elif number_list[2]  >= 4:
    print "this number {}".format(number_list[2]) + " is not greater than 4"
else:
    print "this number {}".format(number_list[3]) + " is equal to 4"


#while loop
n = 21
i = 3
sum = 0
while i <= 21:
    sum = sum + i
    i = i + 3
print sum

#operators and,or, not
x = True
y = False


print ('x and y are the same ', x and y)
print ('x or y are the same ', x or y)
print ('x is not y ', not x)

#Tuple
t=( 'Dog', 'cat', 'sky', 'earth')
for t in t:
    print t[0:4]

#define a function and have that value returned and printed in the shell.
def rosesAreRed():
    print('violets are blue')
    







