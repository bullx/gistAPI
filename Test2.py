import Base as base


class TestClass:
    # give an Invalid gist id and it should return 404
    # not found error
    def test_read_2(self):
        id = "45454444444"
        response = base.get_gist(id)
        assert response == 404
