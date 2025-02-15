class MyStack:
    
    
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        #we need to reverse the elements in the queue
        # so we do as elements are coming
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            first_item = self.queue.popleft()
            self.queue.append(first_item)

    def pop(self) -> int:
        return self.queue.popleft()
        
    def top(self) -> int:
        return self.queue[0]
        
    def empty(self) -> bool:
        return False if self.queue else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()