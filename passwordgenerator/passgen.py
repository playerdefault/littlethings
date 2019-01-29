import json, random, click

@click.command()
@click.option('--complex', default=0, help='Password complexity switch')
def passgen(complex):
    with open('words.json') as json_data:
        words = json.load(json_data)
        
    word_list = words["data"]

    pos1 = random.randrange(len(word_list))
    string1 = word_list[pos1]

    pos2 = random.randrange(len(word_list))
    string2 = word_list[pos2]

    pos3 = random.randrange(len(word_list))
    string3 = word_list[pos3]

    if (complex == 0):
        final = string1 + ' ' + string2 + ' ' + string3
        print(final)
    elif (complex == 1):
        num1 = '_' + str(random.randrange(100)) + '_'
        num2 = '_' + str(random.randrange(100)) + '_'
        num3 = '_' +  str(random.randrange(100))

        final = string1 + num1 + string2 + num2 + string3 + num3
        print(final)
    else:
        print("Wrong parameter")

if __name__ == '__main__':
    passgen()
