CREATE TABLE vulnerabilities (
    id SERIAL PRIMARY KEY,
    target VARCHAR(255),
    severity VARCHAR(50),
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);