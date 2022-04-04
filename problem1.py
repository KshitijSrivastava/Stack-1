## Problem1 Daily Temperatures 

# (https://leetcode.com/problems/daily-temperatures/)



class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = []
        stack = []
        
        for idx in range(n-1, -1, -1):
            num = temperatures[idx]
            #print(idx, num)
            
            #while stack is not empty
            while len(stack) != 0:
                #if stack's top value is more than the current value
                #break out of while loop
                if stack[-1].value > num:
                    break
                #else keep popping thr stack
                stack.pop()
            
            #if stack is empty then no temp more than the current temp
            if len(stack) == 0:
                output.append(0)
            else:
                #find the difference in the index
                output.append(stack[-1].index - idx)
            stack.append( Node(num, idx) )
            
        return output[::-1]