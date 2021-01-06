from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from flask_login import UserMixin
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Usuario(UserMixin, db.Model):
    __tablename__ = 'Usuarios'
    IdUsuario = Column(Integer, primary_key=True)
    Nombre = Column(String, nullable=False)
    Telefono = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    Contrasenia = Column(String, nullable=False)
    Sexo = Column(String, nullable=False)
    Tipo = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        usua = self.query.all()
        return usua
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        usu = self.consultaIndividual()
        db.session.delete(usu)
        db.session.commit()
    def consultaIndividual(self):
        usu = self.query.get(self.IdUsuario)
        return usu
    @property
    def password(self):
        raise AttributeError('El atributo password no es de lectura')
    def validarPassword(self, Contrasenia):
        pwd = self.query.filter_by(Contrasenia=Contrasenia).first()
        print(Contrasenia)
        return pwd
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.IdUsuario
    def validar(self, Email, Contrasenia):
        user = Usuario.query.filter_by(Email=Email).first()
        if user != None:
            if user.validarPassword(Contrasenia):
                return user
        else:
            return None


class Cliente(db.Model):
    __tablename__ = 'Clientes'
    IdCliente = Column(Integer, primary_key=True)
    IdUsuario = Column(Integer, ForeignKey('Usuarios.IdUsuario'))

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        clientes = self.query.all()
        return clientes
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        cli = self.consultaIndividual()
        db.session.delete(cli)
        db.session.commit()
    def consultaIndividual(self):
        cli = self.query.get(self.IdCliente)
        return cli

class Administrador(db.Model):
    __tablename__   = 'Administradores'
    IdAdministrador = Column(Integer, primary_key=True)
    IdUsuario = Column(Integer, ForeignKey('Usuarios.IdUsuario'))

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        administradores = self.query.all()
        return administradores
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        admin = self.consultaIndividual()
        db.session.delete(admin)
        db.session.commit()
    def consultaIndividual(self):
        admin = self.query.get(self.IdAdministrador)
        return admin

class Direccion(db.Model):
    __tablename__   = 'Direcciones'
    IdDireccion  = Column(Integer, primary_key=True)
    Pais         = Column(String, nullable=False)
    Estado       = Column(String, nullable=False)
    Ciudad       = Column(String, nullable=False)
    Colonia      = Column(String, nullable=False)
    Calle        = Column(String, nullable=False)
    CodigoPostal = Column(Integer, nullable=False)
    Descripcion  = Column(String, nullable=False)
    IdCliente    = Column(Integer, ForeignKey('Clientes.IdCliente'))

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        direcciones = self.query.all()
        return direcciones
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        direc = self.consultaIndividual()
        db.session.delete(direc)
        db.session.commit()
    def consultaIndividual(self):
        direc = self.query.get(self.IdDireccion)
        return direc

class Tarjeta(db.Model):
    __tablename__   = 'Tarjetas'
    IdTarjeta        = Column(Integer, primary_key=True)
    NumeroTarjeta    = Column(String, nullable=False)
    FechaVencimiento = Column(Date, nullable=False)
    Cvv              = Column(Integer, nullable=False)
    Titular          = Column(String, nullable=False)
    IdCliente        = Column(Integer, ForeignKey('Clientes.IdCliente'))

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        tarjetas = self.query.all()
        return tarjetas
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        tar = self.consultaIndividual()
        db.session.delete(tar)
        db.session.commit()
    def consultaIndividual(self):
        tar = self.query.get(self.IdTarjeta)
        return tar

class Producto(db.Model):
    __tablename__   = 'Productos'
    IdProducto    = Column(Integer, primary_key=True)
    CodigoBarras  = Column(Integer, nullable=False)
    Nombre        = Column(String, nullable=False)
    Descripcion   = Column(String, nullable=False)
    Departamento  = Column(String, nullable=False)
    Seccion       = Column(String, nullable=False)
    Stock         = Column(Integer, nullable=False)
    PrecioVenta   = Column(Float, nullable=False)
    PrecioCompra  = Column(Float, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        productos = self.query.all()
        return productos
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        prod = self.consultaIndividual()
        db.session.delete(prod)
        db.session.commit()
    def consultaIndividual(self):
        prod = self.query.get(self.IdProducto)
        return prod

class Pedido(db.Model):
    __tablename__   = 'Pedidos'
    IdPedido    = Column(Integer, primary_key=True)
    IdProducto  = Column(Integer, ForeignKey('Productos.IdProducto'))
    Fecha       = Column(Date, nullable=False)
    IdCliente   = Column(Integer, ForeignKey('Clientes.IdCliente'))

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        pedidos = self.query.all()
        return pedidos
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        ped = self.consultaIndividual()
        db.session.delete(ped)
        db.session.commit()
    def consultaIndividual(self):
        ped = self.query.get(self.IdPedido)
        return ped

class Venta(db.Model):
    __tablename__   = 'Ventas'
    IdVentas  = Column(Integer, primary_key=True)
    IdPedido  = Column(Integer, ForeignKey('Pedidos.IdPedido'))
    idEnvio   = Column(Integer, ForeignKey('Envios.IdEnvios'))
    Fecha     = Column(Date, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        ventas = self.query.all()
        return ventas
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        vent = self.consultaIndividual()
        db.session.delete(vent)
        db.session.commit()
    def consultaIndividual(self):
        vent = self.query.get(self.IdVentas)
        return vent

class Envio(db.Model):
    __tablename__   = 'Envios'
    IdEnvios      = Column(Integer, primary_key=True)
    IdPaqueteria  = Column(Integer, ForeignKey('Paqueteria.IdPaqueteria'))
    FechaSalida   = Column(Date, nullable=False)
    FechaArribo   = Column(Date, nullable=False)
    FechaEntrega  = Column(Date, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        envios = self.query.all()
        return envios
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        env = self.consultaIndividual()
        db.session.delete(env)
        db.session.commit()
    def consultaIndividual(self):
        env = self.query.get(self.IdEnvios)
        return env


class Paqueterias(db.Model):
    __tablename__   = 'Paqueteria'
    IdPaqueteria = Column(Integer, primary_key=True)
    Nombre       = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        paqueterias = self.query.all()
        return paqueterias
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        paque = self.consultaIndividual()
        db.session.delete(paque)
        db.session.commit()
    def consultaIndividual(self):
        paque = self.query.get(self.IdPaqueteria)
        return paque
