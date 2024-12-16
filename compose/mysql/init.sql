create table customers (
  fiscal_code varchar(32),
  last_name varchar(255) NOT NULL,
  first_name varchar(255),
  address varchar(255) NOT NULL,
  city varchar(255) NOT NULL,
  primary key (fiscal_code)
);

insert into customers (fiscal_code, last_name, first_name, address, city)
values ('AAAAAAAAAAAAAAAA', 'Bianchi', 'Alessia', 'Via quella, 4 - 12345', 'Quel paese');

insert into customers (fiscal_code, last_name, first_name, address, city)
values ('BBBBBBBBBBBBBBBB', 'Rossi', 'Mario', 'P.za altrove, 12 - 12345', 'Quel paese');

create table orders (
  order_id int auto_increment,
  customer_cf varchar(32),
  total DECIMAL(10, 2) NOT NULL,
  items DECIMAL(16) NOT NULL,
  order_date DATETIME NOT NULL,
  primary key (order_id),
  foreign key (customer_cf) references customers(fiscal_code)
);

insert into orders (customer_cf, total, items, order_date)
values ('AAAAAAAAAAAAAAAA', '12.98', '2', '2024-12-15 14:30:00');

insert into orders (customer_cf, total, items, order_date)
values ('BBBBBBBBBBBBBBBB', '0.99', '1', '2024-12-15 18:30:00');

insert into orders (customer_cf, total, items, order_date)
values ('AAAAAAAAAAAAAAAA', '44.98', '2', '2024-12-16 14:30:00');

insert into orders (customer_cf, total, items, order_date)
values ('AAAAAAAAAAAAAAAA', '19.97', '3', '2024-12-16 18:30:00');

insert into orders (customer_cf, total, items, order_date)
values ('BBBBBBBBBBBBBBBB', '10.00', '1', '2024-12-16 15:30:00');

create table orders_stats (
  total_avg DECIMAL(10, 2) NOT NULL,
  items_avg DECIMAL(16) NOT NULL,
  order_date DATETIME NOT NULL,
  primary key (order_date)
);