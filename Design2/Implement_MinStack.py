# TimeComplexity: O(n)
# Space Complexity: O(1)
class MinStack(object):

    def __init__(self):
        self.stack = [] # creating first stack
        self.minstack = [] # creating second stack for storing min values

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val) # appending val in first stack
        if len(self.minstack) == 0: # if minstack is empty
            self.minstack.append(val) # appending val in minstack
        else: # if minstack is not empty
            if val <= self.minstack[-1]: # if appending value is less than the last element in minstack
                self.minstack.append(val) # appending val in minstack

    def pop(self):
        """
        :rtype: None
        """
        if self.minstack[-1]==self.stack[-1]: # if last value in minstack is equal to last value in first stack
            self.minstack.pop() # popping from minstack
        self.stack.pop() # popping from first stack

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] # peeking the last element in first stack

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1] # peeking the last element in minstack


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
