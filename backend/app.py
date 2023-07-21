from flask import Flask
from flask import jsonify ,request
from flask_cors import CORS, cross_origin
from api_func_call import send_and_receive_ans
app = Flask(__name__)


@app.route('/chat')
@cross_origin(origin='*')
def chatbot():
    message = request.args.get('text')
    return_message = send_and_receive_ans(message)
    response = {"message": return_message}
    return jsonify(response)

if __name__ =='__main__':
          app.run(host='0.0.0.0',port='3000')
