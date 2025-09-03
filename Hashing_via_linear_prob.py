class Dictionary:
    
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size # Slots are nothing but it is an array for keys for dictionary
        self.data = [None] * self.size # Slots are nothing but it is an array for value for dictionary
        
    def put(self,key,value):
        hash_val = self.hash_func(key)
        if self.slots[hash_val] == None:
            self.slots[hash_val] = key
            self.data[hash_val] = value
        else:
            if self.slots[hash_val] == key:
                self.data[hash_val] = value
            else:
                new_hash = self.rehash(hash_val)
                while self.slots[new_hash] != None and self.slots[new_hash] != key:
                    new_hash = self.rehash(new_hash)
                if self.slots[new_hash] == None:
                    self.slots[new_hash] = key
                    self.data[new_hash] = value
                else:
                    self.data[new_hash] = value
    
    def __setitem__(self,key,value):
        self.put(key,value)
    
    def get(self,key):
        start_pos = self.hash_func(key)
        curr_pos = start_pos
        
        while self.slots[curr_pos] != None:
            if self.slots[curr_pos] == key:
                return self.data[curr_pos]
            curr_pos = self.rehash(curr_pos)
            if start_pos == curr_pos:
                return "Item Not Found In Array"
        return 'Item Not found'
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __str__(self):
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(self.slots[i],':',self.data[i],end=' ')
        return ''
    
    def rehash(self,old_hash):
        return (old_hash + 1) % self.size
    
    def hash_func(self,key):
        return abs(hash(key)) % self.size
    
d1 = Dictionary(3)
d1['Python'] = 7
d1["Java"] = 4
d1['JS'] = 2

print(d1)