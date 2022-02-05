import flask
from flask import Flask
from flask import jsonify, request, make_response
# import CORS to be able to get the information form another port or device through the Browser
from flask_cors import CORS
# For making a websocket to communicate to
from flask_socketio import SocketIO


app = Flask(__name__)
socketioSocket = SocketIO(app, cors_allowed_origins="*")

CORS(app)

@app.route("/", methods=["GET"])
def __main():
    print(request.headers)
    socketioSocket.emit("message", "new data available", broadcast=True)
    return make_response("api is running", 200)

if __name__ == '__main__':
    # https start
    socketioSocket.run(app, host="0.0.0.0")