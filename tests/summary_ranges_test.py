import pytest
from myproj import solution


@pytest.mark.parametrize("nums, answer", [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    ])
def test_myclass(nums, answer):
    my_obj = solution.Solution()
    assert my_obj.summaryRanges(nums) == answer
