# Personal Data Project

This project covers handling Personally Identifiable Information (PII) in Python logs, database connection security, and password encryption:
- Obfuscating sensitive fields in log messages using regular expressions (`filter_datum`).
- Custom redacting logging formatters (`RedactingFormatter`).
- Creating parameterized loggers (`get_logger`) with `PII_FIELDS`.
- Connecting securely to MySQL database via environment variables (`get_db`).
- Reading, formatting, and logging database records cleanly (`main`).
- Salting and hashing passwords using `bcrypt` (`hash_password`, `is_valid`).
