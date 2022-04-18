# app/tests/test_config.py


import unittest

from flask import current_app
from flask_testing import TestCase

from app.server import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/user_service'
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.server.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/user_service'
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.server.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
