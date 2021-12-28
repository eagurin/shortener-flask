DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
    shorten TEXT PRIMARY KEY,
    url TEXT NOT NULL,
    count INTEGER DEFAULT 0,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
