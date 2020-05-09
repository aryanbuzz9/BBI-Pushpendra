#Stack Implementation Using Array(List) In Python
class Stack:
  def __init__(self,n):
    self.arr=[None]*3
    self.top=-1
    self.size=n
  def push(self,data):
    if(self.top<self.size):
      self.top=self.top+1
      self.arr[self.top]=data
    else:
      print("Overflow")
      exit(1)
  def pop(self):
    if(self.top>=0):

      data=self.arr[self.top]
      self.top=self.top-1
      return data
    else:
      print("underflow")
      exit(1)
obj=Stack(3)
obj.push(7)
obj.push(98)
obj.push(19)
#obj.push(67)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
print(obj.arr)

#Queue implementation Using Array(List) In Python

class Queue: 

	def __init__(self, capacity): 
		self.front = self.size = 0
		self.rear = capacity -1
		self.arr = [None]*capacity 
		self.capacity = capacity 

	def isFull(self): 
		return self.size == self.capacity 

	def isEmpty(self): 
		return self.size == 0

	def add(self, item): 
		if self.isFull(): 
			print("Full") 
			return
		self.rear = (self.rear + 1) % (self.capacity) 
		self.arr[self.rear] = item 
		self.size = self.size + 1
		print(item) 

	def pop(self): 
		if self.isEmpty(): 
			print("Empty") 
			return
		
		print(self.arr[self.front]) 
		self.front = (self.front + 1) % (self.capacity) 
		self.size = self.size -1

	def que_front(self): 
		if self.isEmpty(): 
			print("Queue is empty") 

		print("Front item is", self.arr[self.front]) 

	def que_rear(self): 
		if self.isEmpty(): 
			print("Queue is empty") 
		print("Rear item is", self.arr[self.rear]) 
 

queue = Queue(10) 
print("Added items")
queue.add(10) 
queue.add(20) 
queue.add(30) 
queue.add(40) 
print("Deleted items")
queue.pop()

queue.que_front()

queue.que_rear() 


