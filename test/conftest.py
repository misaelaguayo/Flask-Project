# -*- coding: utf-8 -*-

import pytest
from flask_project.main import init_app

@pytest.fixture
def app():
    application = init_app()
    application.debug = True
    application.threaded = True
    return application