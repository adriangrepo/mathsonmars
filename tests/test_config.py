#! ../env/bin/python
# -*- coding: utf-8 -*-
import sys
print("TestConfig sys.path: {0}".format(sys.path))
from mathsonmars import create_app
import unittest

class TestConfig(unittest.TestCase):
    
    def test_dev_config(self):
        """ Tests if the development config loads correctly """

        app = create_app('mathsonmars.settings.DevConfig')
        self.assertEqual('dev', app.config['ENV'])
        self.assertEqual(True, app.config['DEBUG'])
        #self.assertEqual('sqlite:///../database.db', app.config['SQLALCHEMY_DATABASE_URI'])
        self.assertEqual('null', app.config['CACHE_TYPE'] )

    def test_test_config(self):
        """ Tests if the test config loads correctly """

        app = create_app('mathsonmars.settings.TestConfig')
        self.assertEqual('test', app.config['ENV'])
        self.assertEqual(True, app.config['DEBUG'])
        self.assertEqual(True, app.config['SQLALCHEMY_ECHO'])
        self.assertEqual('null', app.config['CACHE_TYPE'] )

    def test_prod_config(self):
        """ Tests if the production config loads correctly """

        app = create_app('mathsonmars.settings.ProdConfig')
        self.assertEqual('prod', app.config['ENV'])
        #self.assertEqual("postgresql://deployer:samsung@localhost/mathsonmars_db", app.config['SQLALCHEMY_DATABASE_URI'])
        #self.assertEqual('/home/deployer/mathsonmars/mathsonmars/logger_out.txt', app.config['SQLALCHEMY_DATABASE_URI'])
        self.assertEqual( 'simple', app.config['CACHE_TYPE'])

if __name__ == "__main__":
    unittest.main()