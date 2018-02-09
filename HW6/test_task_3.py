from task_3 import Widget


class TestWidget:

    def setup_method(self, string):
        self.luke = Widget("Luke")
        self.hansolo = Widget("Han Solo")
        self.leia = Widget("Leia")

    def test_add_dependency(self, *args):
        self.luke.add_dependency(self.hansolo, self.leia)
        assert self.luke.dependency == ["Han Solo", "Leia"]

