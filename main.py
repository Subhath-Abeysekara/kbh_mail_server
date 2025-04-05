from flask import Flask, request
from flask_cors import CORS, cross_origin

from report_generation import kbh_product_report, kbh_sales_report, kbh_order_report

app = Flask(__name__)
CORS(app, resources={r"/": {"origins": "*"}})

@app.route("/")
def main():
    return "home"

@app.route("/report/product", methods=["POST"])
@cross_origin()
def get_product_report_kbh():
    try:
        if request.data:
            body = request.json
            print(body)
            kbh_product_report(body['data'])
            return {
                'state': True,
            }
        else:
            return {
                "state": False,
                "message": "no body"
            }
    except Exception as e:
        print(str(e))
        return {
            "state": False,
            "message": "error"
        }

@app.route("/report/sales", methods=["POST"])
@cross_origin()
def get_sale_report_kbh():
    try:
        if request.data:
            body = request.json
            print(body)
            kbh_sales_report(body['data'])
            return {
                'state': True,
            }
        else:
            return {
                "state": False,
                "message": "no body"
            }
    except Exception as e:
        print(str(e))
        return {
            "state": False,
            "message": "error"
        }

@app.route("/report/order", methods=["POST"])
@cross_origin()
def get_order_report_kbh():
    try:
        if request.data:
            body = request.json
            print(body)
            kbh_order_report(body['data'])
            return {
                'state': True,
            }
        else:
            return {
                "state": False,
                "message": "no body"
            }
    except Exception as e:
        print(str(e))
        return {
            "state": False,
            "message": "error"
        }

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
