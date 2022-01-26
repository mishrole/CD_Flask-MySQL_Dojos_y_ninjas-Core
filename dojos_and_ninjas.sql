Create database dojos_and_ninjas_schema;
Use dojos_and_ninjas_schema;

Create table dojos(
	id int primary key auto_increment,
    name varchar(45),
    created_at datetime,
    updated_at datetime
);

Create table ninjas(
	id int primary key auto_increment,
    first_name varchar(45),
    last_name varchar(45),
    age int,
    dojo_id int not null,
    created_at datetime,
    updated_at datetime,
    foreign key (dojo_id) references dojos(id)
);
