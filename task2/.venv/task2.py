from flask import Flask,request,jsonify

app = Flask(__name__)

def checkRequest(request_data):
    authorizedSellerIDs = []
    unathorizedSales = []

    for item in request_data["productListings"]:
        authorizedSellerIDs.append(item["authorizedSellerID"])

    for sale in request_data["salesTransactions"]:
        if(sale['sellerID']) not in authorizedSellerIDs:
            unathorizedSales.append(sale['sellerID'])

    if len(unathorizedSales)>=1:
        return {"unauthorizedSales": [{"productID": "123", "unauthorizedSellerID": unathorizedSales}]}, 200
    else:
        return "NOT OK", 400      


@app.route('/info', methods=['POST'])
def task2():
    data = request.get_json()
    return checkRequest(data)