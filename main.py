from flask import Flask , render_template, request
import qrcode

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/qrcode", methods=["POST"])
def qrget():
    data = request.form["data"]
    print(data)
    img = qrcode.make(data)
    img.save("static/qr.png")
    
    return render_template("showqr.html")

app.run(debug=True)

