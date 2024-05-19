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
2. Hem d'afegir tots els fitxers del repositori local al "staging area" i fer un commit:
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

- En mode local fem servir aquesta funció:
```python
def get_rss_puntavui(seccio):
    # MODE REMOT: versió on descarrega l'XML de la web
    xml = f"http://www.elpuntavui.cat/{seccio}.feed?type=rss"
```