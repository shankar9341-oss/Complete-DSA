class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        low = nums[0]
        up = nums[0]
        ans = []
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                if low == up:
                    ans.append(str(low))
                else:
                    ans.append(f"{low}->{up}")
                low = nums[i]
            up = nums[i]
        
        if low == up:
            ans.append(str(low))
        else:
            ans.append(f"{low}->{up}")
        return ans