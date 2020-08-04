from random import choice, randrange
from responder import RandomResponder, WhatResponder, PatternResponder, TemplateResponder, MarkovResponder
from dictionary import Dictionary
import morph
from emotion import Emotion
from wakati import Wakati


class Unmo:
    """人工無脳コアクラス。
    プロパティ:
    name -- 人工無脳コアの名前
    responder_name -- 現在の応答クラスの名前
    """
    # 名前の設定を行うクラスだよ


    def __init__(self, name):
        """文字列を受け取り、コアインスタンスの名前に複数設定する。"""
        self._dictionary = Dictionary()
        self._name = name  # Unmoの名前を設定している
        self._responders = {'random': RandomResponder('Random', self._dictionary),  # 辞書型でクラスを登録
                            'what': WhatResponder('What', self._dictionary),
                            'pattern': PatternResponder('Pattern', self._dictionary),
                            'template': TemplateResponder('template', self._dictionary),
                            'markov': MarkovResponder('markov', self._dictionary)
                            }
        # 登録されたクラスをここで指定して呼びだしている
        self._responder = self._responders['pattern']
        self._emotion = Emotion(self._dictionary)
        self._wakati=Wakati()
        # 初期設定としてrandom
        # 呼び出されたクラスはインスタンス化される（要するに__init__が動く)

    def dialogue(self, text):
        """ユーザーからの入力を受け取り、Responderに処理させた結果を返す。"""
        text = morph.fix(text)
        chance = randrange(0, 100)  # random.randomではfloat型なのでrandrangeを使う
        # ランダムに0から１００を生成
        '''
        if chance in range(0, 30):  # rangeはint型　０から５９
            self._responder = self._responders['pattern']
        elif chance in range(30, 50):  # rangeはstart<=x<stop この場合60以上９０未満
            self._responder = self._responders['template']
        elif chance in range(50, 70):
            self._responder = self._responders['random']
        el
        '''
        if chance in range(0, 100):
            self._responder = self._responders['markov']
        else:
            self._responder = self._responders['what']
        parts = morph.analyze(text, 0)
        response = self._responder.response(text, parts)
        self._dictionary.study(text, parts)
        parts = morph.analyze(response, 1)
        emotion = self._emotion.emotionv(parts)
        text=self._wakati.wakati_text(text)
        self._wakati.add_wakati(text)
        return [response, emotion]

    def save(self):
        # Dictionaryのsaveを持ってくる
        self._dictionary.save()
        return 1

    @property
    def name(self):
        """unmoの名前を返す"""
        return self._name

    @property
    def responder_name(self):
        """Responderの名前を返す"""
        return self._responder.name
