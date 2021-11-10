import sm3

class Node(object):
    def __init__(self, packet_hash, hash_chain, sequence):
        self.packet_hash = packet_hash
        self.hash_chain = hash_chain
        self.sequence = sequence
        self.next = None

# 创建单链表类
class Hash_Chain(object):
    def __init__(self):
        self.header = None
        self.length = 0


    # 1、判断是否为空
    def is_empty(self):
        if self.header == None:
            return True
        else:
            return False

    def insert(self, node):
        if self.is_empty():
            self.header = node
        else:
            node.next = self.header
            self.header = node
            # currentNode = self.header
        self.length += 1

    def travel(self):
        current_Node = self.header
        if self.length == 0:
            print("目前链表没有数据！")
        else:
            print("目前链表里面的元素有:", end=" ")
            for i in range(self.length):
                print("%s " % current_Node.packet_hash, end=" ")
                print("%s " % current_Node.hash_chain, end=" ")
                print("%s " % current_Node.sequence, end=" ")
                current_Node = current_Node.next
            print("\n")

    # 8、查找是否包含,并返回下标
    def isContain(self, num):
        contain = 0
        current_Node = self.header
        for i in range(self.length):
            if current_Node.element == num:
                print("%d在链表中%d处\n" % (num, i + 1))  # i+1是在正常人认为的位置处，程序员一般是从0开始算起
                contain = 1
            current_Node = current_Node.next
        if contain == 0:
            print("%d不在链表中\n" % num)

    # 9、根据下标找节点
    def searchNodeByIndex(self, index):
        current_Node = self.header
        if index <= 0 or index > self.length:
            while (index <= 0 or index > self.length):
                print("你输入的下标不对，请重新输入:")
                index = eval(input())
            #   return 0
        if index > 0 or index <= self.length:
            for i in range(index - 1):
                current_Node = current_Node.next
            return current_Node

    # 10、根据下标修改节点的值
    def Alert(self, index, num):  # index定义为下标
        current_Node = self.header
        if index <= 0 or index > self.length:
            print("你输入的下标不对，请重新输入!\n")
        else:
            for i in range(index - 1):
                current_Node = current_Node.next
            current_Node.element = num

    def get_final_hash_chain_node(self):
        print(self.header.hash_chain)

def init_hash_chain(hash_chain):
    register = "register"
    register_b = bytes(register, encoding='utf-8')
    register_hash = sm3.sm3_hash(register_b)
    node = Node(register_hash, register_hash, 1)
    hash_chain.insert(node)
    return hash_chain

def basic_hash_chain_construction(message, hash_chain):
    message_b = bytes(message, encoding='utf-8')
    message_hash = sm3.sm3_hash(message_b)
    merge_hash = hash_chain.header.hash_chain+message_hash
    merge_hash_b = bytes(merge_hash, encoding='utf-8')
    new_hash_chain = sm3.sm3_hash(merge_hash_b)
    node = Node(message_hash, new_hash_chain, hash_chain.length+1)
    hash_chain.insert(node)


def pk_hash_chain_construction(message, hash_chain, pk):
    message_b = bytes(message+pk, encoding='utf-8')
    message_hash = sm3.sm3_hash(message_b)
    merge_hash = hash_chain.header.hash_chain+message_hash
    merge_hash_b = bytes(merge_hash, encoding='utf-8')
    new_hash_chain = sm3.sm3_hash(merge_hash_b)
    node = Node(message_hash, new_hash_chain, hash_chain.length+1)
    hash_chain.insert(node)

def salt_hash_chain_construction(message, hash_chain, salt):
    message_b = bytes(message, encoding='utf-8')
    message_hash = sm3.sm3_hash(message_b)
    merge_hash = hash_chain.header.hash_chain+message_hash+salt
    merge_hash_b = bytes(merge_hash, encoding='utf-8')
    new_hash_chain = sm3.sm3_hash(merge_hash_b)
    node = Node(message_hash, new_hash_chain, hash_chain.length+1)
    hash_chain.insert(node)

if __name__ == '__main__':

    hash_chain = Hash_Chain()

    init_hash_chain(hash_chain)

    message = "111"

    for i in range(100):
        basic_hash_chain_construction(message, hash_chain)
        hash_chain.get_final_hash_chain_node()