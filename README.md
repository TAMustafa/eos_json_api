# EOS JSON API
A convenient way to lookup JSON data on the EOS Blockchain.<br> 

**Please note that the API is still work in progress and endpoints might change.**

## Getting Started
These instructions will give a brief overview of the EOS API **GET** endpoints that are currently available to use.<br>

The api is currently hosted on Heroku under the following URL:<br>
`https://eos-easy-json-api.herokuapp.com/`

-----------------------------------------------------

### Get_Account
Returns an object containing various details about a specific account on the EOS blockchain.

**Parameter** <br>
- `name` TEXT - The name of the account to retrieve

`/account/eos_account_name`

**Example:**
https://eos-easy-json-api.herokuapp.com/account/tareknanobnk

------------------------------------------------------

### Get_Table
Returns an object containing rows from the specified table.

**Parameter**<br>
- `contract` TEXT - The contract who owns the table<br>
- `scope` TEXT - The scope within the contract in which the table is found<br>
- `table` TEXT - The name of the table as specified by the contract abi

`/table&contract=value?scope=value?table=value`

**Example:**
https://eos-easy-json-api.herokuapp.com/table?contract=eosio.msig&scope=eosnewyorkio&table=approvals

------------------------------------------------------

### Get_Currency_Balance
Retrieve the balance of an account for a given currency

**Parameter**<br>
`account` TEXT - The account to query balances for<br>
`contract` TEXT - The contract that operates the currency<br>
`symbol` TEXT - The symbol for the currency if the contract operates multiple currencies

`/currency&account=value?contract=value?symbol=value`

**Example:**
https://eos-easy-json-api.herokuapp.com/currency?account=tareknanobnk&contract=eosio.token&symbol=eos

---------------------------------------------------------------

### Get_ABI
Retrieve the ABI for an account

**Parameter** <br>
- `name` TEXT - The name of the account whose abi should be retrieved

`/abi/eos_account_name`

**Example:**
https://eos-easy-json-api.herokuapp.com/abi/eosio

-----------------------------------------------------------

### Get_Block
Retrieves a full block from the blockchain.

**Parameter** <br>
- `number` NUMBER - The number or ID of the block to retrieve

`/block/50022875`

**Example:**
https://eos-easy-json-api.herokuapp.com/block/50022875

----------------------------------------------------

### Get_Info
Retrieve current blockchain information.

**Parameter** <br>
- `none`

`/info`

**Example:**
https://eos-easy-json-api.herokuapp.com/info

-------------------------------------------------

## Built With
- Flask RESTfull
- Python 3.7.2

## License
This project is licensed under the MIT License.

## Acknowledgments
I would not be able to create this API endpoint without the help from **Deck** (EOS NewYork) and the 
awesome Python Library "eospy" EOS NewYork created.

Please checkout https://github.com/eosnewyork/eospy for more information!
