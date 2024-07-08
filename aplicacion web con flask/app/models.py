from __main__ import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  # agregado
db = SQLAlchemy(app) 

class Repartidor(db.Model):
    __tablename__ = 'repartidor'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    # relaciones--------------------------------------------
    paquetes = db.relationship('Paquete', backref='repartidor', lazy=True,)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))

class Sucursal(db.Model):
    __tablename__ = 'sucursal'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    provincia = db.Column(db.String(20), nullable=False)
    localidad = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(20), nullable=False)
    # relaciones----------------------------------------
    repartidores = db.relationship('Repartidor', backref='sucursal')
    paquetes = db.relationship('Paquete', backref='sucursal')
    transportes = db.relationship('Transporte', backref='sucursal')

class Transporte(db.Model):
    __tablename__ = 'transporte'
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte = db.Column(db.Integer, nullable=False)
    fechahorasalida = db.Column(db.DateTime, nullable=False)
    fechahorallegada = db.Column(db.DateTime, nullable=False)
    # relaciones----------------------------------------
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    paquetes = db.relationship('Paquete', backref='transporte')

class Paquete(db.Model):
    __tablename__ = 'paquete'
    id = db.Column(db.Integer, primary_key=True)
    numeroenvio = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    nomdestinatario = db.Column(db.String(20), nullable=False)
    dirdestinatario = db.Column(db.String(20), nullable=False)
    entregado = db.Column(db.Boolean, default=False)
    observaciones = db.Column(db.String, nullable=False)
    #creado_en = db.Column(db.DateTime, default=datetime.utcnow)  # Add this line
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idtransporte= db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'))
    
    
    def __init__(self, numeroenvio, peso, nomdestinatario, dirdestinatario, entregado, observaciones, idsucursal, idtransporte, idrepartidor ):
        self.numeroenvio = numeroenvio
        self.peso = peso
        self.nomdestinatario = nomdestinatario
        self.dirdestinatario = dirdestinatario
        self.entregado= entregado
        self.observaciones = observaciones
        self.idtransporte = idtransporte
        self.idrepartidor = idrepartidor
        self.idsucursal = idsucursal