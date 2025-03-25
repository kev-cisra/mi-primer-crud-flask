from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db import db 

users = Blueprint('users', __name__)

@users.route('/users')
def index():
    return render_template('users.html')