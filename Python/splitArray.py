Split Array Largest Sum - (Dynamic Programming)

Problem Statemet: Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.

Code:
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def splitPart(arr, cap):
            k = 1
            caps = 0
            for i in range(len(arr)):
                if caps + arr[i] <= cap:
                    caps += arr[i]
                else:
                    k += 1
                    caps = arr[i]

            return k

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low+ high) // 2
            sp = splitPart(nums, mid)

            if sp > k:
                low = mid + 1
            else:
                high = mid - 1

        return low
