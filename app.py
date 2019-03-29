from eospy.cleos import Cleos
from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api

app = Flask(__name__)
CORS(app)
api = Api(app)

##
ce = Cleos('https://api.eosnewyork.io')
##

class Welcome(Resource):
    def get(self):
        return {'message': 'Welcome on eosjson.io'}

##

class Account(Resource):
    def get(self, name):

        act_name = name
        
        try:
            account_data = ce.get_account(act_name)
            return account_data

        except:    
            return {'message': 'Account data not found'}, 404 

##

class Table(Resource):
    def get(self):

        table_contract = request.args.get('contract', type=str)
        table_scope = request.args.get('scope', type=str)
        table_table = request.args.get('table', type=str)
        
        try:
            table_data = ce.get_table(table_contract, table_scope, table_table)
            return table_data

        except:    
            return {'message': 'Table data not found'}, 404 

##

class Currency(Resource):
    def get(self):

        currency_contract = request.args.get('contract', type=str)
        currency_account = request.args.get('account', type=str)
        currency_symbol = request.args.get('symbol', type=str)
        
        try:
            currency_data = ce.get_currency_balance(currency_account, currency_contract, currency_symbol)
            return currency_data

        except:    
            return {'message': 'Currency Balance data not found'}, 404 

##

class Abi(Resource):
    def get(self, name):

        abi_account = name
        
        try:
            abi_data = ce.get_abi(abi_account)
            return abi_data

        except:    
            return {'message': 'Abi data not found'}, 404 

##

class Block(Resource):
    def get(self, number):

        block_nr = number
        
        try:
            block_data = ce.get_block(block_nr)
            return block_data

        except:    
            return {'message': 'Block data not found'}, 404 
##

class Info(Resource):
    def get(self):
        
        try:
            info_data = ce.get_info()
            return info_data

        except:    
            return {'message': 'Info data not found'}, 404 

##

api.add_resource(Account, '/api/account/<string:name>')
api.add_resource(Table, '/api/table')
api.add_resource(Currency, '/api/currency')
api.add_resource(Abi, '/api/abi/<string:name>')
api.add_resource(Block, '/api/block/<int:number>')
api.add_resource(Info, '/api/info')
api.add_resource(Welcome, '/api')

##

if __name__ == '__main__':
    app.run(debug=True)