

from flask import Flask, render_template    # Uvozimo samo Flask, Flask deluje na principu Objektno orient. progr.

app = Flask(__name__)                       # V tej vrstici smo kreirali nov flask objekt

# controller ali handler (izraz handler uporabljajo python razvijalci)
# lahko imamo več kontrolerjev
@app.route("/")         # Samo poševnica je root of the page
def index():
    # return "Hello!" 
    return render_template("index.html")                       # Controller se vedno zaključi z return ukazom

@app.route("/galerie")        
def galerie():
    return render_template("galerie.html")    

@app.route("/contact")         
def contact():
    return render_template("contact.html")   

@app.route("/aboutme")         
def aboutme():
    return render_template("aboutme.html")   

if __name__ == "__main__":
    app.run()




