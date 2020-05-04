import os, sys

def arg_parser(args):
    try:
        old_ext = args[0]
        new_ext = args[1]
        return old_ext, new_ext

    except IndexError:
        print("Not enough arguments")
        print("ext2ext.py <current-extension> <new-extension>")
        sys.exit(0)

def file_renamer(old_ext, new_ext, dir_path="."):
    try:
        if (old_ext[0] != '.' or new_ext[0] != '.'):
            raise ValueError

        file_list = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(old_ext):
                    file_list.append(os.path.join(root, file))

        for file in file_list:
            new_file = file.replace(old_ext, new_ext)
            os.rename(file, new_file)
    except ValueError:
        print("Incorrect extension format")
        print("ext2ext.py <current-extension> <new-extension>")
        sys.exit(0)
    except Exception:
        print("Error: " + Exception)
        sys.exit(0)

if __name__ == "__main__":
    old_ext, new_ext = arg_parser(sys.argv[1:])
    file_renamer(old_ext, new_ext)
    sys.exit(0)
