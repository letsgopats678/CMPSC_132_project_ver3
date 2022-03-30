
function privateCheck() {

    if (document.getElementById('private').checked) {
        document.getElementById('ifPrivate').style.visibility = 'visible';
    }
    else {document.getElementById('ifPrivate').style.visibility = 'hidden';
         }
}

function calculate() {
let income, transportation,priv_tran, utilities, meal, household_size, misnsavings, rent;

income = parseInt(document.getElementById('income').value);
rent = income;
let min_rent = 300;

// Transportation
priv_tran = parseInt(document.getElementById('tran_cost').value);
if (document.getElementById('public').checked == false) {
  transportation = priv_tran;
} else {
  transportation = 82 + priv_tran;
}

//meal
if (document.getElementById('yes_mealp').checked) {
  meal = 167 + 280;
} else {
  meal = 296;
}

//utilities
household_size = parseInt(document.getElementById('Household_size').value);
utilities= (((9+household_size)/10)*200)/household_size;

// Miscellenious and savings
misnsavings = income * 0.15;

rent = income - transportation - meal - utilities - misnsavings;
document.getElementById("rent").innerHTML = "Rent: "+ rent;
document.getElementById("transportation").innerHTML = "Transportation: " + transportation;
document.getElementById("meal").innerHTML = "Meal: "+ meal;
document.getElementById("utilities").innerHTML = "Utilities: " + utilities;
document.getElementById("misnsavings").innerHTML = "Miscellenious and Savings: " + misnsavings;
document.getElementById("household").innerHTML = "Household Size: " + household_size;

}