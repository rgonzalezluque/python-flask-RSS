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

![Captura de pantalla 2024-04-13 175408](https://github.com/rgonzalezluque/python-flask/assets/165800646/fb538292-8bc1-481c-96f6-908ab3ae4318)

Més informació sobre la creació de entors virtuals de Python a:  https://docs.python.org/es/3/library/venv.html

## Com connectar el meu projecte al meu repositori de GitHub?
