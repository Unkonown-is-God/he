from dictionary import Dictionary
import morph
import jaconv


class Emotion:
    def __init__(self,dictionary):
        dic = dictionary._emotion
        self.ewords = [d[0] for d in dic]
        self.evalues = [d[2] for d in dic]
        self.ereading = list(map(jaconv.hira2kata, [d[1]for d in dic]))

    def emotionv(self, parts):
        twords = []
        tparts = []
        treading = []
        for p in parts:
            twords.append(p[0])
            tparts.append(p[1])
            treading.append(p[2])
        sum = 0.0
        li = len(twords)
        lj = len(self.ewords)
        for i in range(li):
            if tparts[i].split(',')[0] in ['動詞', '名詞', '形容詞', '副詞']:
                for j in range(lj):
                    if twords[i] == self.ewords[j]:
                        if treading[i] == self.ereading[j]:
                            sum += float(self.evalues[j])
        return sum


if __name__ == "__main__":
    D=Dictionary()
    key = input()
    parts = morph.analyze(key,1)
    e = Emotion(D)
    print(parts[0][2])
    print(e.emotionv(parts))
