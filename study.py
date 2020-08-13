from unmo import Unmo
from util import format_error
import tqdm

FILE = 'dics/wakati.txt'
def build_prompt(unmo):
    """AIインスタンスを取り、AIとResponderの名前を整形して返す"""
    return '{name}:{responder}> '.format(name=unmo.name,
                                         responder=unmo.responder_name)


def load_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [x for x in f.read().splitlines() if x]  # リスト内表記で検索
    except IOError as e:
        print(format_error(e))
        return -1


if __name__ == '__main__':  # main.pyがターミナルで実行されているのかを判別
    print('Unmo System prototype : study')
    proto = Unmo('study')
    lines = load_file(FILE)
    
    for text in tqdm.tqdm(lines):
        if not text:
            pass
        try:
            response = proto.dialogue(text)
        except IndexError as error:
            pass
        else:
            pass
    proto.save()
