class Solution(object):
    def lengthOfLongestSubstring(self, s):
		lens = len(s)
		i = 0
		ret = []
		for x in range(0,lens):
			if(ret.count(s[x])>0):
				pass
			else:
				ret.append(s[x])

		print ret



s = Solution()
s.lengthOfLongestSubstring("wanglin")