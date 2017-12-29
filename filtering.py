import json

f = open('cities.json', 'r')
message = f.readlines()
str = 'Ahmedabad'
k=0

# if str in message:
#     print(" Ahmedabad is Matched in Cities")
# else:
#     print("No such string found,try again")
for city in message:
    if str in city:
        k = k+1
f.close()
print(k)

# str = 'Ahmedabad'
# k = 0
# with open('gujarat.json', 'r') as f:
#     items = json.load(f)
#
# for item in items:
#     if item['c'].lower() == str.lower():
#         k = k + 1
#
# print(k)