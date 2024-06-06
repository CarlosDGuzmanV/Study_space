from typing import List


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numslen: int = len(nums)
        for i in range(0, numslen):
            for j in range(0, numslen):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]  # [1,2]

        return []


if __name__ == "__main__":
    solution = Solution()
    cas1 = [0, 4, 5, 8, 2, 7]
    target1 = 13  # [2,3]
    cas2 = [2, 3, 5, 6, 8, 9]
    target2 = 14  # [2,5]
    cas3 = [9, 8]
    target3 = 17  # [0,1]
    print(solution.twoSum(cas2, target2))
