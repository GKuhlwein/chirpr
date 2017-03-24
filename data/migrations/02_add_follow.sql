CREATE TABLE follow (
    lead_id INTEGER,
    follow_id INTEGER,
    FOREIGN KEY(lead_id) REFERENCES users(id)
    FOREIGN KEY(follow_id) REFERENCES users(id)
);