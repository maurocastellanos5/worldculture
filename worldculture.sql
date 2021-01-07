create  database Worldculture;
use Worldculture;

/*==============================================================*/
/* Table: Productos                                             */
/*==============================================================*/
create table Productos
(
   IdProducto         int auto_increment not null,
   CodigoBarras       int not null,
   Nombre             varchar(50) not null,
   Descripcion        varchar(900) not null,
   Departamento       varchar(10) not null,
   Seccion            varchar(9) not null,
   Stock              int not null,
   PrecioVenta        float not null,
   PrecioCompra       float not null,
   constraint pk_IdProdcuto primary key (IdProducto)
);

/*==============================================================*/
/* Table: Usuarios                                                 */
/*==============================================================*/
create table Usuarios
(
   IdUsuario           int auto_increment not null,
   Nombre          		varchar(150) not null,
   Telefono    			char(12) not null,
   Email            	varchar(100) not null,
   Contrasenia          varchar(15) not null,
   Sexo                 char(1) not null,
   Tipo                 char(1) not null,
   constraint pk_IdUsuario primary key (IdUsuario)
);

/*==============================================================*/
/* Table:  Clientes                            */
/*==============================================================*/
create table Clientes
(
   IdCliente      	int auto_increment not null,
   IdUsuario        int not null,
   constraint pk_IdCliente primary key (IdCliente)
);

/*==============================================================*/
/* Table: Administradores                                               */
/*==============================================================*/

create table Administradores
(
	IdAdministrador     int auto_increment not null,
    IdUsuario            int not null,
    constraint pk_IdAdministrador primary key (IdAdministrador)
);

/*==============================================================*/
/* Table: Direcciones                                              */
/*==============================================================*/

create table Direcciones
(
   IdDireccion          int auto_increment not null,
   Pais                 varchar(50) not null,
   Estado               varchar(50) not null,
   Ciudad               varchar(50) not null,
   Colonia              varchar(50) not null,
   Calle         		varchar(50) not null,
   CodigoPostal         int not null,
   Descripcion          varchar (100) not null,
   IdCliente            int not null,
   constraint pk_IdDireccion primary key (IdDireccion)
);

/*==============================================================*/
/* Table: Tarjetas                                           */
/*==============================================================*/
create table Tarjetas
(
   IdTarjeta             int auto_increment not null,
   NumeroTarjeta         varchar(16) not null,
   FechaVencimiento      date not null,
   Cvv     		         int not null,
   Titular               varchar (50) not null,
   IdCliente             int not null,
   constraint pk_IdTarjeta primary key (IdTarjeta)
);



/*==============================================================*/
/* Table: Pedidos                                             */
/*==============================================================*/
create table Pedidos
(
   IdPedido           int auto_increment not null,
   IdProducto         int not null,
   Fecha              date not null,
   IdCliente          int not null,
   constraint pk_IdPedido primary key (IdPedido)
);


/*==============================================================*/
/* Table: Ventas                                              */
/*==============================================================*/
create table Ventas
(
   IdVentas      		int  not null,
   IdPedido             int  not null,
   idEnvio              int  not null,
   Fecha                date not null,
   constraint pk_IdVentas primary key (IdVentas)
);


/*==============================================================*/
/* Table: Envios                                             */
/*==============================================================*/
create table Envios
(
   IdEnvios             int auto_increment not null,
   IdPaqueteria         int not null,
   FechaSalida          date not null,
   FechaArribo          date not null,
   FechaEntrega         date not null,
   constraint pk_IdEnvios primary key (IdEnvios)
);



/*==============================================================*/
/* Table: Paqueteria                                            */
/*==============================================================*/
create table Paqueteria
(
   IdPaqueteria        int auto_increment not null,
   Nombre              varchar(50) not null,
   constraint pk_IdPaqueteria unique (IdPaqueteria)
);



/*==============================================================*/
/* Restricciones FK	alter													                                             */
/*==============================================================*/
alter table Clientes add constraint Clientes_Usuarios_FK foreign key (IdUsuario)
      references Usuarios (IdUsuario);

alter table Administradores add constraint Administradores_Usuarios_FK foreign key (IdUsuario)
      references Usuarios (IdUsuario);

alter table Pedidos add constraint Pedidos_Cliente_FK foreign key (IdCliente)
      references Clientes (IdCliente);

alter table Pedidos add constraint Pedidos_Productos_FK foreign key (IdProducto)
      references Productos (IdProducto);

alter table Direcciones add constraint Direcciones_Clientes_FK foreign key (IdCliente)
      references Clientes (IdCliente);

alter table Ventas add constraint Ventas_Pedidos_FK foreign key (IdPedido)
      references Pedidos (IdPedido);

alter table Ventas add constraint Ventas_Envios_FK foreign key (IdEnvio)
      references Envios (IdEnvios);
      
alter table Envios add constraint Envios_Paqueteria_FK foreign key (IdPaqueteria)
      references Paqueteria (IdPaqueteria);
      
alter table Tarjetas add constraint Tarjetas_Clientes_FK foreign key (IdCliente)
      references Clientes (IdCliente);
      
CREATE USER 'admin1'@'localhost' IDENTIFIED BY 'hola.123';
GRANT ALL PRIVILEGES ON Worldculture.Usuarios TO 'admin1'@'localhost';
GRANT ALL PRIVILEGES ON Worldculture.Productos TO 'admin1'@'localhost';
select * from Productos;
select * from Usuarios;


insert into Usuarios(IdUsuario,Nombre,Telefono,Email,Contrasenia,Sexo,Tipo) 
values(1,"Mauro castellanos Diaz","3931041660","administrador@gmail.com","Hola","H","A");
insert into Usuarios(IdUsuario,Nombre,Telefono,Email,Contrasenia,Sexo,Tipo) 
values(2,"Guillermo Godinez","3931041660","cliente@gmail.com","Hola","H","C");
