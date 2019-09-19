from flask import Blueprint, render_template, request
import hash
auth = Blueprint('auth',__name__)

@auth.route("/login", methods=["GET","POST"])
def login
