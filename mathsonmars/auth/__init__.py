from flask import Blueprint

auth_view = Blueprint('auth_view', __name__)

from mathsonmars.auth import authview