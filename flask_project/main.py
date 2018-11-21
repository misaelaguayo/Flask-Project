from flask_login import LoginManager, current_user,login_user, logout_user
from flask import Flask, render_template, abort, request,url_for,redirect,flash

from flask_project.models.user import User

def init_app():
	app = Flask("myapp")
	app.secret_key = "asldkfjpaosdicmpaosdfh"

	login_manager = LoginManager()
	login_manager.init_app(app)
	login_manager.login_view = "login"

	sample_user = {
		"name":"Misael",
		"email":"misael.aguayo@ttu.edu",
		"password":"password"
	}
	@login_manager.user_loader
	def load_user(email):
		if email == sample_user["email"]:
			return User(sample_user["name"],sample_user["email"])
		return None

	@app.route("/")
	def index():
		return render_template("index.html")
		
	@app.route("/login", methods = ["GET","POST"])
	def login():
		if request.method == "POST":
			print(dict(request.form))
			email = request.form.get("email")
			password = request.form.get("password")
			if password == sample_user["password"]:
				user = User(sample_user["name"],sample_user["email"])
				login_user(user)
				return redirect(url_for("index"))
			flash("Incorrect password")
			return redirect(url_for("index"))
			
		return render_template("login.html")
		
	@app.route("/register")
	def register():
		return "This is the registration page"
		
	@app.route("/logout")
	def logout():
		return "This is the logout page"
	
	return app
if __name__ == "__main__":
	init_app().run(host = "0.0.0.0",port = 80)