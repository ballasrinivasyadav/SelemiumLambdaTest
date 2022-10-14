import pytest

from TestScenario2.dragDrop import DragDrop


@pytest.mark.usefixtures
class TestTwo:

    def test_two(self, setup):
        dragDrop = DragDrop(self.driver)
        dragDrop.getDragDrop()

        dragDrop.getSlider()
