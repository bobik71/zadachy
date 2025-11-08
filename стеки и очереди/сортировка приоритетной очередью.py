from queue import PriorityQueue
r = int(input())
n1 = PriorityQueue()

for i in range(r):
    x,y = map(int,input().split())
    n1.put((x, y))


while not n1.empty():
    a, b = n1.get()
    print(a, b)