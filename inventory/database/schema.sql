CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    reorder_threshold INTEGER NOT NULL
);