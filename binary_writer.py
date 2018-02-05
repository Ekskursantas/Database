import sys





def write_to(word1, word2):
    file_db = open('db.txt', 'a')
    file_db.write(' '.join(format(ord(x), 'b') for x in word1)+ " ")

def read_from():
    file_db = open('db.txt', 'rb')
    message = file_db.read().decode('utf-8')
    message = ''.join(chr(int(message[i*8:i*8+8],2)) for i in range(len(message)//8))
    
    print(message)
if __name__ == "__main__":
    write_to('emilisapoop', 97)
    read_from()