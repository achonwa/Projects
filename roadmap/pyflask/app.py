from flask import Flask, redirect, url_for, session, request
from requests_oauthlib import OAuth2Session
import os

# Replace these with your app's credentials
CLIENT_ID = 'Ov23li03IjTGIMlKaqzz'
CLIENT_SECRET = '40c3b07180f8e3455d93668984c2fc73b88c519f'
AUTHORIZATION_BASE_URL ='https://github.com/login/oauth/authorize'
TOKEN_URL = 'https://github.com/login/oauth/access_token'
API_BASE_URL ='https://api.github.com/user'
REDIRECT_URI ='http://127.0.0.1:5000/callback'

# Allow insecure transport for local development (http instead of https)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

 #initialize the flask app

app = Flask(__name__)
app.secret_key = 'a_random_secret_key'

#  step 1 : ROUTE TO LOGIN 

@app.route('/')
def home():
    return'<a href="/login"> login with Github </a>'

@app.route('/login')
def login():
    #create an oauth2 session
    github = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, state = github.authorization_url(AUTHORIZATION_BASE_URL)
   # Save the state in the session for security purposes
    session['oauth_state'] = state 
    return redirect(authorization_url)

# Step 2: Handle Callback
@app.route('/callback')
def callback():

    github = OAuth2Session(CLIENT_ID, state =session['oauth_state'], redirect_uri=REDIRECT_URI)

    #FETCH ACCESS TOKEN
    token = github.fetch_token(TOKEN_URL, client_secret=CLIENT_SECRET, authorization_response = request.url)
    session['oauth_token'] = token

    return redirect(url_for('profile'))

#step 3: fetch user profile
@app.route('/profile')
def profile():
    # Use the token to access the API
    github = OAuth2Session(CLIENT_ID, token=session['oauth_token'])
    user_info = github.get(API_BASE_URL).json()

    return f'<h1>Logged in as {user_info["login"]}</h1><pre>{user_info}</pre>'

if __name__ == '__main__':
    app.run(debug=True)

