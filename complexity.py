#!/usr/bin/env python
# coding: utf-8

# # 2.3 Random trees’ simulation

# In[1]:


from binarysearchtree import TreeNode, BinarySearchTree
from linkedlist import ListNode, LinkedList
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import sympy
import math


# In[2]:


def random_tree(n):
    
    # generate a size n integer list
    int_list = list(np.random.randint(1, 1000, size=n))
    
    # first number in the list as the root for the BST
    root = TreeNode(int_list[0])
    tree = BinarySearchTree(root, max_size=n)
    for i in range(n-1):
        tree.insert(root, int_list[i+1])
    return tree


# In[3]:


def random_list(n):
    
    # generate a size n integer list
    int_list = list(np.random.randint(1, 1000, size=n))
    
    # first number in the list as the head for the linked list
    head = ListNode(int_list[0])
    link_list = LinkedList(head, max_size=n)
    for i in range(n-1):
        link_list.insert(int_list[i+1])
    return link_list


# In[4]:


# generate binary search tree size and linked list size
X = list(np.arange(5, 101, 5))


# In[5]:


print(X)


# In[6]:


# complexity for BST
trees = 1000
Y = []
for i in X:
    ran_list = []
    
    # for each size, build 1000 trees
    for j in range(trees):
        ran_list.append(random_tree(i))
        
    start_time = time.time()
    for item in ran_list:
        item.search(item.get_root(), 42)
    elapsed_time = time.time() - start_time
    
    # average time
    Y.append(elapsed_time/trees)
print(Y)


# In[7]:


# Complexity analysis X vs Y
# the shape of the binary search tree is 
# much close to a logarithmic relationaship.
# the time increases along with the the size of the tree
# but its marginal search time decreases when the size of tree is
# greater than 0.5.
plt.plot(X, Y)
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()


# In[8]:


# complexity for LinkedList
trees = 1000
Y4 = []
for i in X:
    ran_list = []
    
    # for each size, build 1000 linked lists
    for j in range(trees):
        ran_list.append(random_list(i))
        
    start_time = time.time()
    for item in ran_list:
        item.search(42)
    elapsed_time = time.time() - start_time
    Y4.append(elapsed_time/trees)
print(Y4)


# In[9]:


# Complexity analysis X vs Y4
# the shape of the linked list is 
# a linear relationaship
# it is a 45-degree line which means that the searching time
# increases when the size increases.
plt.plot(X, Y4)
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()


# In[20]:


# linear relationship
# t = c * n + b
c = sympy.symbols("c")
b = sympy.symbols("b")

n_5 = Y[0]
n_10 = Y[1]
y2_ans = sympy.solve([c*5+b-n_5, c*10+b-n_10], [c, b])
print(y2_ans)


# In[16]:


Y2 = []
c = y2_ans[c]
b = y2_ans[b]
for item in X:
    a = c * item + b
    Y2.append(a)


# In[12]:


# logarithmic relationship
# t = c∗log(n)+b
# use log(n) = log2(n)
c2 = sympy.symbols("c2")
b2 = sympy.symbols("b2")

log_5 = math.log(n_5,2)
log_10 = math.log(n_10,2)

y3_ans = sympy.solve([c2* log_5 +b2-n_5, c2*log_10+b2-n_10], [c2, b2])
print(y3_ans)


# In[13]:


Y3 = []
c2 = y3_ans[c2]
b2 = y3_ans[b2]
for item in X:
    a = c * math.log(item,2) + b
    Y3.append(a)


# In[21]:


# Complexity analysis X vs Y, Y2 and Y3
# compared to linear and logarithmic, the initial graph lies
# between the two lines but it is closer to a logarithmic relatiobaship.
# the main reason for the difference between Y and Y3 could be the balance
# of the tree. If the tree could have larger size, without duplicate values, 
# or be more balanced, e.g. using different way to decide the node side,
# then the Y might be closer to Y3.
# compared to binary search tree, Linked list is a linear relationship,
# which means the search time increases along with the size.
plt.plot(X, Y)
plt.plot(X, Y2)
plt.plot(X, Y3)
plt.plot(X, Y4)
plt.legend(['BST','Linear','Logarithmic', 'LL'])
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()


# In[ ]:




