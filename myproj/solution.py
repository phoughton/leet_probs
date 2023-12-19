class Solution(object):
    def summaryRanges(self, nums: list[int]) -> list[str]:
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        response = []
        current_range = []

        # Add dummy entry, lower than all others, that allows final ranges to work.
        nums.append(nums[0]-1)

        for index, item in enumerate(nums):

            if len(current_range) == 0:
                # No Existing range
                current_range.append(item)
            else:
                # Existing range exists
                if item-1 == current_range[-1]:
                    # The Item is Consecutive
                    current_range.append(item)
                else:
                    # Not Consecutive
                    # Output varies depending on length of current range
                    if len(current_range) == 1:
                        response.append(f"{current_range[0]}")
                    else:
                        response.append(f"{current_range[0]}->{current_range[-1]}")

                    # Reset the current range
                    current_range = []
                    current_range.append(item)

        return response
