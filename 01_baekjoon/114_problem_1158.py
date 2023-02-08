# https://www.acmicpc.net/problem/1158
# 요세푸스 문제

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)


    def insert(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
    
    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            count += 1
            node = node.next

        return node

    
    def delete_node(self, index):
        if index == 0:
            del_node = self.head.data
            self.head = self.head.next
            return del_node
        node = self.get_node(index-1)
        del_node = node.next.data
        node.next = node.next.next
        return del_node


N, K = list(map(int, sys.stdin.readline().split()))

LinkList = LinkedList(1)
for i in range(2, N + 1):
    LinkList.insert(i)

answer = []
idx = K - 1
while LinkList.head is not None:
    idx %= N
    answer.append(LinkList.delete_node(idx))
    idx += (K - 1)
    N -= 1

print('<', end='')
for i in range(len(answer) - 1):
    print(answer[i], end=', ')
print(answer[len(answer)-1], end='')
print('>')