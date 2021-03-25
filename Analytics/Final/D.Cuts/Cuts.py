#!/usr/bin/env python
# coding: utf-8

# In[17]:


def compatible_cuts(nums):
    temp = []
    for elem in nums:
        temp.append([elem[0], -(elem[2]+1)])
        temp.append([elem[1], (elem[2]+1)])
    temp = sorted(temp)
    for i in range(len(temp)):
        temp[i] = temp[i][1]
    colours = 0
    stack = []
    for i in range(len(temp)):
        if temp[i] < 0:
            if colours != 0:
                if colours > 0 and colours == -temp[i]:
                    stack.append(temp[i])
                else:
                    print("NO")
                    stack.append('no')
                    break
            else:
                stack.append(temp[i])
        if temp[i] > 0:
            if stack[-1] == -temp[i]:
                if colours  == 0 or colours == temp[i]:
                    colours = temp[i]
                else:
                    colours = -1
                stack.pop()
            else:
                print("NO")
                stack.append('no')
                break
    if len(stack) == 0:
        print("YES")

with open('input.txt') as f:
    nums = f.readlines()
matrix = [[int(num) for num in line.split()] for line in nums]
length = int(matrix[0][0])
nums = matrix[1:]

compatible_cuts(nums)

