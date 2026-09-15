from flask import Flask, jsonify, render_template
import redis
import psycopg

app = Flask(__name__)

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)


def get_db_connection():
    return psycopg.connect(
        host="postgres",
        port=5432,
        dbname="three_tier_db",
        user="appuser",
        password="AppPassword123"
    )


def check_postgres():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        cursor.close()
        connection.close()
        return True
    except Exception:
        return False


def check_redis():
    try:
        return redis_client.ping()
    except Exception:
        return False


@app.route("/")
def home():
    postgres_status = check_postgres()
    redis_status = check_redis()

    return render_template(
        "index.html",
        postgres=postgres_status,
        redis=redis_status
    )


@app.route("/health")
def health():
    postgres_status = check_postgres()
    redis_status = check_redis()

    healthy = postgres_status and redis_status

    return jsonify({
        "application": "healthy" if healthy else "degraded",
        "postgresql": "connected" if postgres_status else "disconnected",
        "redis": "connected" if redis_status else "disconnected"
    })


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
