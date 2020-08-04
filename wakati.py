from janome.tokenizer import Tokenizer
import os

WAKATI = 'dics/wakati.txt'
#' 'を使って分かつ
def wakati_text(text):
    t = Tokenizer()
    return t.tokenize(text,wakati=True)

def add_wakati(wakati):
    with open(WAKATI,'a',encoding='utf-8') as f:
        print('\n'.join(wakati),file=f)

def load_file(path):
    #実装途中
    pass
if __name__ == '__main__': 
    path=input()
    sentences=load_file(path)
    for line in sentences:
        wakati=wakati_text(line)
        add_wakati(wakati)
        
