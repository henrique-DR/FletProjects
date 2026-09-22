create table if not exists pintao (
    id          integer primary key autoincrement,
    titulo      text not null,
    autor       text not null,
    desc        text not null,
    preco       real not null
);