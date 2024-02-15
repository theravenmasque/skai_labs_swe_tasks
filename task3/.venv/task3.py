from flask import Flask, request,jsonify

app = Flask(__name__)

def checkRequest(request_data):
    overlaps = 0
    list3 = [item1 for item1, item2 in zip(request_data['end_times'][:-1], request_data['start_times'][1:]) if item1 >= item2]
    overlaps = len(list3)

    if overlaps==0:
        return {"max_interviews" : 0},400  
    else:
        return{"max_interviews": overlaps}, 200


@app.route("/info", methods=['POST'])

def task3():
    data = request.get_json()
    return checkRequest(data)