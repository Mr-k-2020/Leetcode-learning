# _*_coding:utf-8_*_
# @Time    : 2020/10/24 15:26
# 方法一：动态规划
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        #创建dp，第i位置上的元素意为：覆盖0-i范围，需要多少个clips
        dp =[float('inf')]*(T+1)        #初始化dp，每个位置为无穷大
        dp[0] = 0                       #dp[0]=0
        for i in range(1,T+1):          #挨个修改dp每一位的值
            for clip in clips:          #遍历clips
                # 找到包含结束端点的视频片段
                if (clip[0] < i <= clip[1]):    #找到包含i的clip
                    # 缩小问题范围，求覆盖 (0 - clip[0]) 区间的视频的最小片段数量
                    dp[i] = min(dp[i], dp[clip[0]] + 1)       # dp[clip[0]] 表示覆盖0-clip[0]的片段数量，但是clip[0]-i这
                                                              # 部分还需要[clip[0],clip[1]]这个片段来覆盖，因此需要+1
        return -1 if (dp[T] == float('inf')) else dp[T]


# 方法二：贪心
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        maxn = [0] * T
        last = ret = pre = 0
        for a, b in clips:
            if a < T:
                maxn[a] = max(maxn[a], b)

        for i in range(T):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last

        return ret

