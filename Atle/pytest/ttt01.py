import pytest

@pytest.fixture(scope="class")
def myfixture():
    print("执行myfixture")

class Test_firstFile():

    # @pytest.mark.usefixtures("myfixture")
    def test_one(self):
        print("执行test_one")
        assert 1+1 == 3

    # @pytest.mark.usefixtures("myfixture")
    def test_two(self, myfixture):
        print("执行test_two")
        assert 1 == 1

    # @pytest.mark.usefixtures("myfixture")
    def test_three(self, myfixture):
        print("执行test_three")
        assert 1+1 == 2


if __name__ == "__main__":
    pytest.main(['-s', 'test_01.py'])


