from datetime import datetime

from api.api_module import classify_pm25, fetch_pm25_from_api
from config.config_module import CAMPUS_LOCATIONS
from database import database

def initialize_records():
    database.create_database()

def _current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %I:%M %p")

def get_records():
    return database.get_all_records()

def choose_location():
    print("\nSelect a location at UM Matina Campus:")

    for index, location in enumerate(CAMPUS_LOCATIONS, start=1):
        print(f"  {index}. {location}")

    while True:
        choice = input("Enter location number: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(CAMPUS_LOCATIONS):
            return CAMPUS_LOCATIONS[int(choice) - 1]

        print("Invalid choice. Please enter a valid number from the list.")

def add_record(location):
    if location not in CAMPUS_LOCATIONS:
        raise ValueError("Invalid campus location.")

    pm25_value = fetch_pm25_from_api()
    category, advisory = classify_pm25(pm25_value)
    timestamp = _current_timestamp()
    pm25_value = round(pm25_value, 2)

    record_id = database.add_record_to_database(
        location,
        pm25_value,
        category,
        advisory,
        timestamp,
    )

    return database.get_record(record_id)

def view_records():
    records = get_records()

    print("\n--- ALL AIR QUALITY RECORDS (UM MATINA CAMPUS) ---")

    if not records:
        print("No records found yet. Use 'Add Record' first.")
        return

    header = (
        f"{'ID':<4}"
        f"{'Location':<40}"
        f"{'PM2.5':<10}"
        f"{'Category':<32}"
        f"{'Logged At':<20}"
    )
    print(header)
    print("-" * len(header))

    for record in records:
        print(
            f"{record['id']:<4}"
            f"{record['location']:<40}"
            f"{record['pm25']:<10}"
            f"{record['category']:<32}"
            f"{record['timestamp']:<20}"
        )

def search_records(keyword):
    keyword = keyword.strip()

    if not keyword:
        return []

    return database.search_database(keyword)

def update_record(record_id, update_type, new_location=None):
    target = database.get_record(record_id)

    if target is None:
        raise ValueError(f"No record found with ID {record_id}.")

    if update_type == "refresh":
        pm25_value = fetch_pm25_from_api()
        category, advisory = classify_pm25(pm25_value)
        timestamp = _current_timestamp()
        pm25_value = round(pm25_value, 2)

        updated = database.update_record_in_database(
            record_id,
            pm25_value,
            category,
            advisory,
            timestamp,
        )

    elif update_type == "location":
        if new_location not in CAMPUS_LOCATIONS:
            raise ValueError("Invalid campus location.")

        updated = database.update_location(
            record_id,
            new_location,
        )

    else:
        raise ValueError("Invalid update type.")

    if not updated:
        raise ValueError(f"Could not update record with ID {record_id}.")

    return database.get_record(record_id)


def delete_record(record_id):
    target = database.get_record(record_id)

    if target is None:
        raise ValueError(f"No record found with ID {record_id}.")

    deleted = database.delete_record_from_database(record_id)

    if not deleted:
        raise ValueError(f"Could not delete record with ID {record_id}.")

    return target

def print_record(record):
    print(
        f"ID {record['id']} | {record['location']}\n"
        f"PM2.5: {record['pm25']} ug/m3 | "
        f"Category: {record['category']}\n"
        f"Advisory: {record['advisory']}\n"
        f"Logged at: {record['timestamp']}"
    )