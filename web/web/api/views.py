from flask import Blueprint, jsonify, request

from web.utils import simhash

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/check', methods=['POST'])
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
        '漢明距離': distance,
        '相似結果': similarity
    })
