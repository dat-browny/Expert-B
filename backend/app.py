from flask import Flask
from flask import jsonify ,request
from flask_cors import CORS, cross_origin
from api_func_call import send_and_receive_ans

# CORS(app)

app = Flask(__name__)
          
@app.route("/")
# @cross_origin(origin='*')
def hello_world():
    return "<p>Hello, World!</p>"
@app.route('/chat')
@cross_origin()
def chatbot():
    message = request.args.get('text')
    return_message = send_and_receive_ans(message)
    response = {"message": return_message}
    return jsonify(response)

if __name__ =='__main__':
        
        app.run()
