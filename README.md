# modelo
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <title>Modelo de optimización - Bauxita</title>
  </head>

  <body>
    <h1>Modelo de optimización de costos</h1>

    <!-- Formulario para capturar los costos -->
    <form method="post">
      <label>Primer costo:</label>
      <input type="text" placeholder="Ingrese el primer costo" name="costo_1" />

      <br><br>

      <label>Segundo costo:</label>
      <input type="text" placeholder="Ingrese el segundo costo" name="costo_2" />

      <br><br>

      <button type="submit">Ejecutar modelo</button>
    </form>

    <!-- Mostrar el resultado solo si existe -->
    {% if costo_total %}
      <h2>Resultado de la función objetivo: {{ costo_total }}</h2>
    {% endif %}
  </body>
</html>
