

##
from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from models.user import User, db

client_bp = Blueprint(
    'client',
    __name__
)

# TRANG CHỦ
@client_bp.route('/')
def home():

    return render_template(
        'client/home.html'
    )
@client_bp.route('/ve-chung-toi')
def ve_chung_toi():

    return render_template(
        'client/about.html'
    )
# TUYỂN SINH
@client_bp.route('/tuyen-sinh')
def tuyen_sinh():

    return render_template(
        'client/tuyensinh.html'
    )
# LOGIN
@client_bp.route('/login',
                 methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        user = User.query.filter_by(
            username=username,
            password=password
        ).first()

        if user:

            session['user_id'] = user.id

            session['role'] = user.role

            # ADMIN
            if user.role == 'admin':

                return redirect('/admin')

            # CLIENT
            return redirect('/')

    return render_template(
        'client/login.html'
    )

# REGISTER
@client_bp.route('/register',
                 methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        new_user = User(
            username=username,
            password=password,
            role='client'
        )

        db.session.add(new_user)

        db.session.commit()

        return redirect('/login')

    return render_template(
        'client/login.html'
    )

# LOGOUT
@client_bp.route('/logout')
def logout():

    session.clear()

    return redirect('/login')