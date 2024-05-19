# python-flask
## Com fer un entorn virtual de Python?
1. Creem la carpeta de l'entorn virtual amb la següent comanda amb PowerShell o Bash. En el nostre cas aquesta carpeta es diu venv, però pot tindre qualsevol altre nom:
```powershell
python -m venv .venv
```
2. Activem el entorn virtual executant l'script "activate" que trobem a la carpeta de l'entorn virtual:
```powershell
.venv\Scripts\activate
```
* Si la comanda funciona bé el prompt s'hauria de veure així:

![image](https://github.com/rgonzalezluque/python-flask-RSS/assets/165800646/1b66b4cc-bd01-4554-a466-ba075d9940f0)

3. Ara ja podrem instalar els paquets que necessitem amb pip:
```powershell
pip install flask
pip install feedparser
```

4. Per iniciar el servidor Flask utilitzarem la següent comanda:
```powershell
flask run --debug
```
* I aquest serà el resultat final:

![image](https://github.com/rgonzalezluque/python-flask-RSS/assets/165800646/25fa7473-6489-49f6-8987-77ebbe5127ef)

* Més informació sobre la creació de entors virtuals de Python a:  https://docs.python.org/es/3/library/venv.html

* Més informació sobre Flask a: https://flask.palletsprojects.com/en/3.0.x/

## Com connectar el meu projecte al repositori de GitHub?
1. Primer, creem un repositori local de GitHub amb la següent comanda:
```
git init
```
2. Hem d'afegir tots els fitxers al "staging area" i fer un commit per confirmar els canvis i afegir-los al repositori local:
```
git add <fitxer>
```
```
git commit -m "Fase incial de projecte Flask-RSS"
```
3. Amb git config ens identifiquem amb el nostre mail i nom d'usuari de GitHub:
```
git config --global user.email rgonzalezl@insjoaquimmir.cat
```
```
git config --global user.name "rgonzalezluque"
```
4. Després, vinculem el repositori local amb el repositori virtual que hem de creat a GitHub:
```
git remote add origin https://github.com/rgonzalezluque/python-flask-RSS.git
```
5. Renombrem la rama principal a "main" amb la següent comanda:
```
git branch -M main
```
6. Finalment, enviem els canvis del nostre repositori local a la branca "main" del nostre repositori virtual de GitHub:
```
git push -u origin main
```
Més informació sobre la creació de repositoris a GitHub a: https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories

## Com fer servir un xml en mode local i en mode remot?
Abans de fer res he modificat el template "index.html" per a que detecti totes les diferents seccions que vull mostrar a la meva pàgina web:

![image](https://github.com/rgonzalezluque/python-flask-RSS/assets/165800646/c68edff7-d3a0-4906-99ce-388bfe8528f6)

### Mode local
1. Descarrego nous RSSs de la Vanguardia i els he desat a la subcarpeta "lavanguardia" dins de la carpeta "rss":

![image](https://github.com/rgonzalezluque/python-flask-RSS/assets/165800646/b985ecde-619b-45ce-92a0-3f1d8e9f88fd)

2. Funció al "app.py" que detecta els RSSs en local:

![image](https://github.com/rgonzalezluque/python-flask-RSS/assets/165800646/965b00ff-72db-4407-863b-e0fcbe6a01f0)

### Mode remot
1. Funció al "app.py" que detecta els RSSs de la web de la Vanguardia:

![image](https://github.com/rgonzalezluque/python-flask-RSS/assets/165800646/c354dc77-1560-4df1-acdb-2995fd602244)

## Accés als diferents items i al channel dels RSSs
Per accedir a tots els diferents items dels RSSs de la Vanguardia he utilitzat "Jinja" a la template "lavanguardia.html".
### Accés al titol de la secció
He obtingut el titol de la secció desde el channel del RSS amb el següent codi:
```html
<h1>La Vanguardia - <small>{{rss.feed.title}}</small></h1>
```
La variable {{rss.feed.title}} és la que em dona el titol de la secció del diari. Aquest codi es pot replicar en altres elements del "channel" del RSS.
### Accés als items del RSS
En el següent codi hi ha un for que itera tots els items del RSS i cerca els elements que es demanen.
Els elements són els següents:
* item.link: url que ens direcciona a la noticia.
* item.title: títol de la notícia
* media.url: imatge de la notícia
* item.description: descripció de la notícia
* item.published: data de publicació de la notícia
* item.updated: data de modificació de la notícia
* item.autor: autor de la notícia
* item.category: categoria de la notícia
```html
{% for item in rss.entries %}
    <p>
        <a href="{{item.link}}">{{item.title}}</a>
        {% for media in item.media_content %}
            <p><img src="{{media.url}}" alt="{{item.title}}" /></p>
        {% endfor %}
        <p>Descripció: {{item.description}}</p>
        <p>Data de publicació: {{item.published}}</p>
        <p>Data de modificació: {{item.updated}}</p>
        <p>Autor: {{item.author}}</p>
        <p>Categoria: {{item.category}}</p>
    </p>
{% endfor %}
```

- En mode local fem servir aquesta funció:
```python
def get_rss_puntavui(seccio):
    # MODE REMOT: versió on descarrega l'XML de la web
    xml = f"http://www.elpuntavui.cat/{seccio}.feed?type=rss"
```