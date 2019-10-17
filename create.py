import Base as base


# create a gist file
class TestClass:
    def test_create(self):
        new_gist = {
            "description": "Sample gist",
            "public": True,
            "files": {
                "hello_world.rb": {
                    "content": "Hello World"
                }
            }
        }
        base.create_gist(new_gist)