from flask import Flask, json, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    obj = {'data': {'resp': 1}}
    return transfer_response(obj)

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    print(request.headers)
    sentences = request.json
    if isinstance(sentences, str):
        sentences = json.loads(sentences)
    print(sentences)
    obj = {'data': sentences}
    return transfer_response(obj)


def transfer_response(obj, status_code=200):
    predict_results = json.dumps(obj, ensure_ascii=False)
    return Response(
        response=predict_results,
        mimetype="application/json; charset=UTF-8",
        status=status_code
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)