import sqlite3
from pathlib import Path

DATABASE_FILE = Path(__file__).resolve().parent.parent / "airsense.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS air_quality_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT NOT NULL,
    pm25 REAL NOT NULL,
    category TEXT NOT NULL,
    advisory TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
"""

SELECT_COLUMNS = """
id, location, pm25, category, advisory, timestamp
"""
def connect_database():
    return sqlite3.connect(DATABASE_FILE)

def create_database():
    with connect_database() as connection:
        connection.execute(CREATE_TABLE_SQL)

def _row_to_dict(row):
    return {
        "id": row[0],
        "location": row[1],
        "pm25": row[2],
        "category": row[3],
        "advisory": row[4],
        "timestamp": row[5],
    }

def get_all_records():
    with connect_database() as connection:
        rows = connection.execute(
            f"""
            SELECT {SELECT_COLUMNS}
            FROM air_quality_records
            ORDER BY id
            """
        ).fetchall()

    return [_row_to_dict(row) for row in rows]

def get_record(record_id):
    with connect_database() as connection:
        row = connection.execute(
            f"""
            SELECT {SELECT_COLUMNS}
            FROM air_quality_records
            WHERE id = ?
            """,
            (record_id,),
        ).fetchone()

    return _row_to_dict(row) if row else None

def add_record_to_database(
    location,
    pm25,
    category,
    advisory,
    timestamp,
):

    with connect_database() as connection:
        cursor = connection.execute(
            """
            INSERT INTO air_quality_records
            (location, pm25, category, advisory, timestamp)
            VALUES (?, ?, ?, ?, ?)
            """,
            (location, pm25, category, advisory, timestamp),
        )
        return cursor.lastrowid

def search_database(keyword):
    search_value = f"%{keyword.strip().lower()}%"

    with connect_database() as connection:
        rows = connection.execute(
            f"""
            SELECT {SELECT_COLUMNS}
            FROM air_quality_records
            WHERE LOWER(location) LIKE ?
            ORDER BY id
            """,
            (search_value,),
        ).fetchall()

    return [_row_to_dict(row) for row in rows]

def update_record_in_database(
    record_id,
    pm25,
    category,
    advisory,
    timestamp,
):
    with connect_database() as connection:
        cursor = connection.execute(
            """
            UPDATE air_quality_records
            SET pm25 = ?, category = ?, advisory = ?, timestamp = ?
            WHERE id = ?
            """,
            (pm25, category, advisory, timestamp, record_id),
        )
        return cursor.rowcount > 0

def update_location(record_id, location):
    with connect_database() as connection:
        cursor = connection.execute(
            """
            UPDATE air_quality_records
            SET location = ?
            WHERE id = ?
            """,
            (location, record_id),
        )
        return cursor.rowcount > 0

def delete_record_from_database(record_id):
    with connect_database() as connection:
        cursor = connection.execute(
            """
            DELETE FROM air_quality_records
            WHERE id = ?
            """,
            (record_id,),
        )
        return cursor.rowcount > 0
