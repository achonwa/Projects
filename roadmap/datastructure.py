class CustomStack:


     def __init__(self):
        
         self.stack = [] #Internal storage
         self.min_stack =[]
         self.max_stack =[]

    
     def push(self,item):
         self.stack.append(item) # Add item to the stack
         if not self.min_stack or item <= self.min_stack[-1]:
             self.min_stack.append(item)
         if not self.max_stack or item >= self.max_stack[-1]:
             self.max_stack.append(item)


     def pop(self):

        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        item = self.stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        if item == self.max_stack[-1]:
            self.min_stack.pop()
        return item

     def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.item[-1] # view the last item

     def is_empty(self):
        return len(self.stack) == 0

     def min(self):
        if not self.is_empty():

            return self.min_stack[-1]

        raise ValueError("Min from empty stack")
        # return min(self.elements) # find the minimum value

     def max(self):
        if not self.is_empty():
            
            return self.max_stack[-1] # Find the maximum value
        raise ValueError('Max from empty stack')

     def sort(self):
        self.item = sorted(self.stack , reverse = True) # sort in decending order

     def display(self):
        print(self.item) # print all elements


class CustomQueue:

     def __init__(self):
        self.queue = []

     def enqueue(self, item):
        self.queue.append(item) # add items to the queue

     def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) #this removes the first element on the queue
        raise IndexError("dequeue from an empty queue")

     def front(self):

    # """ 
    # gets the first element on the queue without removing it
    # return the front element on the queue
    # raises error if the queue is empty
    # """
        if not self.is_empty():
            return self.queue[0]
        raise IndexError('Front from an empty queue')


     def is_empty(self):
        #check if queue is empty

        return len(self.queue) == 0

    
     def size(self):
        # get the size  or number of elememnts in the queue 
        return len (self.queue)



if __name__ == "__main__":
    CTQ = CustomQueue()

    CTQ.enqueue("walter")
    CTQ.enqueue("frodd")
    CTQ.enqueue('Frank')
    print('Queue after enqueues: ', CTQ.queue)

    print("Front element:", CTQ.front())

    dequeued = CTQ.dequeue()
    print("Dequeued Element: ", dequeued)
    print("Queue after dequeue: " , CTQ.queue)

    print("Is the queue empty?", CTQ.is_empty())

    print("Queue size:", CTQ.size())



if __name__ == "__main__":
    CTS = CustomStack()

    CTS.push(23)
    CTS.push(45)
    CTS.push(27)
    CTS.push(27)
    CTS.push(27)
    CTS.push(27)
    CTS.push(27)
    print("THE STACK AFTER BEING STACKED: ", CTS.stack)
    print ("This me peeking into the stack:", CTS.peek)
    print("Min:", CTS.min())
    print("sortin the stack:", CTS.sort())
    CTS.pop()
    print("After Pop:", CTS.stack)



    

    