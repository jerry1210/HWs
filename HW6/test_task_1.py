from task_1 import Rectangle


class Setup:
   def setup_method(self):
       self.rectangle = Rectangle(6, 3)

class TestRectangle(Setup):

    def test_area(self):
        assert self.rectangle.area() == 18

