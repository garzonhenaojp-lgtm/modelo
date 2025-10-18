from flask import Flask, render_template, request

# Crea la aplicación Flask correctamente
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    costo_total = None  # valor por defecto

    # Solo procesamos si el formulario se envía (POST)
    if request.method == "POST":
        costo_1 = request.form.get("costo_1")
        costo_2 = request.form.get("costo_2")

        # Validamos que los campos no estén vacíos
        if costo_1 and costo_2:
            try:
                # Convertimos a enteros o flotantes
                costo_total = int(costo_1) + int(costo_2)
                print("Costo total:", costo_total)
            except ValueError:
                costo_total = "Error: Debes ingresar números válidos."

    # Renderizamos el HTML pasando el resultado (puede ser None)
    return render_template("home.html", costo_total=costo_total)

# Corrección del bloque main
if __name__ == "__main__":
    app.run(debug=True)