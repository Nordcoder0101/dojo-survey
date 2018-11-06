from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'lololol'

@app.route("/")
def index():
  
    
    return render_template('index.html')

@app.route("/users", methods=['POST'])
def submit_survey():
    print("Got post info")
    print(request.form)
    name_from_form = request.form['name']
    school_from_form = request.form['dojo']
    language_from_form = request.form['favorite_language']
    comments_from_form = request.form['comments']
    print(len(name_from_form))
    isValid = True
    if len(name_from_form) < 2:
        isValid = False
        flash('Please enter valid name')
    if len(school_from_form) < 1:
        isValid = False
        flash('Please select a valid school')
    if len(language_from_form) < 1:
        isValid = False
        flash('Please select a valid language')

    if isValid:
        mysql = connectToMySQL('dojo_survey')
        query = "INSERT INTO student (name, location, fave_language, comment) VALUES (%(n)s, %(l)s, %(fl)s, %(c)s)"
        data = {'n': name_from_form, 'l': school_from_form,
                'fl': language_from_form, 'c': comments_from_form}
        flash('User successfully made')
        new_user = mysql.query_db(query, data)
    

    # return render_template('show.html', name_from_form = name_from_form, school_from_form=school_from_form, language_from_form=language_from_form, comments_from_form =comments_from_form)

    return redirect('/')

@app.route("/back_to_form")
def back_to_form():
  print('click')
  return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)
