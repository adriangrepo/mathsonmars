from flask import Blueprint

report_view = Blueprint('report_view', __name__)

from mathsonmars.report import reportview