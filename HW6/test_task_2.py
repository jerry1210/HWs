from task_2 import Circle


class TestCircle:

    def setup_method(self):
        self.circle = Circle(3)

    def test_area(self):
        assert round(self.circle.area()) == 28

    def test_perimeter(self):
        assert round(self.circle.perimeter()) == 19

