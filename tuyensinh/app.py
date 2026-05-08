from flask import Flask, render_template, request, redirect, session
from routes.client import client_bp
from routes.admin import admin_bp

from models.user import db, User

app = Flask(__name__)

# SECRET KEY
app.secret_key = "123456"

# SQLITE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# KẾT NỐI DB
db.init_app(app)

# REGISTER BLUEPRINT
app.register_blueprint(client_bp)
app.register_blueprint(admin_bp, url_prefix="/admin")

# =========================
# ĐĂNG KÝ
# =========================
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = User(
            username=username,
            password=password,
            role='client'
        )

        db.session.add(user)
        db.session.commit()

        return redirect('/login')

    return render_template('client/register.html')

# =========================
# ĐĂNG NHẬP
# =========================
@app.route('/login', methods=['GET', 'POST'])
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

    return render_template('client/login.html')

# =========================
# ADMIN
# =========================
@app.route('/admin')
def admin():

    if session.get('role') != 'admin':
        return "Bạn không có quyền"

    return render_template('admin/index.html')

# =========================
# LOGOUT
# =========================
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')

# =========================
# CREATE DATABASE
# =========================
with app.app_context():
    db.create_all()

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)
