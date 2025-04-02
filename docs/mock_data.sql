-- Create the sales_data table
CREATE TABLE sales_data (
    id SERIAL PRIMARY KEY,
    product VARCHAR(255) NOT NULL,
    sales INTEGER NOT NULL
);

-- Insert mock data for an electronics store
INSERT INTO sales_data (product, sales) VALUES
    ('MacBook Pro 14"', 150),
    ('iPhone 15 Pro', 200),
    ('Samsung Galaxy S23', 180),
    ('AirPods Pro', 120),
    ('USB-C Charger 65W', 90),
    ('Dell XPS 13', 140),
    ('Sony WH-1000XM5 Headphones', 110);