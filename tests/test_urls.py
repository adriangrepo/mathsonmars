#! ../env/bin/python
# -*- coding: utf-8 -*-
import sys
print("TestURLs sys.path: {0}".format(sys.path))
import unittest

from mathsonmars.models import db, User, Role
from mathsonmars import create_app
from mathsonmars.constants.modelconstants import RoleTypes, DefaultUserName
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

create_user = False


class TestURLs(unittest.TestCase):
    
    def setUp(self):
        #admin._views = []
        #rest_api.resources = []
        app = create_app('mathsonmars.settings.TestConfig')
        self.client = app.test_client()
        self.app = app
        db.app = app
        
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_home(self):
        """ Tests if the home page loads """
        rv = self.client.get('/')
        assert rv.status_code == 200

    def test_login(self):
        """ Tests if the login page loads """

        rv = self.client.get('/login')
        assert rv.status_code == 200

    def test_logout(self):
        """ Tests if the logout page loads """

        rv = self.client.get('/logout')
        assert rv.status_code == 302

    def test_restricted_logged_out(self):
        """ Tests if the restricted page returns a 302
            if the user is logged out
        """

        rv = self.client.get('/restricted')
        assert rv.status_code == 302

    def test_restricted_logged_in(self):
        """ Tests if the restricted page returns a 200
            if the user is logged in
        """
        with self.app.app_context():
            admin_role = Role(role_name = RoleTypes.ADMIN)
            db.session.add(admin_role)
            db.session.flush()
            admin = User(role_id = admin_role.id, user_name='admin', password='supersafepassword')
            db.session.add(admin)
            db.session.commit()

        self.client.get('/login', data=dict(
            username='admin',
            password="supersafepassword"
        ), follow_redirects=True)

        rv = self.client.get('/restricted')
        logger.debug("--test_restricted_logged_in() code:{0}, rv:{1}".format(rv.status_code, rv))
        assert rv.status_code == 302

if __name__ == "__main__":
    unittest.main()