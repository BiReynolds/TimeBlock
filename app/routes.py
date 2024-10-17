from flask import render_template, flash, redirect, get_flashed_messages, url_for
from app import app
from app.models import testUser,testBlockType,testTaskType,testTask,testTimeBlock
from app.forms import LoginForm

from datetime import datetime,timezone

## Temp test data ------------------------------------
# Users
users = {}
usersById = {}
for i in range(10):
    newUser = testUser(i,'test'+str(i),'pass'+str(i))
    usersById[i] = newUser
    users['test'+str(i)] = newUser

# Block Types
sleepBlock = testBlockType(0,'sleep',1,None,None,'D',0)
workBlock = testBlockType(1,'work',None,1,None,'W',0)
chillBlock = testBlockType(2,'chill',None,None,20,'M',0)

blockTypes = {'sleep':sleepBlock,
              'work':workBlock,
              'chill':chillBlock}
blockTypesById = {0:sleepBlock,
                  1:workBlock,
                  2:chillBlock}

#TaskTypes
doYourJob = testTaskType(0,"Do your job",300,1,None,None,'D',1,0)
takeALunchBreak = testTaskType(1,"Take a lunch break",60,1,None,None,'D',1,0)
playVideoGames = testTaskType(2,"Play video games",120,1,None,None,'D',2,0)
petThatDog = testTaskType(3,"Pet that dog",60,1,None,None,'D',2,0)
weeklyChillTask = testTaskType(4,"Weekly Chill Task",60,None,2,None,'W',2,0)
monthlyWorkTask = testTaskType(5,"Monthly Work Task",60,None,None,3,'M',1,0)

tasksTypesById = {
             0:doYourJob,
             1:takeALunchBreak,
             2:playVideoGames,
             3:petThatDog,
             4:weeklyChillTask,
             5:monthlyWorkTask}

taskTypesByBlockType = {
                    0:[],
                    1:[doYourJob,takeALunchBreak,monthlyWorkTask],
                    2:[playVideoGames,petThatDog,weeklyChillTask]}



## Helper functions
def user_login(username,password):
    if username in users: 
        if password == users[username].password:
            return True,'Successfully logged in!',users[username]
        else:
            return False,'Incorrect Password',None
    else:
        return False,'No such user',None
    

@app.route('/')
@app.route('/index')
def index():
    user = users['test1']
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

@app.route('/testScreen', methods=['GET','POST'])
def testScreen():
    return render_template('testScreen.html',title = 'Sign In')