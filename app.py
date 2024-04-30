from flask import Flask, request, render_template, redirect, url_for, flash
from flask import request
import feedparser

app = Flask(__name__)
app.secret_key = '¡3248 97320983 bkjxdlrkfj k2 r9p874989387 98p78oiyylkhçç'

#
# Exemples inicials de flask
#
@app.route("/demo0")
def demo0():
    return "<h1>Hola em dic Alfonso</h1>"

@app.route("/demo1")
def demo1():
    return render_template("exemples/demo/hola.html")

@app.route("/demo2")
def demo2():
    return render_template("exemples/demo/edat.html", nom="Alfonso", edat=26)

@app.route("/demo3/<nom_usuari>/<int:edat>")
def demo3(nom_usuari, edat):
    return render_template("exemples/demo/edat.html", nom = nom_usuari, edat = edat)

@app.route("/demo4")
def demo4():
    nom = request.args.get('nom', default = "Desconegut/a", type = str)
    edat = request.args.get('edat', default = 0, type = int)
    return render_template("exemples/demo/edat.html", nom = nom, edat = edat)

@app.route("/demo5")
def demo5():
    # pàgina mostrant un exemple amb bootstrap
    return render_template("exemples/demo/boostrap.html")

#
# Petit exemple amb flask [SEGUIMENT]
#
@app.route("/hola1")
def hola1():
    return render_template("exemples/hola/salutacio_form.html")

@app.route("/hola2")
def hola2():
    valor_salutacio = request.args.get('salutacio', default = "WTF!", type = str)
    valor_quantes = request.args.get('quantes', default = 1, type = int)
    valor_color_de_fons = request.args.get('color-de-fons', default = "white", type = str)
    valor_gatete = request.args.get('gatete', default = False, type = bool)
    return render_template("exemples/hola/salutacio_resultat.html", 
                           salutacio = valor_salutacio, 
                           quantes = valor_quantes,
                           color_de_fons = valor_color_de_fons,
                           gatete = valor_gatete
                           )

#
# Exemple de formulari amb post
#
@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == 'GET':
        return render_template("exemples/insert/insert_form.html")
    else:
        # POST
        producte = request.form.get('producte', type = str)
        quantitat = request.form.get('quantitat', type = int)

        # Aquí hauríem de fer alguna cosa amb producte i quantitat
        # com per exemple un insert a la base de dades

        # https://www.seobility.net/es/wiki/Post/Redirect/Get
        flash(f"El producte {producte} amb quantitat {quantitat} s'ha inserit correctament")
        return redirect(url_for('insert'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lavanguardia/<seccio>')
def lavanguardia(seccio):
    rss = get_rss_lavanguardia(seccio)
    return render_template("lavanguardia.html", rss = rss)

def get_rss_lavanguardia(seccio):
    # MODE REMOT: versió on descarrega l'XML de la web
    # xml = f"https://www.lavanguardia.com/rss/{seccio}.xml"
    
    # MODE LOCAL: versió que fa servir l'XML descarregat
    xml = f"./rss/lavanguardia/{seccio}.xml"
    
    rss = feedparser.parse(xml)
    return rss
