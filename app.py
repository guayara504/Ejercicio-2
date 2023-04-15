from flask import Flask, render_template, request

app = Flask(__name__)

# Productos y precios
productos = {
    'Lavadora': 1500000,
    'Refrigerador': 3500000,
    'Radiograbadora': 500000,
    'Tostadora': 700000
}

@app.route('/', methods=['GET', 'POST'])
def venta():
    if request.method == 'POST':
        # Obtener los datos del formulario
        producto = request.form['producto']
        precio = productos[producto]
        cantidad = int(request.form['cantidad'])
        cuotas = int(request.form['cuotas'])

        # Calcular el subtotal y el total
        subtotal = precio * cantidad
        total = subtotal * (1 + cuotas * 0.1)

        # Calcular los montos de las cuotas
        cuota = total / cuotas

        # Mostrar los resultados en una tabla HTML
        return render_template('resultado.html', producto=producto, precio=precio,
                               cantidad=cantidad, cuotas=cuotas, subtotal=subtotal,
                               total=total, cuota=cuota)

    else:
        # Mostrar el formulario de ventas
        return render_template('venta.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
     