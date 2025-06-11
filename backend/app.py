import os,pymongo
from dotenv import  load_dotenv
from urllib.parse import quote_plus
from  flask import  Flask,render_template,request,jsonify
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv(dotenv_path='backend/.env')

username = quote_plus(os.getenv('username'))
password = quote_plus(os.getenv('password'))
app_name = quote_plus(os.getenv('app_name'))

client  = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{app_name}.zu2cbek.mongodb.net/?retryWrites=true&w=majority&appName={app_name}")
db      = client.flask_db
collect = db['flask-project']

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup_user():
    email    = request.form['email']
    username = request.form['username']
    password = request.form['password']
    user     = collect.find_one({"username": username})
    if not user:
        hashed_pw = generate_password_hash(password)
        collect.insert_one({"email": email,"password": hashed_pw,"username":username})
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"error": "User already exists"}), 400

@app.route('/signin', methods=['POST'])
def signin_user():
    email     = request.form['email']
    password  = request.form['password']
    user      = collect.find_one({"email": email})
    if user:
        if check_password_hash(user['password'], password):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid password"}), 401
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/view_user', methods=['GET'])
def user_list():
    users       = collect.find()
    users_lst   = [{'id':str(user['_id']),'email':user['email'],'username':user['username']} for user in users]
    return jsonify({"result":users_lst})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)