from dictionary import Dictionary


class Emotion:
    def __init__(self):
        dic = Dictionary()._emotion
        self.ewords = [d[0] for d in dic]
        self.evalues = [d[1] for d in dic]

    def emotionv(self, parts):
        twords = []
        tparts = []
        for p in parts:
            twords.append(p[0])
            tparts.append(p[1])
        sum = 0
        li = len(twords)
        lj = len(self.ewords)
        for i in range(li):
            if tparts[i] in ['動詞', '名詞', '形容詞', '副詞']:
                for j in range(lj):
                    if twords[i] == self.ewords[j]:
                        sum += self.evalues[j]
        return sum
