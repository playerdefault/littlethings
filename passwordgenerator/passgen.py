import json, random, click

with open('words.json') as json_data:
    words = json.load(json_data)
    
word_list = words["data"]

# create the password

pos1 = random.randrange(len(word_list))
string1 = word_list[pos1]

pos2 = random.randrange(len(word_list))
string2 = word_list[pos2]

pos3 = random.randrange(len(word_list))
string3 = word_list[pos3]

final = string1 + ' ' + string2 + ' ' + string3
print(final)
