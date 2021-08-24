import time
from hashlib import sha256
MAX_NONCE = 10000000000000000

def SHA256(text):
    return (sha256(text.encode("ascii")).hexdigest())

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(23581981443663,MAX_NONCE) :
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"SUCCESSFULL!!! :) Nonce Value: {nonce}")
            return new_hash
    raise BaseException(f"NOT FOUND!! Trying @{MAX_NONCE} times! :/")

if __name__ == '__main__':
    transactions= '''
    Rony  -> Honey -> 20
    SC ->  DC -> 45
    '''

    difficulty = 7
    start = time.time()
    print("Start Mining")
    new_hash = mine(5, transactions, '896e3ac94d9fe903c7e15d572224a7815f00e2461bc9a', difficulty )
    total_time = str((time.time() - start))
    print(f'Time required: {total_time}')
    print(new_hash)