# import Flask
from flask import Flask, render_template, redirect, jsonify
from model import session, Contracts

# initialize flask app
app = Flask(__name__)

# retun homepage
@app.route('/')
def index():
    return render_template('index.html')

# return list of sample names
@app.route('/awards')
def awards():

    # empty array to hold award data
    contracts_array = []

    # place each award in a dict. and add to awards_array
    for contract in Contracts:

        contract_dict = {}

        contract_dict['Awarding_Agency'] = contract.Awarding_Agency
        contract_dict['Subtier_Agency'] = contract.Subtier_Agency
        contract_dict['Subtier_Code'] = contract.Subtier_Code
        contract_dict['Category'] = contract.Category
        contract_dict['POP_City'] = contract.POP_City
        contract_dict['POP_State'] = contract.POP_State
        contract_dict['POP_Zip'] = contract.POP_Zip
        contract_dict['Recipient_Name'] = contract.Recipient_Name
        contract_dict['Total_Obligation'] = contract.Total_Obligation
        # contract_dict['Latitude'] = contract.Latitude
        # contract_dict['Longitude'] = contract.Longitude

        contracts_array.append(contract_dict)

    return jsonify(contracts_array)

@app.route('/top10')
def top10():
    return render_template('anyMapChart.html')

if __name__ == '__main__':
  app.run(debug=True)




