# f = open('helloworld.txt', 'r')
# message = f.read()
# print "Before coverstion: ", message
# print "After coverstion : ", message.upper()
# f.close()
#

with open('helloworld.txt', 'r') as f:
    content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.upper() for x in content]

with open('helloworld.txt', 'w') as f:
    for line in content:
        f.write(line)
