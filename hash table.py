class HashTable:
    def __init__(self,size=5):
        self.size=size
        self.table=[[] for x in range(self.size)]
    def getIndex(self,key):
        return hash(key)% self.size
    def insert(self,key,value):
        index=self.getIndex(key)
        for i,(k,v) in enumerate(self.table[index]):
            if k==key:
                self.table[index][i]=(key,value)
                return
        self.table[index].append((key,value))
    def delete(self,key):
        index=self.getIndex(key)
        for i,(k,v) in enumerate(self.table[index]):
            if k==key:
                del self.table[index][i]
                return
        return 'key not found'
    def search(self,key):
        index=self.getIndex(key)
        for k,v in self.table[index]:
            if k==key:
                return v
        return 'key not found'
    def display(self):
        for i,j in enumerate(self.table):
            print(f'{i}:{j}')
# ha=HashTable()
# ha.insert('aa',10)
# ha.insert('bb',33)
# ha.insert('xx',77)
# ha.delete('aa')
# ha.display()  

def hash_freq(arr):
    freq_table={}
    for i in arr:
        if i in freq_table:
            freq_table[i]+=1
        else:
            freq_table[i]=1
    return freq_table
# print(hash_freq([1,2,2,3,3,4,3,4]))

def hash_dupli(arr):
    dupli=set()
    for i in arr:
        if i in dupli:
            return True
        dupli.add(i)
    return False
# print(hash_dupli([3,2,2,1,1,1,2]))
