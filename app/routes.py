from flask import render_template, flash, redirect, get_flashed_messages,url_for
from app import app
from app.forms import LoginForm

## Temp test data
users = {}
for i in range(10):
    users['test'+str(i)] = ['test'+str(i),'pass'+str(i)]

## Helper functions
def user_login(username,password):
    if username in users: 
        if password == users[username][1]:
            return True,'Successfully logged in!',users[username]
        else:
            return False,'Incorrect Password',None
    else:
        return False,'No such user',None
    

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'guest',
            'password':''}
    return render_template('index.html',user=user)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        logged_in,login_message,logged_in_user = user_login(form.username.data,form.password.data)
        flash('Login requested for user {}: {}'.format(
            form.username.data,login_message))
        if logged_in:
            user = logged_in_user
            return redirect(url_for('index'))
        else:
            render_template('login.html', title='Sign In', form=form)
    return render_template('login.html', title='Sign In', form=form)