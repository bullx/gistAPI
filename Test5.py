import Base as base
from Constants import ID


class TestClass:
    # This will delete the file present in the gist
    def test_delete_single_file_from_gist(self):

        file_name = "def.txt"
        updated_gist = {
            "files": {
                file_name: None
            }
        }
        gist_obj = base.get_gist(ID)
        files = gist_obj['files']
        file_deleted = False
        for f in files:
            f_name = files[f]['filename']
            if file_name == f_name:
                base.update_gist(ID, updated_gist)
                file_deleted = True
                break

        assert file_deleted, "No file found to be deleted"
