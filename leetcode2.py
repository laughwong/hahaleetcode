class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution:
	def insertList(self,lists,values):
		node = ListNode(values)
		node.next = lists
		return node

	def getNumber(self,lists):
		tmp = 0
		ret_number = 0
		ten = 1
		j = 0
		datas = 0
		while(lists):
			for x in range(0,j):
				ten = ten * 10
			datas = lists.val
			tmp = datas * ten
			ret_number = ret_number + tmp
			lists = lists.next
			j = j + 1
			ten = 1

		return ret_number

	def numberToList(self,nums):
		tmp = 0
		ret = []
		tmp_node = 0
		ret_list = False
		if(nums == 0):
			return ListNode(nums)
		else:
			while(nums):
				tmp = nums % 10
				nums = nums / 10
				ret.append(tmp)

			while(ret):
				tmp_node = ret.pop()
				if(ret_list == False):
					ret_list = ListNode(tmp_node)
				else:
					ret_list = self.insertList(ret_list,tmp_node)

		return ret_list

	def addTwoNumbers(self,l1,l2):
		num1 = 0
		num2 = 0
		ret_number = 0
		num1 = self.getNumber(l1)
		num2 = self.getNumber(l2)
		ret_number = num1 + num2
		return self.numberToList(ret_number)



s = Solution()

a = ListNode(0)


b = ListNode(0)


result = s.addTwoNumbers(a,b)

print result.val
