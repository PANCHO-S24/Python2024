from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_pyfile(os.path.join('C:\\Users\\frans\\OneDrive\\Escritorio\\aplicacion web con flask\\app','config.py'))

from models import Repartidor, Sucursal, Transporte, Paquete, db

import random  # Genera números aleatorios

@app.route("/", methods=["GET", "POST"])  #ruta pagina principal
def login():
    return render_template('template_base.html')

@app.route('/sucursales', methods=["GET", "POST"])  #ruta para lista sucursales y operaciones a realizar
def lista_sucursales():
    try:
        sucursales = Sucursal.query.order_by(Sucursal.numero).all()   #obtiene sucursales ordenadas por numero
        print(f"Numero de sucursales obtenidas: {len(sucursales)}")
        return render_template('sucursales.html', sucursales=sucursales)
    except Exception as e:
        print(f"Error al obtener sucursales: {e}")
        return render_template('error.html')

@app.route('/registrar_paquete', methods=["GET", "POST"])  # ruta para registrar paquete
def registrar_paquete():
    sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    print(f"Numero de sucursales obtenidas: {len(sucursales)}")

    if request.method == "POST":
        # Obtener los datos del formulario
        peso_paquete = request.form["peso_paquete"]
        nombre_destinatario = request.form["nombre_destinatario"]
        direccion_destinatario = request.form["direccion_destinatario"]
        sucursal_destino = request.form["sucursal_destino"]

        # Generar un número de envío único
        ultimo_paquete = Paquete.query.order_by(Paquete.numeroenvio.desc()).first()
        if ultimo_paquete:
            numeroenvio = ultimo_paquete.numeroenvio + 20
        else:
            numeroenvio = 1060

        # Crear un nuevo paquete
        nuevo_paquete = Paquete(
            numeroenvio= numeroenvio,
            peso= peso_paquete,
            nomdestinatario=nombre_destinatario,
            dirdestinatario=direccion_destinatario,
            entregado=False,
            observaciones='',  # vacío ya que no se requiere
            idsucursal= int(sucursal_destino),
            idtransporte = None,  
            idrepartidor = None,  
            
        )
        db.session.add(nuevo_paquete)   #agrega paquetes
        db.session.commit()             #guarda los cambios

        flash("Paquete registrado con éxito")
        return redirect(url_for("lista_sucursales"))  # Redirigir a la lista de sucursales o a otra página

    return render_template("registrar_paquete.html", sucursales=sucursales)


@app.route('/registrar_salida', methods=['GET', 'POST'])   # Ruta para registrar la salida de un transporte
def registrar_salida():
    if request.method == "POST":
        sucursal_destino = request.form.get("sucursal_destino")
        paquetes_ids = request.form.getlist("paquetes")
        
        # Verifica si se seleccionó una sucursal destino y al menos un paquete
        if not sucursal_destino or not paquetes_ids:
            # Devuelve error 400 si no se seleccionó una sucursal destino o paquetes
            return 'Error: Debes seleccionar una sucursal destino y al menos un paquete', 400

        # Obtiene la fecha y hora actuales para la salida del transporte
        fecha_hora_salida = datetime.now()
        numerotransporte = random.randint(100, 300) 
        
        if paquetes_ids:
            # Registrar salida de transporte para los paquetes seleccionados
            transporte = Transporte(
                numerotransporte=numerotransporte,  
                fechahorasalida=fecha_hora_salida,
                fechahorallegada=None,  # Se establecerá al llegar a la sucursal destino
                idsucursal=int(sucursal_destino)
            )
            try:
                # Intenta agregar el transporte a la base de datos
                db.session.add(transporte)
                db.session.flush()  # Para obtener el ID del transporte antes de hacer commit

                for paquete_id in paquetes_ids:
                    paquete = db.session.query(Paquete).filter_by(id=paquete_id).first()
                    if paquete:
                        paquete.idtransporte = transporte.id
            
                # guarda cambios en la base de datos
                db.session.commit()
            except Exception as e:
                # Si ocurre un error, desecha los cambios y devuelve un error 500
                db.session.rollback()
                return f'Error al registrar la salida del transporte: {e}', 500

            return render_template('Exito.html', mensaje='Salida de transporte registrada exitosamente')  # Devuelve mensaje de éxito 
    
    # Si la solicitud es de tipo GET, devuelve el template de registro con las sucursales y paquetes disponibles
    sucursales = db.session.query(Sucursal).all()
    paquetes = db.session.query(Paquete).filter_by(entregado=False, idtransporte=None).all()
    return render_template('registrar_salida.html', sucursales=sucursales, paquetes=paquetes)


@app.route('/registrar_llegada', methods=['GET', 'POST'])   #ruta registrar llegada de transporte
def registrar_llegada():
    if request.method == 'POST':
        # Obtiene ID del transporte seleccionado
        transporte_id = request.form.get('transporte_id')

        # Verifica si se selecciono un transporte
        if not transporte_id:
            # Devuelve 400 si no se seleccionó un transporte
            return 'Error: Debes seleccionar un transporte', 400
        # Obtiene la fecha y hora actuales para la llegada del transporte
        fecha_hora_llegada = datetime.now()

        try:
            # Busca el transporte en la base de datos
            transporte = db.session.query(Transporte).filter_by(id=transporte_id).first()
            if not transporte:
                # Devuelve un error 404 si el transporte no se encontró
                return 'Error: Transporte no encontrado', 404
            transporte.fechahorallegada = fecha_hora_llegada # Actualiza la fecha y hora de llegada del transporte
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            return f'Error al registrar la llegada del transporte: {e}', 500
        
        return render_template('Exito.html', mensaje='Llegada de transporte registrada exitosamente')
    else:
        # Si la solicitud es de tipo GET, devuelve el template de registro con los transportes disponibles
        # Obtener todos los transportes que aún no han registrado una fecha de llegada
        transportes = db.session.query(Transporte).filter_by(fechahorallegada=None).all()
        return render_template('registrar_llegada.html', transportes=transportes)

"""def eliminar_paquetes_por_numeros(numeros):
    with app.app_context():
        for numero in numeros:
            paquete =Paquete.query.filter_by(numeroenvio=numero).first()
            if paquete:
                db.session.delete(paquete)
                print(f"numero de transporte {numero} eliminado.")
            else:
                print(f"No se encontró un numero de transporte {numero}.")
        db.session.commit()"""

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        #Lista de números de envío a eliminar
        #numeros_a_eliminar = [1060]
        #eliminar_paquetes_por_numeros(numeros_a_eliminar)

    app.run(debug=True)