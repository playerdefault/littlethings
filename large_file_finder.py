import os, sys

def large_file_list_gen(dir_path="."):
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file_lengthy(os.path.join(root, file))>300:
                file_list.append(os.path.join(root, file))

    return file_list
    

def file_lengthy(fname):
    file = open(fname, 'r')
    counter = 0
    content = file.read()
    colist = content.split('\n')
    for i in colist:
        if i:
            counter += 1
    return counter


if __name__ == "__main__":
    output = large_file_list_gen(r'./area/multi-quote/')
    for file_name in output:
        print(file_name)
    print(len(output))
