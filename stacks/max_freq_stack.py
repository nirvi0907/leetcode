class FreqStack:

    def __init__(self):
        self.freq_to_list = defaultdict(list)
        self.val_to_freq = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.val_to_freq[val] += 1
        self.freq_to_list[self.val_to_freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.val_to_freq[val])

    def pop(self) -> int:
        val = self.freq_to_list[self.max_freq].pop()
        self.val_to_freq[val] -= 1
        if not self.freq_to_list[self.max_freq]:
            self.max_freq -= 1
        return val