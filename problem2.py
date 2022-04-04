
## Problem2 Next Greater Element II 
# (https://leetcode.com/problems/next-greater-element-ii/)


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        #store the stack elements with the top element being the first elment of the stack
        stack = []
        for num in nums[::-1]:
            stack.append(num)
            
        output = []
        for idx in range(n-1, -1, -1):
            num = nums[idx]
            
            #while stack is not equal to 0
            while len(stack) != 0:
                #if the stack's top element is greater than num, break out of the loop
                if stack[-1] > num:
                    break
                #keep popping the element
                stack.pop()
            
            #if the stack is 0
            if len(stack) == 0:
                output.append(-1)
            else:
            #if the stack is not zero, add the stack's top elment
                output.append( stack[-1] )
            stack.append(num)
        return output[::-1]
            