from janome.tokenizer import Tokenizer
import os

WAKATI = 'dics/wakati.txt'
#' 'を使って分かつ
def wakati_text(text):
    t = Tokenizer()
    return t.tokenize(text,wakati=True)

def add_wakati(sentence):
    with open(WAKATI,'a') as f:
        print('\n'.join(sentence),file=f)

def load_file(path):
    pass
