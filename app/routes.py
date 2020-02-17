from flask import render_template,flash,redirect,url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Filip'}
    posts = [{'author':{'username': 'Michał'},
              'body':'Cudowny dzien dzis!'},
             {'author': {'username': 'Jan'},
              'body': 'Co tam mordy?!'}
             ]
    return render_template('index.html', title='Home', user=user,posts=posts)

@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me{}'.format(
            form.username.data,form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html',form=form,title='Sign in')