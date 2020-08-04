from gensim.models import word2vec
import random
MODEL = 'dics/w2v_model.model'
WAKATI  'dics/wakati.txt'
def load_w2v(word): 
    model = word2vec.Word2Vec.load(model_file)
    try:
        #print('w2v')
        similar_words = model.most_similar(positive=[word])
        return random.choice([w[0] for w in similar_words])
    except:
        return word

def make_model():
    w2v_data = word2vec.LineSentence(WAKATI)
    model = word2vec.Word2Vec(w2v_data,size=100,window=3,hs=1,min_count=1,sg=1)
    moel.save(MODEL)
    
def word_calculator(text):
    pass
