from flask import Flask, jsonify, request

from web.utils import simhash

app = Flask(__name__)

@app.route('/check', methods = ['POST'])
def check_documents_is_similar():
    request_data = request.get_json()

    document1 = request_data['document1']
    document2 = request_data['document2']

    hash1 = simhash(document1)
    hash2 = simhash(document2)

    distance = hash1.hammingDis(hash2)
    similarity = False

    if distance <= 18:
        similarity = True

    return jsonify({
        '距離': distance,
        '結果': similarity
    })