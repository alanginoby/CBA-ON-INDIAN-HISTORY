from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__, "views")

@views.route("/history")
def home():
    return render_template("index.html", name= "Alan Ginoby", text= "I am doing my history CBA on India's history.",
    text2= '''Lets start with it's name. India had many names in its past. The oldest names are Bharat, Hindustan and there are many other names too. 
    India is a big country and has a big history. India was ruled by the british approximatly for 100 years and also Mumbai in India was attacked by the
    terrorist in 2008. I am going to briefly describe what happened in these both times.''')

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

@views.route("/json")
def get_json():
    return jsonify({'name': 'History CBA'})