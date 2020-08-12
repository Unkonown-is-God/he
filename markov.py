import os
import sys
from random import choice
from collections import defaultdict, deque
import re
import copy
import dill
import morph
import w2v


class Markov:
    # マルコフ連鎖による学習と生成
    '''クラス定数：
    ENDMARK　文章の終わりを表す記号
    CHAIN-MARK　連鎖の最大値
    ORDER　階数指定'''
    ENDMARK = '%END'
    CHAIN_MAX = 30
    ORDER = 3

    def __init__(self):
        self._dic = defaultdict(lambda: defaultdict(lambda: []))
        # マルコフ辞書 二次元配列のイメージ [key][key]=[value]
        # こんな感じの構造　{key:{key:[value1,value2,value3]},{},{}}
        self._starts = defaultdict(lambda: 0)
        # 文章が始まる単語の数

    # 学習
    def add_sentence(self, parts):
        # 三語以上でないと学習しないようにする
        if len(parts) < Markov.ORDER:
            return

        # 呼びだし元をグチャグチャにしないためにコピー
        parts = copy.copy(parts)
        # pythonの　a=b は　*a=&bと同意義　aの値を変えるとbの値まで変更してしまう
        # 変更したくないときはcopyをしよう！

        parts = [p[0] for p in parts]
        prefixs = [parts.pop(0) for i in range(Markov.ORDER-1)]
        # 文章の頭に単語を代入

        # 下にメソッドが宣言されている
        self._add_start(prefixs[0])
        # 始まりの単語を記録せし者

        for suffix, _ in parts:
            # 品詞は使わないので_
            self._add_suffix(prefixs, suffix)
            # 下に宣言されている
            # 辞書型の中のリスト型にどんどん追記していく

            prefixs = prefixs[1:]
            prefixs.append(suffix)
            # 左側にずれていくイメージ prefix1はいなくなるのであった
        self._add_suffix(prefixs, Markov.ENDMARK)
        # 文章が閉じたことを明記する

    def _add_suffix(self, prefixs, suffix):
        key = tuple(prefixs)
        self._dic[key].append(suffix)

    def _add_start(self, prefix1):
        self._starts[prefix1] += 1
        # 頻度もチェックできて便利

    # 文章の生成
    def generate(self, keyword):
        # 辞書が空だとnoneを返す
        if not self._dic:
            return None

        keyword = w2v.load_w2v(keyword)
        keys = self._dic.keys()
        keys1 = [key[0] for key in keys]
        prefix = keyword if keyword in keys1 else choice(
            list(self._starts.keys()))
        # keyword が　辞書に登録されていればkeywordを代入　登録されていなければランダムに代入

        index = self.search(prefix, keys1)
        key=keys[choice(index)]

        words = list(key)
        # 生成される文章の依り代

        for _ in range(Markov.CHAIN_MAX):
            # CHAIN_MAXまでループ

            suffix = choice(self._dic[key])
            # wordsに追加するsuffixを更新

            if suffix == Markov.ENDMARK:
                # suffixがEND_MARKなら終了
                break
            words.append(suffix)
            # wordsリストにsuffixを追加
            key = key[1:] + tuple(suffix)
            # prefixを更新

        return ''.join(map(str, words))
        # 生成された文章を返す

    def search(self, prefix, keys1):
        # prefixと同じkeys1の要素数を検索
        l = len(keys1)
        index = []
        for i in range(l):
            if keys1[i] == prefix:
                index.append(i)
        return index

    def load(self, filename):
        # filenameから辞書を読み取る
        try:
            with open(filename, 'rb') as f:
                self._dic, self._starts = dill.load(f)
        except TypeError:
            pass

    def save(self, filename):
        # filenameのファイルへ辞書データを書き込む
        with open(filename, 'wb') as f:
            dill.dump((self._dic, self._starts), f)

if __name__ == "__main__":
    print('demo')
    M=Markov()
    M.load('dics/markov.dat')
    key=input('>')
    M.generate(key)
