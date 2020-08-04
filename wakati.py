from janome.tokenizer import Tokenizer
import os
import morph

WAKATI = 'dics/wakati.txt'
# ' 'を使って分かつ


def wakati_text(text):
    t = Tokenizer()
    return t.tokenize(text, wakati=True)


def add_wakati(wakati):
    with open(WAKATI, 'a', encoding='utf-8') as f:
        print('\n'.join(wakati), file=f)


def load_file(path):
    # 実装途中
    with open(path) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines


if __name__ == '__main__':
    #一気に分かちたいとき
    path = input('path> ')
    lines = load_file(path)
    for line in lines:
        line = morph.fix(line)
        wakati = wakati_text(line)
        add_wakati(wakati)
