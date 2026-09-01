class RandomizedSet(object):

    def __init__(self):
        self.SET = set()

    def insert(self, val):
        if val not in self.SET:
            self.SET.add(val)
            return True
        return False
        

    def remove(self, val):
        if val in self.SET:
            self.SET.remove(val)
            return True
        return False
        

    def getRandom(self):
        return random.choice(list(self.SET))



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()