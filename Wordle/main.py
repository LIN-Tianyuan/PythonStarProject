import pandas as pd
class Code(list):
    def __init__(self, code=None, word=None, target=None):

        self.g = '\U0001f7e9'
        self.r = '\U0001f7e5'
        self.y = '\U0001f7e8'
        self.b = '\u2B1B'

        self.convert = [self.b, self.y, self.g]

        self.code = code
        self.target = target
        self.word = word

        if code is None and target is not None and word is not None:
            self.code = compare(word, target)

    def __repr__(self):
        if self.word is not None:
            return "".join([self.convert[c] for c in self.code]) + " Attempt {}, Target {}".format(self.word.upper(),
                                                                                                   self.target.upper())
        return "".join([self.convert[c] for c in self.code])

    def __getitem__(self, idx):
        return self.code[idx]

    def __setitem__(self, idx, v):
        self.code[idx] = v

    def __iter__(self):
        yield from self.code


def isin(c, word, word_marked):
    for i in range(5):
        if c == word[i] and not word_marked[i]:
            word_marked[i] = True
            return True
    return False


def compare(word, target):
    code = Code([0 for _ in range(5)], word, target)
    target_marked = [False for _ in target]
    for i, (u, v) in enumerate(zip(word, target)):
        if u == v:
            code[i] = 2
            target_marked[i] = True

    for i, (u, v) in enumerate(zip(word, target)):
        if u != v and isin(u, target, target_marked):
            code[i] = 1
    return code


def code_satisfied(code, new_word):
    word = code.word
    new_word_marked = [False for _ in range(5)]
    for i, (w, c) in enumerate(zip(word, code)):
        if c == 2 and w != new_word[i]:
            return False
        elif c == 2:
            new_word_marked[i] = True

        elif c == 1 and w == new_word[i]:
            return False
        elif c == 1:
            new_word_marked[i] = True
            if not isin(w, new_word, new_word_marked):
                return False

        elif c == 0 and w in new_word:
            return False
    return True


word_list = pd.read_csv('word_list.csv', header=None).squeeze().tolist()


def find_longest_valid_sequence(target, words):
    def backtrack(sequence, codes):
        if len(sequence) > len(best_sequence[0]):
            best_sequence[0] = list(sequence)

        for word in words:
            if word not in sequence:
                if all(code_satisfied(code, word) for code in codes):
                    new_code = compare(word, target)
                    sequence.append(word)
                    codes.append(new_code)
                    backtrack(sequence, codes)
                    sequence.pop()
                    codes.pop()

    best_sequence = [[]]
    backtrack([], [])
    return best_sequence[0]

seq = find_longest_valid_sequence('TRACK', word_list)
print(seq)