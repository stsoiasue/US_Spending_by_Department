# import Flask
from flask import Flask, render_template, redirect, jsonify
from model import session, Awards

# initialize flask app
app = Flask(__name__)

# retun homepage
@app.route('/')
def index():
    return render_template('index.html')

# return list of sample names
@app.route('/awards')
def awards():

    # query db for awards
    gov_awards = session.query(Awards)

    # empty array to hold award data
    awards_array = []

    # place each award in a dict. and add to awards_array
    for award in gov_awards:

        award_dict = {}

        award_dict['awarding_agency'] = award.awarding_agency
        award_dict['date_signed'] = award.date_signed
        award_dict['recipient_name'] = award.recipient_name
        award_dict['recipient_zip'] = award.recipient_zip
        award_dict['total_obligation'] = award.total_obligation

        awards_array.append(award_dict)

    return jsonify(awards_array)

if __name__ == '__main__':
  app.run(debug=True)