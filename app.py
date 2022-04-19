from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])

def calculate():
    rent = 0
    transportation = 0
    utilities = 0
    meal = 0
    misnsavings = 0
    household_size = 0
    if request.method == 'POST' and 'income' in request.form and 'Household_size' in request.form:
        income = float(request.form.get('income'))
        min_rent = 300

        #Transportation
        priv_tran = float(request.form.get('tran_cost'))
        if request.form.get('tran_cost'):
            transportation = 82 + priv_tran
        else:
            transportation = priv_tran

        #meal
        if request.form.get('yes_mealp'):
            meal = 167 +  280
        else:
            meal = 296

        #utilities
        household_size = int(request.form.get('Household_size'))
        utilities = (((9 + household_size)/10)*200)/household_size

        #miscellenious and savings
        misnsavings = income * 0.15
        rent =(income - transportation - meal - utilities - misnsavings)
    return render_template('Home.html', rent=rent, transportation=transportation, meal=meal, utilities=utilities, misnsavings=misnsavings, household_size=household_size)


if __name__ == '__main__':
    app.run()
