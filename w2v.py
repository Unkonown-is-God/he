from gensim.models import word2vec
import random
MODEL = 'dics/w2v_model.model'
WAKATI = 'dics/wakati.txt'


def load_w2v(word):
    model = word2vec.Word2Vec.load(MODEL)
    try:
        # print('w2v')
        similar_words = model.most_similar(positive=[word])
        return random.choice([w[0] for w in similar_words])
    except:
        return word


def make_model():
    w2v_data = word2vec.LineSentence(WAKATI)
    model = word2vec.Word2Vec(
        w2v_data, size=100, window=3, hs=1, min_count=1, sg=1)
    model.save(MODEL)


def word_calculator(text):
    pass

if __name__ == "__main__":
    make_model()
    model = word2vec.Word2Vec.load(MODEL)
    keys=input('>').split()
    # print('w2v')
    for word in keys:
        print(word+'↓')
        similar_words = model.most_similar(positive=[word])
        print(similar_words)
