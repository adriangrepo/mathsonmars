#! ../env/bin/python
# -*- coding: utf-8 -*-
import sys
print("TestLogin sys.path: {0}".format(sys.path))
import unittest
from mathsonmars import create_app
from mathsonmars.models import db, Role, User, BlockedIPForUser
import logging
from mathsonmars.constants.modelconstants import RoleTypes

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

create_user = True

class TestLogin(unittest.TestCase):
    def setUp(self):
        app = create_app('mathsonmars.settings.TestConfig')
        self.client = app.test_client()
        self.app = app
        db.app = app
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_login(self):
        """ Tests if the login form functions """
        with self.app.app_context():
            admin_role = Role(role_name = RoleTypes.ADMIN)
            db.session.add(admin_role)
            db.session.flush()
            admin = User(role_id = admin_role.id, user_name='admin', password='supersafepassword')
            db.session.add(admin)
            db.session.commit()
            rv = self.client.post('/login', data=dict(
                login_field='admin',
                password="supersafepassword"
            ), follow_redirects=True)

        assert rv.status_code == 200
        logger.debug("--test_login() rv.data:{0}".format(rv.data))
        #assert 'Logged in successfully.' in str(rv.data)
        assert 'Logout' in str(rv.data)

    '''
    def test_login_fail(self):
        """ Tests if the login form fails correctly """
        with self.app.app_context():
            rv = self.client.post('/login', data=dict(
                login_field='admin',
                password=""
            ), follow_redirects=True)

        assert rv.status_code == 200
        logger.debug("--test_login_fail() rv.data:{0}".format(rv.data))
        assert 'Incorrect email/username or password' in str(rv.data)
        assert 'Login' in str(rv.data)
    '''
        
    '''
    TODO debug why not working
    def test_multi_login_fail(self):
        """ Tests if the login form fails correctly """
        with self.app.app_context():
            admin_role = Role(role_name = RoleTypes.ADMIN)
            db.session.add(admin_role)
            db.session.flush()
            admin = User(role_id = admin_role.id, user_name='admin', password='supersafepassword')
            db.session.add(admin)
            db.session.commit()
            for i in range(12):
                rv = self.client.post('/login', data=dict(
                    login_field='admin',
                    password=""
                ), follow_redirects=True)
            user = db.session.query(User).filter(User.user_name=='admin').first()
            if user is not None:
                blocked_hacker = db.session.query(BlockedIPForUser).filter(User.id == user.id).first()
                logger.debug(blocked_hacker)
                assert blocked_hacker is not None
    '''

if __name__ == "__main__":
    unittest.main()