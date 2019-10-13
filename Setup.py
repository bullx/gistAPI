import Base as base
from Constants import ID


def test_setup_module():
    # This setup creates test files
    update = {
        "description": "Test files",
        "public": 'true',
        "files": {
            "abc.txt": {
                "content": "haha"
            },
            "def.txt": {
                "content": "lol"
            },
            "lorem.txt": {
                "content": "hehe"
            },
            "ipsum.txt": {
                "content": "rofl"
            }
        }
    }
    base.create_files_in_gist(ID, update)
