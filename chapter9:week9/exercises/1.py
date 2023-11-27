class Counter:
    def __init__(self):
        self.theCount = 0

    def inc(self):
        if self.theCount < 999:
            self.theCount = self.theCount + 1
        else:
            self.theCount = 0

    def dec(self):
        if self.theCount > 0:
            self.theCount = self.theCount - 1
        else:
            self.theCount = 999

    def getCount(self):
        return self.theCount
    
    def setCount(self, newCount):
        self.theCount = newCount

    def equals(self, other):
        return self.theCount == other.theCount
    
X = "aabbcc"

A = Counter ()
B = Counter ()
C = Counter ()
D = C
E = B

A.inc()

for char in X :
    A.inc()

B.dec()
B.dec()

B.dec()
B.inc()

C.inc()
C.setCount(7)

# AFTER RUNNING ALL OF THE CODE ABOVE

# How many times was the body of the for loop above executed ?
# 6

# What is the value of char ?

# What is the value of A.getCount() ?
# 7

# What is the value of B.getCount() ?
# 998

# What is the value of E.getCount() ?
# 998 or 0. Does E change as B changes, if so, E = 998, if not E = 0. GPT says 998 but idk if I trust it.

# What is the value of C.getCount() ?
# 7

# What is the value of C == D ?
# True

# What is the value of A == C ?
# False

# What is the value of A.equals(C) ?
# True