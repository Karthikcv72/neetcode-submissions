class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        value=min(value,self.minStack[-1] if self.minStack else value)
        self.minStack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]