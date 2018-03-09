# import Flask
from flask import Flask, render_template, redirect, jsonify
from model import session, Contracts, Top_Contracts

# initialize flask app
app = Flask(__name__)

# retun homepage
@app.route('/')
def index():
    return render_template('index2.html')

# return list of awards names
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
        contract_dict['Latitude'] = contract.Latitude
        contract_dict['Longitude'] = contract.Longitude
        contract_dict['Description'] = contract.Description
        contract_dict['Contract_ID'] = contract.Contract_ID

        contracts_array.append(contract_dict)

    return jsonify(contracts_array)

# return list of top awards names
@app.route('/top_awards')
def top_awards():

    # empty array to hold award data
    top_contracts_array = []

    # place each award in a dict. and add to awards_array
    for top_contract in Top_Contracts:

        contract_dict = {}

        contract_dict['Awarding_Agency'] = top_contract.Awarding_Agency
        contract_dict['Subtier_Agency'] = top_contract.Subtier_Agency
        contract_dict['Subtier_Code'] = top_contract.Subtier_Code
        contract_dict['Category'] = top_contract.Category
        contract_dict['POP_City'] = top_contract.POP_City
        contract_dict['POP_State'] = top_contract.POP_State
        contract_dict['POP_Zip'] = top_contract.POP_Zip
        contract_dict['Recipient_Name'] = top_contract.Recipient_Name
        contract_dict['Total_Obligation'] = top_contract.Total_Obligation
        contract_dict['Latitude'] = top_contract.Latitude
        contract_dict['Longitude'] = top_contract.Longitude
        contract_dict['Description'] = top_contract.Description
        contract_dict['Contract_ID'] = top_contract.Contract_ID
        # contract_dict['Percentage_of_Dept'] = top_contract.Percentage_of_Dept
        # contract_dict['Percentage_of_Total'] = top_contract.Percentage_of_Total

        top_contracts_array.append(contract_dict)

    return jsonify(top_contracts_array)

@app.route('/top10')
def top10():
    return render_template('anyMapChart.html')

@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')

@app.route('/spending_data')
def spending_data():
    return render_template('spending_data.html')

if __name__ == '__main__':
  app.run(debug=True)




