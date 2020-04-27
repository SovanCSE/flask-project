class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None] * self.MAX

    #Get hash value for specific key
    def get_hash(self, key):
        h=0
        for ch in key:
            h =+ ord(ch)
        return h % self.MAX

    #get value over key
    def __getitem__(self, key):
        hash_value= self.get_hash(key)
        return self.arr[hash_value]

    #set key value in dictionary
    def __setitem__(self, key, item):
       hash_value = self.get_hash(key)
       self.arr[hash_value] = item

    def __delitem__(self, key):
        hash_value = self.get_hash(key)
        self.arr[hash_value] = None

if __name__ == "__main__":
    hashtable = HashTable()
    hashtable['march 6'] = 120
    hashtable['april 9'] = 123
    hashtable['may 8'] = 125
    hashtable['december 10'] = 127
    print(hashtable['march 7'])
    print(hashtable['march 6'])
    print(hashtable['may 8'])
    print(hashtable['december 10'])
    print(hashtable['april 9'])
    print(hashtable['kkk'])
    del hashtable['april 9']
    print(hashtable['april 9'])