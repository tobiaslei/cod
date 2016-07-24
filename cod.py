from flask import Flask, request, jsonify
import requests
import lxml.html
from lxml import etree
import collections

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

    if 'url' not in request.form or 'xpath' not in request.form:
        out = collections.OrderedDict()
        out['status'] = 'error'
        out['msg'] = 'missing url or xpath'
        return jsonify(out)

    res = requests.get(request.form['url'])
    tree = etree.HTML(res.text)
    r = tree.xpath(request.form['xpath'])
    out = []
    if isinstance(r, list):
        for i in r:
            out.append(lxml.html.tostring(i).strip())
    else:
        print r
        out.append(lxml.html.tostring(r).strip())

    return jsonify(collections.OrderedDict({'status':'ok', 'result': out}))

from flask import render_template
@app.route('/samples')
def hackernews():
    return render_template('samples.html')

if __name__ == "__main__":
    app.run()