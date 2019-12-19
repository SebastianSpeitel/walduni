#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask,redirect
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def tu_ilmenau():
    return redirect("https://www.tu-ilmenau.de/", code=302)

@app.route('/about')
def about():
    return redirect("https://github.com/clerie/walduni", code=302)

@app.route('/turm/')
def turm():
    return redirect("https://turm.rz.tu-ilmenau.de/eE/aktuell/lstr_browser.php", code=302)

@app.route('/modultafeln/<course>/')
@app.route('/modultafel/<course>/')
@app.route('/modulplan/<course>/')
@app.route('/module/<course>/')
@app.route('/modultafeln/')
@app.route('/modultafel/')
@app.route('/modulplan/')
@app.route('/module/')
def modultafeln(course=""):
    courseToPath = {
        "amw": "AngewandteMedienundKommunikationswissenschaft/Bachelor/2014",
        "amk": "AngewandteMedienundKommunikationswissenschaft/Bachelor/2014",
        "bmt": "BiomedizinischeTechnik/Bachelor/2014/",
        "btc": "BiotechnischeChemie/Bachelor/2013/",
        "eit": "ElektrotechnikundInformationstechnik/Bachelor/2013/",
        "ft": "Fahrzeugtechnik/Bachelor/2013/",
        "in": "Informatik/Bachelor/2013/",
        "ii": "Ingenieurinformatik/Bachelor/2013/",
        "mb": "Maschinenbau/Bachelor/2013/",
        "mathe": "Mathematik/Bachelor/2013/",
        "mechatronik": "Mechatronik/Bachelor/2013/",
        "mt": "Medientechnologie/Bachelor/2013/",
        "mw": "Medienwirtschaft/Bachelor/2015/",
        "oso": "OptischeSystemtechnikOptronik/Bachelor/2013/",
        "tks": "TechnischeKybernetikundSystemtheorie/Bachelor/2013/",
        "physik": "TechnischePhysik/Bachelor/2013/",
        "ww": "Werkstoffwissenschaft/Bachelor/2013/",
        "wi": "Wirtschaftsinformatik/Bachelor/2015/",
        "wiw": "Wirtschaftsingenieurwesen/Bachelor/2015/?vertiefung=MB"
    }
    
    return redirect("https://www.tu-ilmenau.de/modultafeln/" + courseToPath.get(course, ""), code=302)

@app.route('/mail/')
@app.route('/webmail/')
def mail():
    return redirect("https://webmail.tu-ilmenau.de/", code=302)

@app.route('/unirz/')
@app.route('/rz/')
def unirz():
    return redirect("https://www.tu-ilmenau.de/unirz/", code=302)

@app.route('/vlv/')
def vlv():
    return redirect("https://www.tu-ilmenau.de/vlv/index.php?id=330", code=302)

########################################################################################################################
# FeM
########################################################################################################################

# FeM
@app.route('/fem/')
def fem():
    return redirect("https://www.fem.tu-ilmenau.de/aktuelles/", code=302)

########################################################################################################################
# ILSC
########################################################################################################################

# ILSC
@app.route('/ilsc/')
def ilsc():
    return redirect("https://www.tu-ilmenau.de/fsr-mn/", code=302)

# BC
@app.route('/bc/')
def bc_club():
    return redirect("https://www.bc-club.de/", code=302)

# BD
@app.route('/bd/')
def bd_club():
    return redirect("http://www.bd-club.de/", code=302)

# BH
@app.route('/bh/')
def bh_club():
    return redirect("http://bh-club.de/", code=302)

# BI
@app.route('/bi/')
def bi_club():
    return redirect("https://www.bi-club.de/", code=302)

# Montagsküche
@app.route('/montag/')
def montagskueche():
    try:
        posts = requests.get("https://www.bi-club.de/tags/montagskueche")
        soup = BeautifulSoup(posts.text, 'html.parser')
        link = soup.find(id='main').article.header.h2.a.get('href')
        return redirect("https://www.bi-club.de" + link, code=302)
    except:
        return redirect("https://www.bi-club.de/tags/montagskueche", code=302)



########################################################################################################################
# Stura
########################################################################################################################

# Stura
@app.route('/stura/')
def stura():
    return redirect("https://stura.tu-ilmenau.de/", code=302)

# FSR EI
@app.route('/ei/')
@app.route('/fsr-ei/')
def fsr_ei():
    return redirect("https://www.tu-ilmenau.de/fachschaftsrat-ei/", code=302)

# FSR IA
@app.route('/ia/')
@app.route('/fsr-ia/')
def fsr_ia():
    return redirect("https://www.tu-ilmenau.de/fsr-ia/", code=302)

# FSR MB
@app.route('/mb/')
@app.route('/fsr-mb/')
def fsr_mb():
    return redirect("https://www.tu-ilmenau.de/fsr-mb/", code=302)

# FSR MN
@app.route('/mn')
@app.route('/fsr-mn/')
def fsr_mn():
    return redirect("https://www.tu-ilmenau.de/fsr-mn/", code=302)



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
