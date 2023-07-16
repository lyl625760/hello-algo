"""
File: binary_search_recur.py
Created Time: 2023-07-17
Author: krahets (xisunyy@163.com)
"""


def dfs(nums: list[int], target: int, i: int, j: int) -> int:
    """二分查找：分治"""
    # 若区间为空，代表未找到目标元素，则返回 -1
    if i > j:
        return -1
    # 计算中点索引 m
    m = (i + j) // 2
    if nums[m] < target:
        # 此情况说明 target 在区间 [m+1, j] 中，递归解决该子问题
        return dfs(nums, target, m + 1, j)
    elif nums[m] > target:
        # 此情况说明 target 在区间 [i, m-1] 中，递归解决该子问题
        return dfs(nums, target, i, m - 1)
    else:
        # 找到目标元素，返回其索引
        return m


def binary_search(nums: list[int], target: int) -> int:
    """二分查找"""
    n = len(nums)
    return dfs(nums, target, 0, n - 1)


"""Driver Code"""
if __name__ == "__main__":
    target = 6
    nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]

    # 二分查找（双闭区间）
    index: int = binary_search(nums, target)
    print("目标元素 6 的索引 = ", index)
