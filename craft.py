from unmo import Unmo


def build_prompt(unmo):
    """AIインスタンスを取り、AIとResponderの名前を整形して返す"""
    return '{name}:{responder}> '.format(name=unmo.name,
                                         responder=unmo.responder_name)


def apimode(key):
    value = {'title': 'Unmo System prototype : proto'}
    proto = Unmo('proto')
    try:
        response = proto.dialogue(key)
        value['response'] = response[0]
        value['emotion'] = response[1]
        value['prompt'] = build_prompt(proto)
    except IndexError as error:
        value['response'] = '{}: {}'.format(type(error).__name__, str(error))
    value['save'] = proto.save()
    return value


if __name__ == '__main__':  # main.pyがターミナルで実行されているのかを判別
    print('Unmo System prototype : proto')
    proto = Unmo('proto')
    while True:
        text = input('> ')
        if not text:
            break
        try:
            response = proto.dialogue(text)
        except IndexError as error:
            print('{}: {}'.format(type(error).__name__, str(error)))
            print('辞書が空です(Responder:{})'.format(proto.responder_name))
        else:
            print('{prompt}{response}:{emotion}'.format(prompt=build_prompt(proto),
                                                        response=response[0], emotion=response[1]))  # {}のなかのやつと.formatのやつは名前をあわせ
    proto.save()
