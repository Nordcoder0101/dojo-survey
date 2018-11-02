from flask import Flask, render_template, request, redirect
 
app = Flask(__name__)

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

    return render_template('show.html', name_from_form = name_from_form, school_from_form=school_from_form, language_from_form=language_from_form, comments_from_form =comments_from_form)

@app.route("/back_to_form")
def back_to_form():
  print('click')
  return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)