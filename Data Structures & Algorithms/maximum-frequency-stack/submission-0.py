class FreqStack:

    def __init__(self):
        self.counts = {}
        self.groups = defaultdict(list)
        self.currMax = 0

        # Think of groups like this:
        # frequency 1 → [5, 7, 4] -> -1th val of this list will always be most recent val
        # frequency 2 → [5, 7]
        # frequency 3 → [5]


    def push(self, val: int) -> None:
        self.counts[val] = self.counts.get(val, 0) + 1
        currFreq = self.counts[val]

        self.groups[currFreq].append(val)

        self.currMax = max(self.currMax, currFreq)

    def pop(self) -> int:
        res = self.groups[self.currMax].pop()

        self.counts[res] -= 1

        if not self.groups[self.currMax]:
            self.currMax -= 1
        
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()