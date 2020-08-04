from gensim.models import word2vec
import random
model_file = 'dics/w2v_model.model'
def load_w2v(word): 
    model = word2vec.Word2Vec.load(model_file)
    try:
        print(1)
        similar_words = model.most_similar(positive=[word])
        return random.choice([w[0] for w in similar_words])
    except:
        return word

def make_moedl():
    pass