import Base as base
from Constants import ID


class TestClass:
    # select and change name of a gist file
    def test_edit_file_rename(self):

        file_name_to_be_changed = "lorem.txt"
        new_file_name = "lorem_updated_file.txt"
        update = {
            "files": {
                file_name_to_be_changed: {
                    "filename": new_file_name
                }
            }
        }

        updated_file_name = False
        gist_obj = base.get_gist(ID)
        files = gist_obj['files']
        for f in files:
            f_name = files[f]['filename']
            if f_name == file_name_to_be_changed:
                base.update_gist(ID, update)
                updated_file_name = True
                break

        assert updated_file_name, "File not found and hence was not renamed"
