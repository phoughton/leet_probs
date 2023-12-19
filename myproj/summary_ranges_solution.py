class SummaryRangesSolution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        response = []
        curr_range = []

        # Add dummy entry, lower than all others,
        # that allows final ranges to work.
        nums.append(nums[0]-1)

        for item in nums:

            if len(curr_range) == 0:
                # No Existing range
                curr_range.append(item)
            else:
                # Existing range exists
                if item-1 == curr_range[-1]:
                    # The Item is Consecutive
                    curr_range.append(item)
                else:
                    # Not Consecutive
                    # Output varies depending on length of current range
                    if len(curr_range) == 1:
                        response.append(f"{curr_range[0]}")
                    else:
                        response.append(f"{curr_range[0]}->{curr_range[-1]}")

                    # Reset the current range
                    curr_range = []
                    curr_range.append(item)

        return response
