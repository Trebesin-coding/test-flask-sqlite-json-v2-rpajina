from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("vitej.html")

@app.route("/form")
def form():
    recenze = request.args.get("recenze")
    print(recenze)
    message = None

    if recenze == "nic":
        message = "uzivatel byl moc liny na napsani recenze"
        print(message)
        recenze = message

    elif len(recenze) <= 3:
        message = "uzivatel byl moc liny na napsani recenze"
        print(message)
        recenze = message
        

    return render_template("form.html", recenze=recenze, message = message)



# Z následujících si vyber kód a sestav funkční flask aplikaci (není třeba použít vše, vyber si pouze ty části kódu, které potřebuješ)
# Kód je funkční, pouze místo dotazníků je potřeba doplnit podle potřeby


# from flask import Flask, render_template, request, redirect, url_for
# @app.route("???")
# request.args.get("???")
# request.form.get("???")
# print("???")
# cursor.execute("???")
# if request.method == "POST"


if __name__ == "__main__": #aplikace se spusti pouze, pokud je spoustena jako hlavni, nespusti se kdyz je importovany modul
    app.run(debug=True)
