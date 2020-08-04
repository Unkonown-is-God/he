from janome.tokenizer import Tokenizer
import os
import morph

WAKATI = 'dics/wakati.txt'
# ' 'を使って分かつ

class Wakati():
    def __init__(self):
        with open(WAKATI, 'r', encoding='utf-8') as f:
            self.texts = [x for x in f.read().splitlines() if x]


    def wakati_text(self,text):
        t = Tokenizer()
        return t.tokenize(text, wakati=True)


    def add_wakati(self,wakati):
        wakati=' '.join(wakati)
        if not wakati in self.texts:
            with open(WAKATI, 'a', encoding='utf-8') as f:
                print(' '.join(wakati), file=f)


    def load_file(self,path):
        # 実装途中
        with open(path,'r',encoding='utf-8') as f:
            lines = [l.strip() for l in f.readlines()]
        return lines

if __name__ == '__main__':
    #一気に分かちたいとき
    w=Wakati()
    path = input('path> ')
    lines = w.load_file(path)
    for line in lines:
        line = morph.fix(line)
        wakati = w.wakati_text(line)
        w.add_wakati(wakati)
