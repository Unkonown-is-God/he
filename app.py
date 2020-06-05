from flask import Flask, jsonify, abort, make_response
import os
from unmo import Unmo


app=Flask(__name__)
@app.route("/<key>",methods=["GET"])
'''def build_prompt(unmo):
    """AIインスタンスを取り、AIとResponderの名前を整形して返す"""
    return '{name}:{responder}> '.format(name=unmo.name,
                                         responder=unmo.responder_name)


if __name__ == '__main__':#main.pyがターミナルで実行されているのかを判別
    print('Unmo System prototype : proto')
    proto = Unmo('proto')
    while True:
        text = input('> ')
        if not text:
            break
        try:
            response=proto.dialogue(text)
        except IndexError as error:
            print('{}: {}'.format(type(error).__name__,str(error)))
            print('辞書が空です(Responder:{})'.format(proto.responder_name))
        else:
            print('{prompt}{response}'.format(prompt=build_prompt(proto),
                                          response=response))#{}のなかのやつと.formatのやつは名前をあわせ
    proto.save()
'''
def main(key):
        return "hello"

app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 5000)))