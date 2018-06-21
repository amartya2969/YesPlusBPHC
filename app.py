from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
#    return "Welcome! to YES+ @ BPHC Page"
@app.route("/Experiences")
def Experiences():
    return render_template('Experiences.html')
@app.route("/Workshops")
def Workshops():
    return render_template('Upcoming_Workshops.html')
@app.route("/Contacts")
def Contact_Us():
    return render_template('Contact_Us.html')

if __name__=="__main__":
    app.run()
