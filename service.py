#!flask/bin/python
"""
The purpose of this program is to allow users to conveniently query word2vec
in order to save time and make experiments faster.
don't forget to set MODEL_PATH before starting.
"""

global model # I know, I'm sorry...
import os
import gensim
print("Loading... Be patient...")
model = gensim.models.KeyedVectors.load_word2vec_format(os.getenv("MODEL_PATH")+'/GoogleNews-vectors-negative300.bin.gz', binary=True)
print("model Loaded")

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_vec/<string:lwords>/<string:rwords>', methods=['GET'])
def get_vec(lwords, rwords):
    global model
    return jsonify({'n_similarity': str(model.n_similarity(lwords.split(" "),rwords.split(" ")))})

@app.route('/')
def index():
    return jsonify({'res': []})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='7634',debug=True)
