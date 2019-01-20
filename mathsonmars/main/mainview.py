from flask import render_template, request, redirect, url_for, session, escape, send_from_directory, current_app
from flask.ext.login import current_user
from mathsonmars.models import db
from mathsonmars.extensions import cache
from mathsonmars.marslogger import logger
from mathsonmars.main import main_view
from mathsonmars.models import db, Role, Student
from mathsonmars.constants.modelconstants import RoleTypes


@main_view.route('/')
@cache.cached(timeout=1000)
def index():
    if 'user_name' in session:
        logger.debug( 'Logged in as {0}'.format(escape(session['user_name'])))
    return render_template('index.html')

@main_view.route('/features')
def features():
    return render_template('index.html', _anchor='features')

@main_view.route('/about')
def about():
    return render_template('index.html', _anchor='about')

@main_view.route('/privacy')
def privacy():
    return render_template('privacy.html')

@main_view.route('/faq')
def faq():
    return render_template('faq.html')

'''
@main_view.route('/robots.txt')
@main_view.route('/sitemap.xml')
def static_from_root():
    app = current_app._get_current_object()
    return send_from_directory(app.static_folder, request.path[1:])
'''






