from flask import Flask, render_template, request, url_for, json
app = Flask(__name__)

@app.route('/')

def home():
   	print "Ok"
   	return render_template('Brain_Results_v5.html')



if __name__ == "__main__":
    app.run(debug=True)
