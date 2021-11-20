from phc import sm3

salt = "453245b037ea9220b49395e65954411ad156bcc1dddf712863f2c8ecfcb22dc4"
share_key = "3245b037ea9220b49395e65954411ad156bcc1dddf712863f2c8ecfcb22dc445"

def init_hash_chain(sip, dip):
    register = "register"
    register_b = bytes(register, encoding='utf-8')
    register_hash = sm3.sm3_hash(register_b)
    hashnode = {}
    hashnode["sip"] = sip
    hashnode["dip"] = dip
    hashnode["pkthash"] = register_hash
    hashnode["chainhash"] = register_hash
    hashnode["seq"] = 0
    return hashnode

def basic_hash_chain_construction(message, hashnode):
    message_b = bytes(message, encoding='utf-8')
    message_hash = sm3.sm3_hash(message_b)
    merge_hash = message_hash + hashnode["chainhash"]
    merge_hash_b = bytes(merge_hash, encoding='utf-8')
    new_hash_chain = sm3.sm3_hash(merge_hash_b)
    seq = hashnode["seq"]
    hashnode["pkthash"] = message_hash
    hashnode["chainhash"] = new_hash_chain
    hashnode["seq"] = seq+1
    return hashnode

def pk_hash_chain_construction(message, hashnode):
    message_b = bytes(message + share_key, encoding='utf-8')
    message_hash = sm3.sm3_hash(message_b)
    merge_hash = message_hash + hashnode["chainhash"]
    merge_hash_b = bytes(merge_hash, encoding='utf-8')
    new_hash_chain = sm3.sm3_hash(merge_hash_b)
    seq = hashnode["seq"]
    hashnode["pkthash"] = message_hash
    hashnode["chainhash"] = new_hash_chain
    hashnode["seq"] = seq+1
    return hashnode

def salt_hash_chain_construction(message, hashnode):
    message_b = bytes(message, encoding='utf-8')
    message_hash = sm3.sm3_hash(message_b)
    merge_hash = message_hash + hashnode["chainhash"] + salt
    merge_hash_b = bytes(merge_hash, encoding='utf-8')
    new_hash_chain = sm3.sm3_hash(merge_hash_b)
    seq = hashnode["seq"]
    hashnode["pkthash"] = message_hash
    hashnode["chainhash"] = new_hash_chain
    hashnode["seq"] = seq+1
    return hashnode