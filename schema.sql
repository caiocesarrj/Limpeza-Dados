create table pedidos (
id_pedido varchar(10) primary key,
cliente_id varchar(10),
nome_cliente varchar(50),
email varchar(100),
produto varchar(50),
categoria varchar(20),
quantidade int,
preco_unitario decimal(10, 2),
desconto decimal(5, 2),
data_pedido date,
estado char(2),
status varchar (10),
avaliacao float
);
