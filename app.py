from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
#    return "Welcome! to YES+ @ BPHC Page"

if __name__=="__main__":
    app.run()
