from flask import Flask
import redis
import psycopg

app = Flask(__name__)

# Redis connection
redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

# PostgreSQL connection
def get_db_connection():
    return psycopg.connect(
        host="postgres",
        port=5432,
        dbname="three_tier_db",
        user="appuser",
        password="AppPassword123"
    )


@app.route("/")
def home():
    return "Hello! Three-Tier Application is Running"


@app.route("/health")
def health():
    return "Application is healthy"


@app.route("/redis")
def redis_test():
    redis_client.set("message", "Hello from Redis")

    message = redis_client.get("message")

    return f"Redis response: {message}"


@app.route("/users")
def users():
    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, email FROM users ORDER BY id"
    )

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    result = ""

    for row in rows:
        result += f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}<br>"

    return result


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
