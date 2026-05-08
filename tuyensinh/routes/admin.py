
from flask import Blueprint, render_template

admin_bp = Blueprint(
    'admin',
    __name__
)

@admin_bp.route('/')
def dashboard():

    return render_template(
        'admin/dashboard.html'
    )

@admin_bp.route('/applicants')
def applicants():

    return render_template(
        'admin/applicants.html'
    )

@admin_bp.route('/majors')
def majors():

    return render_template(
        'admin/majors.html'
    )

@admin_bp.route('/admissions')
def admissions():

    return render_template(
        'admin/admissions.html'
    )

@admin_bp.route('/news')
def news():

    return render_template(
        'admin/news.html'
    )

@admin_bp.route('/users')
def users():

    return render_template(
        'admin/users.html'
    )