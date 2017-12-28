f = open('cities.json', 'r')
message = f.read()
str = 'Ahmedabad'
k=0

# if str in message:
#     print(" Ahmedabad is Matched in Cities")
# else:
#     print("No such string found,try again")
for city in message:
    if(city==str):
        print str
        print("Occurrences of the word:")
        k= k+1
f.close()


