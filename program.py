class Solution(object):
    def findMatrix(self, nums):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        ans = []
        while True:
            sub = []
            for (key, val) in count.items():
                if val >= 1:
                    sub.append(key)
                    count[key] -= 1
            if len(sub) == 0:
                break
            ans.append(sub)
                
        return ans 

sl = Solution()
ans = sl.findMatrix([1,3,4,1,2,3,1])
print(ans)