# AIRSENSE — PM2.5 Air Pollution Monitoring & Analysis System
## Project Description

AIRSENSE is a **PM2.5 Air Pollution Monitoring & Analysis System** that retrieves current PM2.5 data through the **Open-Meteo Air Quality API**, classifies the reading according to predefined PM2.5 categories, and stores the resulting air-quality records in a **SQLite database**.

General air-quality applications may provide information for a larger geographic area. AIRSENSE provides a more organized way of recording PM2.5 readings associated with selected locations within the University of Mindanao – Matina Campus.

---

## Project Objectives

The main objectives of AIRSENSE are to:

- Develop a Python-based desktop application for PM2.5 air-quality monitoring.
- Integrate an external API to retrieve current PM2.5 data.
- Classify PM2.5 readings into predefined air-quality categories.
- Implement Create, Read, Update, Delete, and Search operations.
- Provide a user-friendly graphical interface using PyQt6.
- Apply object-oriented programming through PyQt6 window classes and inheritance.
- Provide a simple way to manage historical air-quality records.

---

## Features

- Add Air-Quality Record - The user selects a campus location and clicks **Add Record**. The system retrieves the current PM2.5 value from the Open-Meteo API, classifies it, generates a timestamp, and saves the record to SQLite.
- View Records - The system displays saved air-quality records in a table containing: ID, Location, PM2.5, Category, Advisory, Logged At
- Search Records - Users can search saved records using a location or PM2.5 category keyword.
- Update Record - The system provides two update options:

  **Refresh PM2.5 reading** — retrieves a new PM2.5 value from the API and updates the category, advisory, and timestamp.

  **Change location** — changes the selected location of an existing record.
- Delete Record - Users can select a record and delete it from the SQLite database. A confirmation dialog is displayed before deletion.
- PM2.5 Classification

  The system classifies PM2.5 values into the following categories:

| PM2.5 Range | Category                       |
| ----------- | ------------------------------ |
| 0.0–12.0    | Good                           |
| 12.1–35.4   | Moderate                       |
| 35.5–55.4   | Unhealthy for Sensitive People |
| 55.5–150.4  | Unhealthy                      |
| 150.5–250.4 | Very Unhealthy                 |
| 250.5–500.4 | Hazardous                      |
---

## Technologies Used

- **Programming Language:** Python 3
- **GUI Framework:** PyQt6
- **Database:** SQLite
- **External API:** Open-Meteo Air Quality API
- **HTTP Library:** `requests`
- **Python Standard Libraries:** `sqlite3`, `datetime`, and `pathlib`
- **GUI Styling:** Qt Style Sheets (QSS)
- **Version Control:** Git and GitHub
---

## Project Structure

```text
AIRSENSE_PythonProject/
│
├── api/
│   └── api_module.py
│
├── config/
│   └── config_module.py
│
├── database/
│   └── database.py
│
├── features/
│   └── airsense.py
│
├── gui/
│   ├── dialogs.py
│   ├── main_window.py
│   ├── record_helpers.py
│   ├── records_window.py
│   └── ui_components.py
│
├── main.py
├── .gitignore
└── airsense.db
```

### Folder and File Descriptions
- `main.py` – Starts the AIRSENSE application and launches the PyQt6 main window.
- `api/api_module.py` – Handles the Open-Meteo API connection, retrieves PM2.5 data, and classifies air-quality readings.
- `config/config_module.py` – Stores the API URL, UM Matina coordinates, campus locations, and PM2.5 classification ranges.
- `database/database.py` – Handles the SQLite database connection and CRUD/search operations for air-quality records.
- `features/airsense.py` – Contains the core application logic for adding, viewing, searching, updating, and deleting air-quality records.
- `gui/` – Contains the PyQt6 graphical interface, including the main window, record-management window, dialogs, reusable UI components, and record display helpers.
    
---

## Installation and Setup

### Requirements

Before running AIRSENSE, install:

* Python 3.x
* PyQt6
* Requests

### Step 1 — Clone or Download the Repository
Clone the GitHub repository:

```bash
git clone <GITHUB_REPOSITORY_LINK>
```

Then enter the project directory:

```bash
cd AIRSENSE_PythonProject
```

### Step 2 — Create a Virtual Environment
Creating a virtual environment is recommended.

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 3 — Install Dependencies
Install the required Python libraries:

```bash
pip install PyQt6 requests
```

### Step 4 — Run the Application

Run:

```bash
python main.py
```

The application automatically creates the SQLite database table when it starts.
No manual database creation is required.

---

# 8. How to Use the System

## Adding a Record

1. Open AIRSENSE.
2. Select a campus location from the dropdown menu.
3. Click **Add Record**.
4. The system requests the current PM2.5 value from the Open-Meteo API.
5. The system classifies the PM2.5 value.
6. The record is saved to SQLite.
7. A success message displays the saved information.

## Viewing Records

1. Click **View Record**.
2. The record-management window opens.
3. Saved records are displayed in the table.

## Searching Records

1. Enter a keyword in the Search field.
2. The keyword may refer to a location or PM2.5 category.
3. Click **Search**.
4. Matching records are displayed.

The **Clear** button can be used to clear the search input.

## Updating a Record

1. Select a record from the table.
2. Click **Update Record**.
3. Choose either:

   * Refresh PM2.5 reading
   * Change location
4. Complete the selected operation.

## Deleting a Record

1. Select a record from the table.
2. Click **Delete Record**.
3. Review the confirmation message.
4. Confirm the deletion.
5. The selected record is removed from the database.

## Showing All Records

Click **Show All** to reload and display all saved records.

---

# 9. OOP Implementation

AIRSENSE uses object-oriented programming through PyQt6 window classes.

## Important Classes

### `AirSenseWindow`

Located in:

```text
gui/main_window.py
```

```python
class AirSenseWindow(QMainWindow):
```

This class represents the main AIRSENSE window.

It contains methods for:

* Building the interface.
* Applying styles.
* Adding records.
* Opening the records window.

### `RecordsWindow`

Located in:

```text
gui/records_window.py
```

```python
class RecordsWindow(QMainWindow):
```

This class represents the record-management window.

It contains methods for:

* Displaying records.
* Searching.
* Selecting records.
* Updating records.
* Deleting records.

## Inheritance

Inheritance is applied when the project creates custom window classes from the PyQt6 `QMainWindow` class:

```python
class AirSenseWindow(QMainWindow):
```

and:

```python
class RecordsWindow(QMainWindow):
```

The custom classes inherit the existing functionality provided by `QMainWindow` and extend it with AIRSENSE-specific behavior.

## Encapsulation

Encapsulation is applied by grouping related data and behavior inside classes and modules.

For example, `AirSenseWindow` contains the GUI-related behavior of the main window, while `RecordsWindow` contains the behavior for managing records.

The project also separates responsibilities into different modules, such as the API module, database module, feature module, and GUI modules.

## Polymorphism

No significant custom polymorphism implementation is used in AIRSENSE.

The project primarily demonstrates **classes, objects, and inheritance through PyQt6** rather than implementing a custom polymorphic class hierarchy.

---

# 10. Database

AIRSENSE uses **SQLite** as its local database.

The database file is:

```text
airsense.db
```

The application creates the required table automatically when it starts.

## Database Table

The main table is:

```text
air_quality_records
```

### Table Structure

| Column      | Type    | Description                          |
| ----------- | ------- | ------------------------------------ |
| `id`        | INTEGER | Primary key with automatic numbering |
| `location`  | TEXT    | Selected campus location             |
| `pm25`      | REAL    | PM2.5 reading                        |
| `category`  | TEXT    | PM2.5 classification                 |
| `advisory`  | TEXT    | Air-quality advisory                 |
| `timestamp` | TEXT    | Date and time the record was logged  |

## Database Operations

### Create

A new record is inserted using an SQL `INSERT` operation.

```sql
INSERT INTO air_quality_records
```

### Read

Records are retrieved using SQL `SELECT` operations.

The system can retrieve:

* All records.
* One record by ID.

### Update

The system uses SQL `UPDATE` operations to:

* Refresh PM2.5 information.
* Update the category and advisory.
* Update the timestamp.
* Change the selected location.

### Delete

The system uses SQL `DELETE` to remove a selected record.

### Search

The system searches the database using the location or category fields with SQL `LIKE`.

---

# 11. Screenshots

The following screenshots should be added to this section before final submission.

## Main Window

**Description:** Shows the main AIRSENSE interface where the user can select a campus location and add a new PM2.5 record.

```text
[Insert Main Window Screenshot Here]
```

## Record Management Window

**Description:** Shows the table containing saved PM2.5 air-quality records.

```text
[Insert Records Window Screenshot Here]
```

## Search Feature

**Description:** Shows the search field and the resulting records after searching by location or PM2.5 category.

```text
[Insert Search Screenshot Here]
```

## Update Feature

**Description:** Shows the update options for refreshing the PM2.5 reading or changing the record location.

```text
[Insert Update Screenshot Here]
```

## Delete Feature

**Description:** Shows the confirmation dialog displayed before deleting a selected air-quality record.

```text
[Insert Delete Confirmation Screenshot Here]
```

---

# 12. Testing

The system was tested by performing the major operations available in AIRSENSE.

| Test Case                         | Expected Result                                            | Actual Result |
| --------------------------------- | ---------------------------------------------------------- | ------------- |
| Add a valid record                | The system retrieves PM2.5 data and saves a new record.    | Passed        |
| View records                      | Saved records are displayed in the table.                  | Passed        |
| Search by location                | Matching records are displayed.                            | Passed        |
| Search by category                | Records with the matching category are displayed.          | Passed        |
| Search with empty input           | The system displays a warning message.                     | Passed        |
| Update PM2.5                      | A new PM2.5 value is retrieved and the record is updated.  | Passed        |
| Change location                   | The selected record's location is updated.                 | Passed        |
| Update without selecting a record | The system displays a warning.                             | Passed        |
| Delete a record                   | The selected record is removed from SQLite.                | Passed        |
| Cancel deletion                   | The record remains in the database.                        | Passed        |
| Delete without selecting a record | The system displays a warning.                             | Passed        |
| Invalid campus location           | The system rejects the invalid location.                   | Passed        |
| Database initialization           | The required SQLite table is created if it does not exist. | Passed        |
| API error                         | The system displays an error instead of silently failing.  | Passed        |

---

# 13. Known Issues / Limitations

1. **API Dependency**
   Adding or refreshing a PM2.5 record requires an internet connection because the system retrieves data from the Open-Meteo Air Quality API.

2. **Coordinate-Based API Data**
   The application uses the configured UM Matina latitude and longitude. The selected campus locations are organizational labels and do not represent separate physical air-quality sensors.

3. **No Physical Sensors**
   AIRSENSE does not directly measure PM2.5 using hardware sensors.

4. **No Separate AQI Calculation**
   The system classifies the retrieved PM2.5 concentration using predefined PM2.5 ranges. It does not calculate or display a separate Air Quality Index (AQI).

5. **Desktop Application**
   AIRSENSE is currently designed as a desktop Python application using PyQt6.

6. **Local Database**
   The SQLite database is stored locally on the computer running the application. Records are not automatically synchronized between different computers.

7. **API Availability**
   If the external Open-Meteo service is unavailable or does not return a PM2.5 value, the system cannot retrieve a new reading.

---

# 14. Author

**Name:** [Your Full Name]

**Section:** [Your Section]

**Course:** Bachelor of Science in Computer Science

**University:** University of Mindanao – Matina Campus

---

# 15. GitHub Repository

**GitHub Repository:** [Insert GitHub Repository Link Here]

---

# Conclusion

AIRSENSE demonstrates the integration of **Python programming, modular programming, API integration, PyQt6 GUI development, SQLite database management, CRUD operations, search functionality, error handling, and object-oriented programming** into a single desktop application.

The system provides a structured way to retrieve, classify, store, and manage PM2.5 air-quality records for selected locations associated with the University of Mindanao – Matina Campus.
