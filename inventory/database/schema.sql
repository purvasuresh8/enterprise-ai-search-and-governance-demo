-- Users

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Support Tickets

CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,

    user_id INTEGER REFERENCES users(id),

    subject VARCHAR(255) NOT NULL,
    issue TEXT NOT NULL,

    category VARCHAR(50),
    priority VARCHAR(20) DEFAULT 'Medium',
    status VARCHAR(20) DEFAULT 'Open',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Chat Sessions

CREATE TABLE chat_sessions (
    id SERIAL PRIMARY KEY,

    user_id INTEGER REFERENCES users(id),

    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Chat Messages

CREATE TABLE chat_messages (
    id SERIAL PRIMARY KEY,

    session_id INTEGER REFERENCES chat_sessions(id),

    role VARCHAR(20) NOT NULL,
    message TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Customer Feedback

CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,

    ticket_id INTEGER REFERENCES tickets(id),

    rating INTEGER CHECK (
        rating >= 1 AND rating <= 5
    ),

    comments TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- AI Evaluation

CREATE TABLE evaluations (
    id SERIAL PRIMARY KEY,

    message_id INTEGER REFERENCES chat_messages(id),

    accuracy_score DECIMAL(4,2),
    relevance_score DECIMAL(4,2),
    helpfulness_score DECIMAL(4,2),

    overall_score DECIMAL(4,2),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Escalations

CREATE TABLE escalations (
    id SERIAL PRIMARY KEY,

    ticket_id INTEGER REFERENCES tickets(id),

    reason TEXT,

    assigned_agent VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Audit Logs

CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,

    user_id INTEGER REFERENCES users(id),

    action VARCHAR(100),

    details TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
