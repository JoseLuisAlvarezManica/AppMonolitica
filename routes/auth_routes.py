from flask import Blueprint, render_template, session

auth_bp = Blueprint('auth', __name__, template_folder='../templates')

