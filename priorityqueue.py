import heapq

class priorityqueue:
    def __init__(self) -> []:
        self.heap = []

    def insert(self, item, priority):
        heapq.heappush(self.heap,(priority, item))

    def min_value(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        else:
            return None
        
    def is_empty(self):
        return len(self.heap) == 0
    
priority_queue = priorityqueue()

priority_queue.insert(2,1)
priority_queue.insert(6,3)

while not priority_queue.is_empty():
    priority, task = priority_queue.min_value()
    print(f"Priority: {priority}, Task: {task}")