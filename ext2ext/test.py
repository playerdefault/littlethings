import os, unittest, shutil
import ext2ext

class TestProperWorking(unittest.TestCase):
    
    def setUp(self):
        i = 0
        while i <= 100:
            open("testfile" + str(i) + ".js", 'w')
            i += 1
        os.mkdir("subdir1")
        i = 0
        while i <=20:
            open(os.path.join("subdir1", "innertestfile" + str(i) + ".js"), 'w')
            i += 1

    def test_arg_parser(self):
        test_args = [".js", ".ts"]
        old_ext, new_ext = ext2ext.arg_parser(test_args)
        self.assertEqual(old_ext, test_args[0])
        self.assertEqual(new_ext, test_args[1])

    def test_file_renamer_in_cwd(self):
        test_args = {
            "old_ext":".js",
            "new_ext": ".ts",
            "subdir": "subdir1"
            }
        ext2ext.file_renamer( test_args["old_ext"], test_args["new_ext"], test_args["subdir"] )
        for root, dirs, files in os.walk(test_args["subdir"]):
            for file in files:
                self.assertEqual(file[-3:], ".ts")

    def tearDown(self):
        i = 0
        while i <= 100:
            os.remove("testfile" + str(i) + ".js")
            i += 1
        shutil.rmtree('subdir1')

if __name__ == '__main__':
    unittest.main()