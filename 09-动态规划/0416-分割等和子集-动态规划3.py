from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # 物品的数量
        l = len(nums)
        if l == 0:
            return False

        s = sum(nums)
        if s & 1 == 1:
            return False

        # 二维 dp 问题：背包的容量
        half = s // 2
        # print(half)

        dp = [False for _ in range(half + 1)]

        # 其实使用一维数组就可以了
        # 先写第 1 行：看看第 1 个数是不是能够填满这个背包

        # 添加了这个设置
        dp[0] = True

        for i in range(1, half + 1):
            dp[i] = False if nums[0] != i else True
        # i 表示物品索引
        for i in range(1, l):
            # j 表示容量
            for j in range(half, -1, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j - nums[i]]

            if dp[-1]:
                return True
        # for item in dp:
        #     print(item)
        return dp[-1]


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    # nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    # nums = [91, 29, 92, 14, 53, 27, 96, 97, 58, 76, 56, 51, 68, 18, 37, 98, 30, 37, 25, 65, 95, 22, 34, 25, 29, 37, 54,
    #         34, 43,
    #         18, 65, 31, 21, 91, 9, 57, 13, 72, 31, 26, 36, 77, 85, 70, 5, 72, 93, 39, 46, 50, 22, 16, 6, 67, 17, 41, 42,
    #         10,
    #         56, 66, 69, 53, 79, 46, 14, 34, 80, 31, 86, 78, 35, 64, 75, 88, 58, 26, 56, 91, 84, 38, 44, 19, 49, 8, 4,
    #         78, 11,
    #         13, 10, 56, 72, 97, 25, 62, 97, 80, 20, 63, 5, 27]
    s = Solution()
    res = s.canPartition(nums)
    print(res)
