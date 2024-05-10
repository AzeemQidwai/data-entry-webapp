#pip install flask


from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Required for session management (e.g., flashing messages)

# Route to display the review form
@app.route('/')
def index():
    return render_template('review_form.html')

# Route to handle form submissions
@app.route('/submit_review', methods=['POST'])
def submit_review():
    name = request.form['name']
    email = request.form['email']
    review = request.form['review']
    rating = request.form['rating']

    # Here, you would typically save these data to a database
    # For this example, just redirecting to the form page

    return redirect(url_for('thank_you', name=name))

@app.route('/thank_you/<name>')
def thank_you(name):
    return render_template('thank_you.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
