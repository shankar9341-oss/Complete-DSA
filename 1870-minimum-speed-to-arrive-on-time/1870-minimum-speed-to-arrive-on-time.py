class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        right = 10 ** 7
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if self.speedcatch(dist,hour,mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
    
    def speedcatch(self,dist,hour,speed):
        time = 0.0
        for i in range(len(dist)):
            t = dist[i] // speed
            if i != len(dist)-1:
                time += math.ceil(dist[i] / speed)
            else:
                time += dist[i] / speed
        return time <= hour