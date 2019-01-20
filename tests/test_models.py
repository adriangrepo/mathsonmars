#! ../env/bin/python
# -*- coding: utf-8 -*-
import sys
print("TestModels sys.path: {0}".format(sys.path))
import unittest

from mathsonmars.models import db, User, Role
from mathsonmars import create_app
from mathsonmars.constants.modelconstants import RoleTypes, DefaultUserName
create_user = False


class TestModels(unittest.TestCase):
    def test_user_save(self):
        """ Test Saving the user model to the database """
        app = create_app('mathsonmars.settings.TestConfig')
        db.app = app
        db.drop_all()
        db.create_all()
        with app.app_context():
            admin_role = Role(role_name = RoleTypes.ADMIN)
            db.session.add(admin_role)
            db.session.flush()
            admin = User(role_id = admin_role.id, user_name='admin', password='supersafepassword')
            db.session.add(admin)
            db.session.commit()

            user = db.session.query(User).filter(User.user_name == "admin").first()
        self.assertNotEqual(None, user)

    
    def test_user_password(self):
        """ Test password hashing and checking """
        app = create_app('mathsonmars.settings.TestConfig')
        db.app = app
        db.drop_all()
        db.create_all()
        with app.app_context():
            admin_role = Role(role_name = RoleTypes.ADMIN)
            db.session.add(admin_role)
            db.session.flush()
            admin = User(role_id = admin_role.id, user_name='admin', password='supersafepassword')
            self.assertEqual('admin', admin.user_name)
            self.assertEqual(True, admin.is_correct_password('supersafepassword'))
        
    def test_contact_user(self):
        app = create_app('mathsonmars.settings.TestConfig')
        db.app = app
        db.drop_all()
        db.create_all()
        with app.app_context():
            contact_role = Role(role_name = RoleTypes.CONTACT)
            db.session.add(contact_role)
            db.session.flush()
            contact_user = User(role_id = contact_role.id, contact_name = 'test contact', email = 'contact@yahoo.com')
            db.session.add(contact_user)
            db.session.flush()
            contact_user = db.session.query(User).filter(User.email == "contact@yahoo.com").first()
            self.assertNotEqual(None, contact_user)
            
    def test_signup_user(self):
        app = create_app('mathsonmars.settings.TestConfig')
        db.app = app
        db.drop_all()
        db.create_all()
        with app.app_context():
            signup_role = Role(role_name = RoleTypes.SIGNUP)
            db.session.add(signup_role)
            db.session.flush()
            signup_user = User(role_id = signup_role.id, contact_name = DefaultUserName.PARENT_GUARDIAN_TEACHER, email = 'signup@yahoo.com')
            db.session.add(signup_user)
            db.session.flush()
            signup_user = db.session.query(User).filter(User.email == "signup@yahoo.com").first()
            self.assertNotEqual(None, signup_user)

if __name__ == "__main__":
    unittest.main()