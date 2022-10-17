#TimeComplexity: O(1)
#SpaceComplexity: O(1)
class MyHashMap(object):
    class ListNode:
        def __init__(self,key,val):
            self.key = key # creating key for the listnode
            self.val = val # creating val for the listnode
            self.next = None # creating next pointer for the listnode and assigning value as None
            
    def __init__(self):
        self.primary = [None] * 100 # creating primary array with none value for the length

    def hashindex(self,key):
        return key%100 # generating hashkey
    
    def findNode(self,head,key):
        curr = head # assigning curr pointer to head
        prev = None # assigning prev pointer to None
        
        while curr!=None and curr.key != key: # if curr pointer is not null and curr pointer value is not equal to key
            prev=curr # assigning prev pointer to curr
            curr=curr.next # assigning curr pointer to next value of curr
        return prev # returning prev
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_index=self.hashindex(key) # storing the hashkey
        
        if self.primary[hash_index] == None: # if primary array is empty
            self.primary[hash_index] = self.ListNode(-1,-1) # assigning the seconadary linked list with values -1,-1
        prev = self.findNode(self.primary[hash_index],key) # finding the node in primary array and storing the key value in prev
        
        if prev.next == None: # if next value of prev is None
            prev.next = self.ListNode(key,value) # creating the listnode and insert the value
            
        else: # if next value of prev is not None
            prev.next.val = value # assign value to next of prev pointer's val

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hash_index=self.hashindex(key) # storing the hashkey
        
        if self.primary[hash_index] == None: # if primary array is empty
            return -1 
        
        prev = self.findNode(self.primary[hash_index],key) # finding the node with the key in primary array
        if prev.next == None: # if next of prev is None
            return -1
        else:
            return prev.next.val # return next of prev pointer's val 

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_index=self.hashindex(key) # storing the hashkey
        if self.primary[hash_index] == None: # if primary array is empty
            return
        prev = self.findNode(self.primary[hash_index],key) # finding the node with the key in primary array
        
        if prev.next == None: # if next of prev is None
            return None
        else:
            prev.next = prev.next.next # assign next of prev pointer to next of next of prev pointer


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
