import json
import ast
import urllib
from flask import Flask, request, make_response, render_template
from main import make

app = Flask(__name__)


@app.route("/")
def menu():
    return render_template("index.html")


@app.route('/pdf', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        with open('resources/empty.json') as f:
            data_dict = json.load(f)
    else:
        # decoding binary
        data_str = request.get_data().decode('utf-8')
        # convertion to dictionary
        data_dict = ast.literal_eval(data_str)

    # saving temporarily PDF file to buffer
    buffer = make(data_dict)
    pdf = buffer.getvalue()
    buffer.close()
    # generating response
    response = make_response(pdf)
    # deciding the file name from chara name
    downloadFileName = data_dict['name'] if data_dict['name'] else '名無しの権兵衛'
    dispostion = "attachment; filename*=UTF-8''"
    # enable encoding Japanese
    dispostion += urllib.parse.quote(downloadFileName + '.pdf')

    response.headers['Content-Disposition'] = dispostion
    response.mimetype = 'application/pdf'

    return response


if __name__ == "__main__":
    app.run(debug=True)
