import pytest

from flask import url_for
from flask_project.models.user import User

class TestFlask:

	def test_home(self, client):
		assert client.get(url_for("index")).status_code == 200
		assert client.get(url_for("register")).status_code == 200
		assert client.get(url_for("logout")).status_code == 200
		
		u = User("misael","Aguayo.misael@gialmc.com")