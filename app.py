from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")  # Correctly linking the About Us page

@app.route('/subscription')
def subscription():
    return render_template("subscription.html")  # This will load subscription.html


if __name__ == '__main__':
    app.run(debug=True)
