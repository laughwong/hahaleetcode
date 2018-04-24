class Solution:
	def twoSum(self,nums,target):
		ret = []
		num_len = len(nums)
		i = 0

		while(i < num_len):
			j = i + 1
			while(j < num_len):
				sum_t = nums[i] + nums[j]
				if(sum_t == target):
					ret.append(i)
					ret.append(j)
					return ret
				else:
					pass
				j = j + 1	
			i = i + 1