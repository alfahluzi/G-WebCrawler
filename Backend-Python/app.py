from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import logging
import MainFunc

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/googlecrawl/<path:keyword>', methods=['GET'])
def googleSearch(keyword):
    try:
        MainFunc.googleSearch(keyword)
        return send_file('D:/KULIAH/Data Kuliah/UNOFFICIAL PROJECT/Web Crawler/Backend-Python/result.xlsx')
    except Exception as e:
            return str(e)

# @app.route('/crawl/<path:target_url>', methods=['GET'])
# def crawl(target_url):
#     try:
#         result = MainFunc.Crawler(target_url)
#         return jsonify(result)
#     except Exception as e:
#         return str(e)

if __name__ == '__main__':
    app.run(debug=True)
