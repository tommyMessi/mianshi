class Solution:
    def jump(self, nums:List[int]) -> int:
    # 定义最远位置，边界，步数
    max_pos = 0
    end = 0
    steps = 0
    for i in range(len(nums) - 1):
        # 获取最远可到达位置
        max_pos = max(max_pos, i + nums[i])
        # 到达边界时，更新边界
        # 同时跳跃次数加 1
        if i == end:
            end = max_pos
            steps += 1

    return steps

解题思路 https://blog.csdn.net/weixin_42664431/article/details/102648376
视频讲解 https://www.bilibili.com/video/BV1SA41147aU?from=search&seid=1873410207411184440