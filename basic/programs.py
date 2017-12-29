def printme( str ):
    print str
    return
printme("first")
printme("second")

# def printme( str ):
#     print str
#     return
# printme()

def printme( str ):
    print str
    return
printme(str = 'my world')

def biodata(name,age,gender):
    print "Name : " ,name
    print "Age :" ,age
    print "Gender :" ,gender
    return
biodata(name='Mahadev',age='infinit',gender='male')

#default argument
def biodata( name,gender,age= 'infinite' ):
    print "Name : " ,name
    print "Age :" ,age
    print "Gender :" ,gender
    return
biodata( name='Mahadev',age=35, gender='male' )
biodata( name='Mahadev',gender='male' )

#variable length argument
def printinfo (arg , *vartuples):
    print 'Output is: '
    print arg
    for var in vartuples:
        print var
    return
printinfo( 10 )
printinfo (100,90,80)

def sum( arg1, arg2 ):
    total = arg1 + arg2
    print "Inside the function : ", total
    return total
total = sum( 10, 20 )
print "Outside the function : ", total

#local and global variable
total = 0
def sum( arg1, arg2 ):
    total = arg1 + arg2; 
    print "Inside the function local total : ", total
    return total
sum( 10, 20 )
print "Outside the function global total : ", total





