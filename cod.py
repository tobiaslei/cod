from flask import Flask, request, jsonify
import requests
import lxml.html

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def parse():
    """
        input json:
        {
            'url': 'http://flask.pocoo.org/docs/0.11/quickstart/#accessing-request-data',
            'xpath': '//*[@id="the-request-object"]/div[2]/div/pre'
        }
    """
    input_json = request.get_json()
    if 'url' not in input_json or 'xpath' not in input_json:
        return jsonify({'status': 'error', 'msg': 'missing url or xpath'})

    page = lxml.html.parse(input_json['url']).getroot()
    r = page.xpath(input_json['xpath'])
    out = []
    if isinstance(r, list):
        for i in r:
            out.append(lxml.html.tostring(i).strip())
    else:
        out.append(lxml.html.tostring(i).strip())

    return jsonify({'status':'ok', 'result': out})

if __name__ == "__main__":
    app.run()