
from budget_app import app

from flask import Flask, render_template, request, redirect, session, flash

from budget_app.models import users, main_bills ,budget

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register_form():

    return render_template('index.html')

@app.route('/create', methods = ['POST'])
def register():

    if request.form['action'] == 'register':

        if not users.User.validate(request.form):
            return redirect('/register')

        pw_hash = bcrypt.generate_password_hash(request.form["password"])

        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password': pw_hash
        
        }

        user_info = users.User.save(data)

        # budget.Budget.save({"id" : user_info})

        session['user_info'] = user_info
        


    else:


        user_info = users.User.get_onewith_email ({'email': request.form['email'].lower()})
        print(user_info)
        if user_info:
            if len(request.form['password']) < 8:
                flash("Password must be at least 8 characters")
                return redirect("/register")
            if bcrypt.check_password_hash(user_info.password, request.form['password']):
                session["user_info"] = user_info.id
                return redirect("/dashboard")
            else:
                flash("Incorrect Password")
                return redirect("/register")
        else:
            flash("No user with this email")
            return redirect("/register")
        
    return redirect ("/dashboard")


@app.route("/dashboard")
def dash():
    if 'user_info' in session:
        current_user = session['user_info']
        # expense = main_bills.Main_bill.get_all_from_id({'id' : session['user_info']})
        id =budget.Budget.get_budgets_by_user_id({'id' : session['user_info']})
        expense = budget.Budget.get_main_bills_by_budget_id({"id" :id})
        print(f'{expense} this is expense')
        print(session['user_info'])
        # print(userBudget)
        return render_template("home.html", user = current_user, expense = expense, use = users.User.get_one_by_id({'id': session['user_info']}))

@app.route('/expenses/<int:id>/newbill')
def new_bill(id):
    if 'user_info' not in session:
        return redirect ('/')
    use = users.User.get_one_by_id({'id': session['user_info']})
    return render_template('home.html', use = use)
    
@app.route('/expenses/<int:id>/newbill/create')
def create_bill(id):
    if 'user_info' not in session:
        return redirect ('/')
    data = {
        'bill_type' : request.form['bill_type'],
        'budget_main_bills_id': request.form['figure this out']
    }
    new_b = main_bills.Main_bill.save(data)
    print(f'this is the new bill{new_b}')
    return redirect('/dashboard')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
