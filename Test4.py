import Base as base
from Constants import ID


class TestClass:
    # select and change content of gist file
    def test_edit_file_content(self):

        file_name = "ipsum.txt"
        new_content = "updated the contents"
        update_content = {
            "files": {
                file_name: {
                    "content": new_content
                }
            }
        }
        gist_obj = base.get_gist(ID)
        files = gist_obj['files']
        content_updated = False
        for f in files:
            f_name = files[f]['filename']
            if f_name == file_name:
                base.update_gist(ID, update_content)
                content_updated = True
                break

        assert content_updated, "File not found. Content not updated"




