from flask import render_template, redirect, request, url_for, flash
from . import auth
from .forms import LoginForm,RegForm
from app.models import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.rememberme.data)
    if form.validate_on_submit():
        try:
            user = User.get(User.username == form.username.data)
            if user.verify_password(form.password.data):
                login_user(user, form.rememberme.data)
                return redirect(request.args.get('next') or url_for('admin.index'))
            else:
                flash('用户名或密码错误')
        except:
            flash('用户名或密码错误')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已退出登录')
    return redirect(url_for('auth.login'))


def is_usr_exist(name):
    user = User.select().where(User.username==name)
    if user.count() == 0:
        return False
    else:
        return True

def add_user(form):
    if is_usr_exist(form.username.data) is True:
        print("[*] Conflicts ")
        return False
    passwd_hash = generate_password_hash(form.password.data)
    new_usr = User(username=form.username.data, password=passwd_hash, phone=form.phone.data)
    new_usr.save()
    return True



@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegForm()
    if request.method == 'GET':
        return render_template('auth/register.html', form=form)
    elif request.method == 'POST':
        success = add_user(form)
        if success:
            return redirect(url_for('auth.login'))
        else:
            return render_template('errors/500.html')
    else:
        return render_template('errors/404.html')