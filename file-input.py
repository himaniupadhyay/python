f = open('helloworld.txt', 'r')
message = f.read()
print "Before coverstion: ", message
print "After coverstion : ", message.upper()
f.close()

