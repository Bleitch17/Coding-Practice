class Solution:
    def get_min_operations(self, nums: list[int]) -> int:
        zero_elements: set[int] = set()
        seen_elements: set[int] = set()

        cur, prev = 0, 0

        for i in range(1, len(nums)):            
            cur = 0 if nums[i] in zero_elements else nums[i]
            prev = 0 if nums[i - 1] in zero_elements else nums[i - 1]

            if cur >= prev:
                seen_elements.add(nums[i - 1])
                continue

            # At this point, the current element is smaller than the previous one,
            # so need to zero out all the elements seen so far.
            seen_elements.add(nums[i - 1])
            zero_elements |= seen_elements

        return len(zero_elements)
