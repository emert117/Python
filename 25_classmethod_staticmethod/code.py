class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")




# instance method call
test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)

# class method call
ClassTest.class_method()

# static method
ClassTest.static_method()
