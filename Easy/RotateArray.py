# Solution - 1 Using Slicing
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k% len(nums)
        nums[:]=nums[len(nums)-k:] + nums[:len(nums)-k]