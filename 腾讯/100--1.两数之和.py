#用字典模拟哈希求解

#参考了大神们的解法，通过哈希来求解，这里通过字典来模拟哈希查询的过程。
#个人理解这种办法相较于方法一其实就是字典记录了 num1 和 num2 的值和位置，而省了再查找 num2 索引的步骤。

def twoSum(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]

#视频讲解 https://www.bilibili.com/video/BV1rv411k7VY?from=search&seid=1860860796779553733