import sys
import pymongo
from pymongo import MongoClient
from flask import Flask
from flask import render_template
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api*": {"origins": "*"}})

cors.init_app(app)
api = Api(app)

mycliend = MongoClient()
carddb = mycliend['carddb']
cards = carddb['cards']
users = carddb['users']

acc_args = reqparse.RequestParser()
acc_args.add_argument("username",type=str,help="username is required",required = True)
acc_args.add_argument("password",type=str,help="password is required",required = True)

card_args = reqparse.RequestParser()
card_args.add_argument("number",type=int,help="card number is required",required = True)
card_args.add_argument("pin",type=int,help="pin is required",required = True)

sendcard_args = reqparse.RequestParser()
sendcard_args.add_argument("number",type=int,help="card number is required",required = True)
sendcard_args.add_argument("pin",type=int,help="pin is required",required = True)
sendcard_args.add_argument("sendto",type=int, help = "receiver card number is required",required = True)
sendcard_args.add_argument("amount",type=int,help = "ammunt is required",required = True)


tok_field = {
	"token":fields.String
}
balance_field = {
	"balance":fields.Integer
}

class Login(Resource):
	@marshal_with(tok_field)
	def post(self):
		args = acc_args.parse_args()

		if len(args['username'])<1:
			abort(401,error="username can't be blank")

		if len(args['password'])<1:
			abort(401,error="password can't be blank")

		try:
			result = users.find({"username":args['username']})[0]
		except:
			abort(401,error="Card information is incorrect")



		if result["password"]!=args["password"]:
			abort(401,error="Password is incorrect")

		token = secrets.token_hex(20)
		result['token'] = token

		return {"token":token}, 200


	def options (self):
	    return {'Allow' : 'POST' }, 200, \
	    { 'Access-Control-Allow-Origin': '*', \
	      'Access-Control-Allow-Methods' : 'POST' ,
	      "Access-Control-Allow-Headers":"content-type"}


class getBalance(Resource):
	@marshal_with(balance_field)
	def post(self):
		args = card_args.parse_args()

		if len(str(args['number']))!=16:
			abort(401,error="Card format is incorrect")

		if len(str(args['pin']))!=4:
			abort(401,error="Pin format is incorrect")
		
		try:
			result = cards.find({"number":args['number']})[0]
		except:
			abort(401,error="Card information is incorrect")


		if result["pin"]!=args["pin"]:
			abort(401,error="Pin is incorrect")

		return {"balance":result['balance']}, 200


	def options (self):
	    return {'Allow' : 'POST' }, 200, \
	    { 'Access-Control-Allow-Origin': '*', \
	      'Access-Control-Allow-Methods' : 'POST' ,
	      "Access-Control-Allow-Headers":"content-type"}


class sendMoney(Resource):
	@marshal_with(balance_field)
	def post(self):
		args = sendcard_args.parse_args()


		if len(str(args['number']))!=16:
			abort(401,error="Card format is incorrect")

		if len(str(args['sendto']))!=16:
			abort(401,error="Card format is incorrect")

		if len(str(args['pin']))!=4:
			abort(401,error="Pin format is incorrect")

		if args['amount']<0:
			abort(401,error="Amount can't be negative")

		if args['number']==args['sendto']:
			abort(401,error="You can not send money to yourself")
		try:
			result = cards.find({"number":args['number']})[0]
		except:
			abort(401,error="Card information is incorrect")

		if result["pin"]!=args["pin"]:
			abort(401,error="Pin is incorrect")

		try:
			toresult = cards.find({"number":args['sendto']})[0]
		except:
			abort(401,error="Receive card information is incorrect")

		if args['amount']>result['balance']:
			abort(401,error="Insufishent funds")

		result['balance']-=args['amount']
		toresult['balance']+=args['amount']
		cards.update_one({"_id":result["_id"]},{"$set":{"balance":result['balance']}})
		cards.update_one({"_id":toresult["_id"]},{"$set":{"balance":toresult['balance']}})

		return {"balance":result['balance']}, 200


	def options (self):
	    return {'Allow' : 'POST' }, 200, \
	    { 'Access-Control-Allow-Origin': '*', \
	      'Access-Control-Allow-Methods' : 'POST' ,
	      "Access-Control-Allow-Headers":"content-type"}




@app.route("/")
def homehtml():
  return render_template("bd.json")
def main():
	api.add_resource(Login,"/api/login")
	api.add_resource(getBalance,"/api/balance")
	api.add_resource(sendMoney,"/api/send")

	#carddict = {"number":4790729914729354,'pin':6769,'balance':0}
	#cards.insert_one(carddict)
	#result = cards.find({'number':4790729914729354})
	#users.insert({"username":"user","password":"pass"})
	app.run(debug=True)

	#print(result[0]['pin'])

if __name__=="__main__":
	main()