from flask import Flask, url_for, redirect, render_template, session
from flask_dance.contrib.github import make_github_blueprint, github
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

gitBlueprint = make_github_blueprint(
    client_id='______________________',
    client_secret='_____________________________',
    redirect_to="callback"
)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app.register_blueprint(blueprint=gitBlueprint, url_prefix="/git-login")

@app.route('/log-in')
def gitLogin():
    global repos
    if not github.authorized:
        return redirect(url_for("github.login"))  # Redirect to GitHub OAuth login
    resp = github.get("/user")
    print(github)
    if resp.ok:
        userInfo = resp.json()
        session['github_info'] = userInfo
        session['github_id'] = userInfo['login']  # Save GitHub username in session

        # repositry response . . .
        repo = github.get("/user/repos")
        if repo.ok:
            repos = repo.json()
        else:
            repos = []
        return redirect(url_for('main'))
    return "Failed to fetch GitHub user info", 400
@app.route('/log-out')
def logout():
    session.clear()
    return redirect(url_for('loginReq'))

@app.route('/login-req')
def loginReq():
    return render_template('login.html')

@app.route('/callback')  # This route is the callback after GitHub authorization
def callback():
    if github.authorized:
        return redirect(url_for('main'))
    return "GitHub authentication failed", 400

@app.route('/')
@app.route('/main')
def main():
    if 'github_id' not in session:
        return redirect(url_for('loginReq'))
    return render_template(
        'index.html',
        username=session['github_id'],
        userinfo = session['github_info'],
        repos = repos
    )
