import Base as base
from Constants import ID


def test_teardown_module():
    # This will delete setup files
    gist_obj = base.get_gist(ID)
    files = gist_obj['files']
    for f in files:
        file_name = files[f]['filename']
        update = {
            "files": {
                file_name: None
            }
        }
        base.update_gist(ID, update)
