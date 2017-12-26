name = raw_input("What Linux release do you use?")

print "I also like", name, " - Linux rules...!"

#if else block

if True:
    print "hello panda"
else:
    print "next time"

raw_input("\n\n Press enter to exit the window")

#variable
count = 1000
marks = 34.5
name = "darsh"

print count
print marks
print name

#strings
str = 'hello world'
print str
print str[0]
print str[2:5]
print str[2:]
print str * 4
print str + ' from God'

#list
list = [1,2,3,4,'tom',1.2,'harry']
atlist = ['potter']
print list
print list + atlist

#tuples
tuple = ('ab','cd','ef')
tituple = ('gh','ij','kl')
print tuple + tituple

#dictionaries
dist = {'name' : 'jonny' , 'answer' : 'yes' , 'telling lies' : 'no'}
print dist.keys()
print dist.values()

#opreator
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
if ( a in list ):
    print "Line 1 - a is available in the given list"
else:
    print "Line 1 - a is not available in the given list"
if ( b not in list ):
    print "Line 2 - b is not available in the given list"
else:
    print "Line 2 - b is available in the given list"
a = 2
if ( a in list ):
    print "Line 3 - a is available in the given list"
else:
    print "Line 3 - a is not available in the given list"

#while loop

count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1
print "Good bye!"

#infinite loop
# var = 1
# while var == 1 :
#     num = raw_input("Enter a number:")
#     print "You entered: ", num
# print "Good bye!"

#for loop
for letter in 'Python':
    print 'Current Letter :', letter

fruits = ['banana', 'apple','mango']
for fruit in fruits:
    print 'Current fruit :', fruit
print "Good bye!"

