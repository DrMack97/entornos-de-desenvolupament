# Entorns de desenvolupament 25-26
Entorns de Desenvolupament 25-26

## Requisits Funcionals TapatApp

[Requisits Funcionals TapatApp](requisitsFuncTapatApp.md)

## Requisits Tècnics TapatApp

[Requisits Tècnics TapatApp](requisitsTecTapatApp.md)


## Configuració GitHub VsCode

Aquí configurem VSCode

# Planificació Scrum

- Iteració 1: 12/11 - 17/12 (15h) - Connexió Client Server
- Iteració 2: 12/01 - 04/02 (12h) - End Points WebService, dades Tutor i Child 
- Iteració 3: 9/02 - 04/03 (10h) - Digrames classes, Login i Seguretat
- Iteració 4: 9/03 - 8/04 (11h) - Vistes Wireframes i BBDD
- Iteració 5: 13/04 - 29/04 (9h) - Pegat i Testing

[Projecte a GiutHub](https://github.com/users/amallad2/projects/9/views/1)

# Prototip 1

Connectar Client / Servidor.
Consultar dades d'usuari per nom.

[Diagrama d'arquitectura prototip 1](charts/diagramaprototip1.mermaid)

Definicion del en-point del webService:

URL Server desenvolupament: http://localhost:5000/

| URL | Method | Parametros | Descripcion | Output |
|--------------|------------|-------------|--------|---------|
|/user   | GET | username <String> obligatorio | Retorna la informacion de | {
    "code_response=1, descripcion="", name="Gustavo Lloris",
    username="glloris",passwoprd="12345", rol="tutor", email="glloris@xtec.cat"
}

