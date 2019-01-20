from flask import g, render_template, redirect, url_for
from flask.ext.login import login_required, current_user
from mathsonmars.models import db, Base, User, Role, Student
from mathsonmars.constants.modelconstants import RoleTypes
from mathsonmars.marslogger import logger
from mathsonmars.report import report_view

@report_view.before_request
def before_request():
    g.user = current_user
    
@report_view.route('/report')
@login_required
def report():
    logger.debug(">>report()")
    user = g.user
    logger.debug("--report() user.role_id:{0}, type:{1} ".format(user.role_id, type(user.role_id)))
    role = db.session.query(Role).filter(Role.id == user.role_id).first()
    #first filter by logged in user properties
    if role.role_name == RoleTypes.PARENT or role.role_name == RoleTypes.GUARDIAN: 
        students = db.session.query(Student).filter(Student.parentid == user.id).all()
        logger.debug("--report() students:".format(students))
        return render_template('report/report.html')
    elif role.role_name == RoleTypes.TEACHER:
        students = db.session.query(Student).filter(Student.teacherid == user.id).all()
        logger.debug("--report() students:".format(students))
        return render_template('report/report.html')
    elif role.role_name == RoleTypes.ADMIN:
        return render_template('report/report.html')
    logger.warn("--report() non parent/teacher/admin accessing report")
    return redirect(url_for("main_view.index"))
    
