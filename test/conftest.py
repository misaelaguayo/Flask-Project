# -*- coding: utf-8 -*-

import pytest
from flask_project.main import app as application

@pytest.fixture
def app():
    application.debug = True
    application.threaded = True
    return application