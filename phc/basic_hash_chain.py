from phc import sm3

salt = "453245b037ea9220b49395e65954411ad156bcc1dddf712863f2c8ecfcb22dc4"
share_key = "3245b037ea9220b49395e65954411ad156bcc1dddf712863f2c8ecfcb22dc445"

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
        self.length = -1


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

    def isContain(self, trace_hashchain):
        current_Node = self.header
        for i in range(self.length):
            if current_Node.hash_chain == trace_hashchain:
                return True
            current_Node = current_Node.next
        return False

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
        return self.header.hash_chain

    def get_final_sequence(self):
        return self.header.sequence

    def get_final_pkthash(self):
        return self.header.packet_hash

def init_hash_chain(hash_chain):
    register = "register"
    register_b = bytes(register, encoding='utf-8')
    register_hash = sm3.sm3_hash(register_b)
    node = Node(register_hash, register_hash, 0)
    hash_chain.insert(node)
    return hash_chain

def continue_hashchain(hash_chain, final_node, content, sequence):

    content_b = bytes(content, encoding='utf-8')
    content_hash = sm3.sm3_hash(content_b)
    merge_hash_b = bytes(final_node + content_hash, encoding='utf-8')
    chain_hash = sm3.sm3_hash(merge_hash_b)
    node = Node(content_hash, chain_hash, sequence)
    hash_chain.insert(node)


def basic_hash_chain_construction(message, hash_chain):
    print(message)
    message_b = bytes(message, encoding='utf-8')
    message_hash = sm3.sm3_hash(message_b)
    merge_hash = hash_chain.header.hash_chain+message_hash
    print(merge_hash)
    merge_hash_b = bytes(merge_hash, encoding='utf-8')
    new_hash_chain = sm3.sm3_hash(merge_hash_b)
    node = Node(message_hash, new_hash_chain, hash_chain.header.sequence+1)
    hash_chain.insert(node)


def pk_hash_chain_construction(message, hash_chain):
    message_b = bytes(message+share_key, encoding='utf-8')
    message_hash = sm3.sm3_hash(message_b)
    merge_hash = hash_chain.header.hash_chain+message_hash
    merge_hash_b = bytes(merge_hash, encoding='utf-8')
    new_hash_chain = sm3.sm3_hash(merge_hash_b)
    node = Node(message_hash, new_hash_chain, hash_chain.length+1)
    hash_chain.insert(node)

def salt_hash_chain_construction(message, hash_chain):
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

    message = "123"

    for i in range(100):
        basic_hash_chain_construction(message, hash_chain)
        hash_chain.get_final_hash_chain_node()