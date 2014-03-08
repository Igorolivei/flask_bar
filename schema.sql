drop table if exists bar;
create table bar (
  id_bar integer primary key autoincrement,
  nome varchar(50) not null,
  descricao text not null,
  endereco text not null,
  telefone varchar(10) not null,
  horario_ini varchar(6) not null,
  horario_fin varchar(6) not null,
  especialidade text not null
);