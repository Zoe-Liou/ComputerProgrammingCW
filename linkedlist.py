#!/usr/bin/env python
# coding: utf-8

# # 2.5 The linked list class

# In[1]:


class ListNode:
    
    # define the node value and connect to the next item
    def __init__(self, value, nextitem=None):
        self.value = value
        self.nextitem  = nextitem
    
    def get_value(self):
        return self.value    


# In[66]:


class LinkedList:
    
    def __init__(self, node, max_size=None):
        self.node = node
        
        # the maximum size of the linked list
        self.max_size = max_size
        
    def get_node(self):
        return self.node
    
    # print a visual representation of the linked list
    def __str__(self):
        temp_node = self.get_node()
        vis_str = ""
        
        # if the next itrm of the current node exists
        while temp_node.nextitem is not None:
            vis_str += str(temp_node.get_value()) + " -> "
            temp_node = temp_node.nextitem
        
        # print the last node
        vis_str = vis_str + str(temp_node.get_value())
        return vis_str
    
    # return the value of node in the linked list order
    # code from https://stackoverflow.com/questions/26445654/how-to-traverse-linked-lists-python/26446934
    def traverse(self):
        temp_node = self.get_node()
        while temp_node.nextitem is not None:
            print(temp_node.get_value())
            temp_node = temp_node.nextitem
        
        # print the last node
        print(temp_node.get_value())
    
    # return the length of the linked list
    # code from https://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/
    def count_size(self):
        
        # get a temporary node
        temp_node = self.get_node()
        
        # given the count = 0 
        count = 0
        while temp_node:
            count += 1
            temp_node = temp_node.nextitem
        return count
    
    # return True if the linked list is empty
    def is_empty(self):
        if self.count_size() == 0:
            return True
        else:
            return False
    
    # return True if the length is equal or grater than the maximim size
    def is_full(self):
        if self.count_size() >= self.max_size:
            return True
        else:
            return False
    
    # code from https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/
    def search(self, search_value):
        
        # search from the first node until the value of current
        # node is equal to the value we specify
        first_node = self.get_node()
        while first_node is not None:
            if first_node.get_value() == search_value:
                return True
            first_node = first_node.nextitem
        
        # return False if the value does not exist
        return False
        
    # code from https://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/
    def insert(self, new_value):
        first_node = self.get_node()
        
        # check if the linked list is full
        if self.is_full() == True:
            return ('The list is full!')
        else:
            
            # insert the new value at the end of the list
            # and connect to the last node
            while first_node.nextitem is not None:
                first_node = first_node.nextitem
            new_node = ListNode(new_value)
            first_node.nextitem = new_node
    
    # code from https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/?ref=lbp
    def delete(self, del_value):
        
        # check if the list is empty
        if self.is_empty() == True:
            return ('The list is empty! Please insert new values.')
        else:
            temp_node = self.get_node()
            # If first node has the value that we want to delete
            if temp_node is not None:
                if temp_node.get_value() == del_value:
                    self.node = temp_node.nextitem
                    temp_node = None
                    return
            
            # keep searching for the value untill the current node value
            # is equal to the value to be deleted
            while temp_node is not None:
                if temp_node.get_value() == del_value:
                    break
                pre_node = temp_node
                temp_node = temp_node.nextitem
            
            # if value is not in the linked list 
            if temp_node == None:
                return
            
            # unlink the node from the list
            pre_node.nextitem = temp_node.nextitem
            temp_node = None

 