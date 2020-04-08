import os
file_list = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".js"):
            file_list.append(os.path.join(root, file))


for file in file_list:
    new_file = file.replace('.js', '.tsx')
    os.rename(file, new_file)
