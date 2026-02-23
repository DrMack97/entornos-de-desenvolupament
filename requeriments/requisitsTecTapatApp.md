# Requisits Tècnics TapatApp

## Arquitectura

[Client Servidor](charts/mvc-generic.mermaid)

## 1. Backend (Servidor i Gestió de Dades)

El backend serà el cor del sistema, encarregat de gestionar dades, usuaris, i la lògica del sistema.

### a. Requisits del Servidor

- Allotjament: Hosting compartit
- Base de dades: Mysql o MariaDB
- Sistema Operatiu: Linux o Windows
- WebService: RESTFul  llibreria Python Flask

### b. Llenguatges de Programació

Python

### c. Seguretat

- Autenticació i autorització pels usuaris 
- Xifratge de dades HTTPS
- Còpies de seguretat automàtiques 

## 2. Frontend

### a. Tipus de Clients 

- App Mòbil: Android
- Consola Python
- Framework Multiplataforma: Flutter (Apps IOS Android, Web, Desktop)

### b. Enmagatzematge local i sincronització

- Dades guardem en local: Token, nickname
- Seguretat: HTTPS, autenticació serveis per Token

### c. Gestió d'accessibilitat

- Nivells A, AA, AAA d'accessibilitat

## 3. Requisits Generals Infraestructura

### a. Gestió d'usuari i autenticació

- Rols d'usuari: Tutor i cuidador
- Seguretat password: md5m, sha256 o sha512

### b.  Requisits d'Infraestructura

- Xarxa: Internet
- Espai d'enmagatzematge a Servidor: 1Tb
- APIs a tercers:  No en fem servir

## 4. Requisits del Procés de Desenvolupament

- IDE's: VScode Python, Android Studio, PyCharm 
- Control de versions: git, GitHub
- Metodologia de desenvolupament: SCRUM
- Testing i proves de qualitat(QA): Tests i proves unitàries
