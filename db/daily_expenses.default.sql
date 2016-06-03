PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS "currencies";
CREATE TABLE "currencies" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT NOT NULL,
    "sign" TEXT NOT NULL,
    "note" TEXT NULL,
    "datetime_created" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "datetime_modified" DATETIME NULL
);
CREATE UNIQUE INDEX currencies_name ON currencies(name);
INSERT INTO "currencies" ('id', 'name', 'sign') VALUES(1, 'UAH', '₴');
INSERT INTO "currencies" ('id', 'name', 'sign') VALUES(2, 'USD', '$');
INSERT INTO "currencies" ('id', 'name', 'sign') VALUES(3, 'EUR', '€');
INSERT INTO "currencies" ('id', 'name', 'sign') VALUES(4, 'PLN', 'zł');

DROP TABLE IF EXISTS "categories";
CREATE TABLE "categories" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NULL,
    "datetime_created" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "datetime_modified" DATETIME NULL
);
CREATE UNIQUE INDEX categories_name ON categories(name);
INSERT INTO "categories" ('id', 'name') VALUES(1, 'groceries');
INSERT INTO "categories" ('id', 'name') VALUES(2, 'monthly expenses');
INSERT INTO "categories" ('id', 'name') VALUES(3, 'public transport');
INSERT INTO "categories" ('id', 'name') VALUES(4, 'detergent');
INSERT INTO "categories" ('id', 'name') VALUES(5, 'cosmetics');
INSERT INTO "categories" ('id', 'name') VALUES(6, 'public utilities');
INSERT INTO "categories" ('id', 'name') VALUES(7, 'hygiene products');
INSERT INTO "categories" ('id', 'name') VALUES(8, 'devices');

DROP TABLE IF EXISTS "locations";
CREATE TABLE "locations" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "city" TEXT NOT NULL,
    "country" TEXT NOT NULL,
    "note" TEXT NULL,
    "datetime_created" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "datetime_modified" DATETIME NULL
);
INSERT INTO "locations" ('id', 'city', 'country') VALUES(1, 'Lviv', 'Ukraine');
INSERT INTO "locations" ('id', 'city', 'country') VALUES(2, 'Ternopil', 'Ukraine');
CREATE UNIQUE INDEX locations_city_country ON locations(city, country);

DROP TABLE IF EXISTS "places";
CREATE TABLE "places" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT NOT NULL,
    "location_id" INTEGER NOT NULL,
    "note" TEXT NULL,
    "datetime_created" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "datetime_modified" DATETIME NULL,
    FOREIGN KEY(location_id) REFERENCES locations(id)
);
CREATE UNIQUE INDEX places_name ON places(name);
INSERT INTO "places" ('id', 'name', 'location_id') VALUES(1, 'central market', 1);
INSERT INTO "places" ('id', 'name', 'location_id') VALUES(2, 'grocery store',  1);

DROP TABLE IF EXISTS "users";
CREATE TABLE "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "user_name" TEXT NOT NULL,
    "full_name" TEXT NOT NULL,
    "datetime_created" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "datetime_modified" DATETIME NULL
);
CREATE UNIQUE INDEX users_name ON users(user_name);
INSERT INTO "users" ('id', 'user_name', 'full_name') VALUES(1, 'test', 'Anonymous Joe');

DROP TABLE IF EXISTS "items";
CREATE TABLE "items" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NULL,
    "datetime_created" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "datetime_modified" DATETIME NULL
);
CREATE UNIQUE INDEX items_names ON items(name);

DROP TABLE IF EXISTS "measures";
CREATE TABLE "measures" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT NOT NULL,
    "short" TEXT NOT NULL,
    "note" TEXT NULL,
    "datetime_created" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "datetime_modified" DATETIME NULL
);
INSERT INTO "measures" ('id', 'name', 'short', 'note') VALUES(1, 'kilogram', 'kg', 'weight');
INSERT INTO "measures" ('id', 'name', 'short', 'note') VALUES(2, 'gram',     'g',  'weight');
INSERT INTO "measures" ('id', 'name', 'short')         VALUES(3, 'pieces',   'pcs'         );

DROP TABLE IF EXISTS "balance";
CREATE TABLE "balance" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "item_id" INTEGER NOT NULL,
    "category_id" INTEGER NOT NULL,
    "cost" REAL NOT NULL,
    "currency_id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "place_id" INTEGER NOT NULL,
    "qty" REAL NOT NULL DEFAULT 1.0,
    "measure_id" INTEGER NOT NULL,
    "is_spending" INTEGER NOT NULL DEFAULT 1,
    "note" TEXT NULL,
    "datetime" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "datetime_created" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "datetime_modified" DATETIME NULL,
    FOREIGN KEY(item_id) REFERENCES items(id),
    FOREIGN KEY(category_id) REFERENCES categories(id),
    FOREIGN KEY(currency_id) REFERENCES currencies(id),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(place_id) REFERENCES places(id),
    FOREIGN KEY(measure_id) REFERENCES measures(id)
);

COMMIT;
PRAGMA foreign_keys=ON;
