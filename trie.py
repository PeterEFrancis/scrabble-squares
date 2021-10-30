class Trie:
    def __init__(self):
        self.leaves = {}
        self.leaf = False
            
    def push(self, *words):
        for word in words:
            l = word[0]
            if l not in self.leaves:
                self.leaves[l] = Trie()
            if len(word) > 1:
                self.leaves[l].push(word[1:])
            else:
                self.leaves[l].leaf = True
    
    def contains(self, word):
        if len(word) == 0:
            return self.leaf
        elif word[0] in self.leaves:
            return self.leaves[word[0]].contains(word[1:])
        return False
    
    def has(self, word):
        if len(word) == 0:
            return True
        if word[0] in self.leaves:
            return self.leaves[word[0]].has(word[1:])
        return False
    
    def iterate(self):
        for letter in self.leaves:
            if self.leaves[letter].leaf:
                yield letter
            for subword in self.leaves[letter].iterate():
                yield letter + subword
    
    def after(self, word):
        state = self
        for letter in word:
            state = state.leaves[letter]
        for letter in state.leaves:
            yield letter
    
    def __str__(self):
        s = "{"
        for i, letter in enumerate(self.leaves):
            s += letter
            if len(self.leaves[letter].leaves) > 0:
                s += ":" + str(self.leaves[letter])
            if i != len(self.leaves) - 1:
                s += ","
        s += "}"
        return s