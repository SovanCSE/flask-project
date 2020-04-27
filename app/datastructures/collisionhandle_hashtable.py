class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    #Get hash value for specific key
    def get_hash(self, key):
        h=0
        for ch in key:
            h =+ ord(ch)
        return h % self.MAX

    #get value over key
    def __getitem__(self, key):
        hash_value = self.get_hash(key)
        for element in self.arr[hash_value]:
            if element[0] == key:
                return element[1]

    #set key value in dictionary
    def __setitem__(self, key, item):
       hash_value = self.get_hash(key)
       print(hash_value)
       found_key = False
       for idx, element in enumerate(self.arr[hash_value]):
         if len(element) == 2 and element[0] == key:
             self.arr[hash_value][idx] = (key, item)
             found_key = True
             break
       if not found_key:
           self.arr[hash_value].append((key,item))


    def __delitem__(self, key):
        hash_value = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash_value]):
            if element[0] == key:
                del self.arr[hash_value][idx]


if __name__ == "__main__":
    hashtable = HashTable()
    hashtable['march 6'] = 120
    hashtable['march 7'] = 123
    hashtable['march 8'] = 145
    hashtable['march 9'] = 167
    hashtable['march 16'] = 450
    print(hashtable['march 6'])
    print(hashtable['march 16'])
    del hashtable['march 16']
    print(hashtable['march 16'])

