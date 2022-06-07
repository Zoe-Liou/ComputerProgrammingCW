#!/usr/bin/env python
# coding: utf-8

# # 2.1 The binary search tree class

# In[1]:


import random


# In[2]:


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def get_value(self):
        return self.value
        
    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left
    
    def set_value(self, value):
        self.value = value
    
    def set_right(self, value):
        self.right = value
    
    def set_left(self, value):
        self.left = value


# In[3]:


# code from https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
class BinarySearchTree:
    
    def __init__(self, node, max_size=None):
        self.max_size = max_size
        self.root = node
        
    def get_root(self):
        return self.root
    
    # return True if the tree is empty
    def is_empty(self, node):
        if self.get_size(node) == 0:
            return True
        else:
            return False
    
    # return True if the size of the treerfvt.  is equal or grater than the maximim size
    def is_full(self, node):
        if self.get_size(node) >= self.max_size:
            return True
        else:
            return False
    
    # print a visual representation of the tree
    # code from: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def print_tree(self, node, level=0):
        if node != None:
            self.print_tree(node.get_right(), level+1)
            print(' '*8*level + '-> ', node.get_value())
            self.print_tree(node.get_left(), level+1)

    # code from https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
    def insert(self, node, insert_value):
        
        # check if the the tree is full
        if self.is_full(node) == True:
            print('The list is full!')
        else:
            
            # if there is no root, return a new node
            if node is None:
                return TreeNode(insert_value)
            else:
                
                # input the same value
                if node.get_value() == insert_value:
                    side_list = ['left','right']
                    
                    # choose the side randomly
                    sides = random.choice(side_list)
                    if sides == 'right':
                        node.set_right(self.insert(node.get_right(), insert_value))
                    else:
                        node.set_left(self.insert(node.get_left(), insert_value))
                elif insert_value > node.get_value():
                        node.set_right(self.insert(node.get_right(), insert_value))
                else:
                    node.set_left(self.insert(node.get_left(), insert_value))
            return node
            
    # returns the values of the tree in ascending order
    def traverse(self, node):
        if node:
            self.traverse(node.get_left())
            print(node.get_value())
            self.traverse(node.get_right())
    
    
    # code from https://www.askpython.com/python/examples/binary-search-tree
    def search(self, node, search_value):

        if node == None:
            return False
        
        elif node.get_value() == search_value:
            return True

        elif node.get_value() < search_value:
            return self.search(node.get_right(), search_value)

        else:
            return self.search(node.get_left(), search_value)
        
    # search tree, return the node
    # with minimum key value
    # code from https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/?ref=lbp
    def min_value(self, node):
        current_node = node

        # find the left most leaf
        while(current_node.get_left() is not None):
            current_node = current_node.get_left()

        return current_node

    # given a binary search tree and a value, this function
    # delete the value and returns the new root
    # code from https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/?ref=lbp
    def delete(self, node, delete_value):
        
        # check if the tree is empty
        if self.is_empty(node) == True:
            return ('The list is empty! Please insert values.')
        
        else:
            # root
            if node is None:
                return node
            
            # if the value is greater than the root's value
            # to the right sub-tree
            if delete_value > node.get_value():
                node.set_right(self.delete(node.get_right(), delete_value))

            elif(delete_value < node.get_value()):
                node.set_left(self.delete(node.get_left(), delete_value))

            # if value is same as root's value, then delete
            else:

                # node with one child on the left or no child
                if node.get_left() is None:
                    node_temp = node.get_right()
                    node = None
                    return node_temp

                elif node.get_right() is None:
                    node_temp = node.get_left()
                    node = None
                    return node_temp

                # with two children
                # get the inorder successor
                # (smallest in the right subtree)
                node_temp = self.min_value(node.get_right())
                
                # copy the inorder successor's
                # content to this node
                node.set_value(node_temp.get_value())

                # delete the inorder successor
                node.set_right(self.delete(node.get_right(), node_temp.get_value()))

            return node
        
    @staticmethod
    # code from https://www.geeksforgeeks.org/write-a-c-program-to-calculate-size-of-a-tree/
    def get_size(node):
        if node is None:
            return 0
        else:
            return (BinarySearchTree.get_size(node.get_left()) + 1 + BinarySearchTree.get_size(node.get_right()))
