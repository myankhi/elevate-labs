from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret123"  # needed for flash messages

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if not name or not email or not message:
            flash("⚠ Please fill all fields")
        else:
            # For now just print (in real app, save to DB or send email)
            print(f"📩 Message from {name} ({email}): {message}")
            flash("✅ Thank you! Your message has been received.")
            return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
