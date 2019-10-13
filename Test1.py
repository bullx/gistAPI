import Base as base
from Constants import ID


class TestClass:
    # read a gist with a valid gist id and print all files in it
    def test_read_1(self):
        gist_obj = base.get_gist(ID)
        files = gist_obj['files']
        print("Owner name :" + str(gist_obj['owner']['login']))
        print("File names and contents are ")
        for f in files:
            msg = files[f]['filename'] + " : " + files[f]['content']
            print(msg)









