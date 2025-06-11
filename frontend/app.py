import os,requests,json
from  datetime import  datetime
from dotenv import  load_dotenv
from  flask import  Flask,render_template,request

load_dotenv(dotenv_path='frontend/.env')

backend_url = os.getenv('backend_url')
app         = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    day_of_week = datetime.today().strftime('%A')
    return render_template('signup.html',day=day_of_week)

@app.route('/signup', methods=['GET','POST'])
def signup_user():
    if request.method == 'POST':
        email    = request.form['email']
        username = request.form['username']
        password = request.form['password_confirm']
        data     = {'email':email,'username':username,'password':password}
        response = requests.post(f"{backend_url}/signup",data=data)
        if response.status_code == 201:
            return render_template('signup.html', message='User registered successfully!', success=True)
        else:
            error_msg = json.loads(response.text)
            return render_template('signup.html', message=error_msg, success=False)
    return render_template('signup.html')

@app.route('/signin', methods=['GET','POST'])
def signin_user():
    if request.method == 'POST':
        email     = request.form['email']
        password  = request.form['password']
        data      = {'email': email,'password': password}
        response  = requests.post(f"{backend_url}/signin", data=data)
        if response.status_code == 200:
            return render_template('signin.html', message='User logged in successfully!', success=True)
        else:
            error_msg = json.loads(response.text)
            return render_template('signin.html', message=error_msg, success=False)
    return render_template('signin.html')

@app.route('/get_users', methods=['GET'])
def user_list():
    response    = requests.get(f"{backend_url}/view_user")
    return  response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)