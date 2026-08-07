class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        st = []
        for i in range(len(nums2)-1, -1, -1):
            while len(st) > 0 and st[-1] <= nums2[i]:
                st.pop()
            if len(st) == 0:
                res[nums2[i]] = -1
            else:
                res[nums2[i]] = st[-1]
            st.append(nums2[i])

        return list(map(lambda x:res[x], nums1))
