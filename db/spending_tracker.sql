DROP TABLE tags;
DROP TABLE merchant;
DROP TABLE transactions;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE merchant (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
);

CREATE TABLE transactions (
    
)