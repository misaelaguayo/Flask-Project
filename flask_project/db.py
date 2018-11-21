from pymongo import MongoClient

class MongoConnector(object):

	def __init__(self,app):
		self.app = app
		uri = "mongodb+srv://admin:753951ma@cluster0-ru4rr.mongodb.net/test?retryWrites=true"
		self.db = MongoClient(uri)

	def insert_user(self,data):
		return self.db.App.Users.insert_one(data).inserted_id
	def get_user(self,email):
		return self.db.App.Users.find_one({"email":email})

if __name__ == "__main__":
	db_connector = MongoConnector(None)
	data = {
		"name": "Misael Aguayo",
		"email": "aguayo.misael@gmail.com",
		"password": "abcdacd",
		"username": "misaelaguayo"
		}
	db_connector.insert_user(data)
	print(db_connector.get_user("aguayo.misael@gmail.com"))

	