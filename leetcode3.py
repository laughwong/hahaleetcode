class Solution(object):
	def lengthOfLongestSubstring(self,s):
		i = 0
		j = 0
		strlen = len(s)
		left = []
		right = []
		str = []
		ret = []
		tmp = []
		flag = 0

		for x in range(0,strlen):
			if str.count(s[x]) > 0:
				if len(str)>len(ret):
					ret = str
				left = []
				right = []
				j = len(str)
				flag = 0
				for k in range(0,j):
					if(str[k] == s[x]):
						left.append(str[k])
						flag = 1
					else:
						if flag == 0:
							left.append(str[k])
						else:
							right.append(str[k])

				right.append(s[x])
				if len(left)>len(right):
					tmp = left
				else:
					tmp = right
				if len(tmp)>len(ret):
					ret = tmp
				str = []
				str = right
			else:
				str.append(s[x])
				i += 1
		if len(str) > len(ret):
			ret = []
			ret = str
		return len(ret)


s = Solution()
print s.lengthOfLongestSubstring("abcabcbb")
# abcabcbb  bbb  pwwkew jbpnbwwd
