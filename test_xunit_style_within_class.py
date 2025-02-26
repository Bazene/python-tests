# @classmethod : Python decorator that is used to define a method that belongs to the class rather than an instance of the class.
# "cls" refers to the class itself
# "self" refers to an instance


class TestClass:
    @classmethod
    def setup_class(cls):
        print("************************* Setup Class! *************************")

    @classmethod
    def teardown_class(cls):
        print(" ************************* Teardown Class! *************************")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1!")
        elif method == self.test2:
            print("\nSetting up test2!")
        else:
            print("\nSetting up unknown test!")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down up test1!")
        elif method == self.test2:
            print("\nTearing down up test2!")
        else:
            print("\nTearing down up test!")

    def test1(self):
        print("Executing test1!")
        assert True

    def test2(self):
        print("Executing test2!")
        assert True
