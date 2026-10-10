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
- View Records - The system displays saved air-quality records in a table containing: ID, Location, PM2.5, Category, Advisory, Logged At.
- Search by Location - Users can search for saved records using a campus location keyword. The search field searches locations only.
- Filter by Category – Users can select a PM2.5 category from a dropdown to display records that match the selected category. The category filter can be combined with the location search.
- Clear Search – Clears the location search input without automatically resetting the category filter.
- Show All Records – Resets the search and category filters and displays all saved records.
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
git clone <https://github.com/chemrewcane/AIRSENSE_PM25_Monitoring_System>
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

## How to Use the System

1. Run `main.py` to launch AIRSENSE.
2. Select a campus location from the **Select Location** dropdown in the main window.
3. Click **Add Record** to retrieve the current PM2.5 reading and save it to the SQLite database.
4. Select **View Record** to open the records window.
5. Use the **Search Location** field to find records by campus location.
6. Use the **Filter by Category** dropdown to display records belonging to a specific PM2.5 category.
7. Click **Search** to apply the location search.
8. Click **Clear** to clear the search input.
9. Click **Show All** to reset the search and category filters and display all records.
10. Select a record and click **Update Record** to refresh its PM2.5 reading or change its location.
11. Select a record and click **Delete Record** to remove it after confirming the deletion.
12. Close the application when finished.

---

## OOP Implementation

AIRSENSE uses classes to organize the graphical interface.

Important classes:

- `AirSenseWindow` – Represents the main AIRSENSE window and handles location selection, adding records, and opening the record-management window.
- `RecordsWindow` – Represents the record-management window and handles viewing, searching, updating, and deleting air-quality records.

### Encapsulation

Encapsulation is applied by grouping related data and behavior into classes and separating the responsibilities of different modules. For example, `AirSenseWindow` handles the main GUI operations, while `RecordsWindow` handles record-management operations. Database and API operations are also separated into their respective modules.

### Inheritance

Inheritance is used mainly through PyQt6. `AirSenseWindow` and `RecordsWindow` both inherit from `QMainWindow`, allowing them to use the built-in functionality provided by PyQt6 while adding AIRSENSE-specific behavior.

### Polymorphism

The project mainly demonstrates polymorphism through PyQt6's inherited GUI behavior. The custom window classes inherit functionality from `QMainWindow` while providing their own application-specific implementations.

---

## Database

AIRSENSE uses a SQLite database named `airsense.db`.

### air_quality_records Table

The `air_quality_records` table stores:

- `id` – Unique record ID generated automatically by the database.
- `location` – Selected location within the University of Mindanao – Matina Campus.
- `pm25` – Retrieved PM2.5 air-quality reading.
- `category` – PM2.5 classification such as Good, Moderate, or Unhealthy.
- `advisory` – Health advisory associated with the PM2.5 category.
- `timestamp` – Date and time when the record was logged.

### Database Operations

The system performs the following main operations:

- **Create** – Add new PM2.5 air-quality records.
- **Read** – Retrieve all records or find a specific record by its ID.
- **Update** – Refresh the PM2.5 reading or change the location of a record.
- **Delete** – Delete a selected air-quality record.
- **Search** – Search records by location or PM2.5 category.
  
---

## Screenshots

### Main Window
<img width="692" height="376" alt="image" src="https://github.com/user-attachments/assets/7dc2cf78-9a29-4f8a-84ac-abd595843db7" />

- Shows the main AIRSENSE interface where the user can select a campus location and add a new PM2.5 record.

### Record Management Window
<img width="1088" height="672" alt="image" src="https://github.com/user-attachments/assets/7ea71f08-0f85-4b32-865b-cdbae1443d42" />

- Shows the table containing saved PM2.5 air-quality records.
---

## Testing

The system was tested by performing the major operations available in AIRSENSE.

| Test Case                         | Expected Result                                              | Actual Result        |
| --------------------------------- | ------------------------------------------------------------ | -------------------- |
| Add a valid record                | The system retrieves PM2.5 data and saves a new record.      | Passed               |
| View records                      | Saved records are displayed in the table.                    | Passed               |
| Search by location                | Only records matching the location keyword are displayed.    | Passed               |
| Filter by category                | Only records matching the selected category are displayed.   | Passed               |
| Search with empty input           | The system displays a warning message.                       | Passed               |
| Clear search                      | The search input is cleared.                                 | Passed               |
| Show All records                  | Both filters are reset, and all saved records are displayed. | Passed               |
| Update PM2.5                      | A new PM2.5 value is retrieved and the record is updated.    | Passed               |
| Change location                   | The selected record's location is updated.                   | Passed               |
| Update without selecting a record | The system displays a warning.                               | Passed               |
| Delete a record                   | The selected record is removed from SQLite.                  | Passed               |
| Cancel deletion                   | The record remains in the database.                          | Passed               |
| Delete without selecting a record | The system displays a warning.                               | Passed               |
| Invalid campus location           | The system rejects the invalid location.                     | Passed               |
| Database initialization           | The required SQLite table is created if it does not exist.   | Passed               |
| API error                         | The system displays an error instead of silently failing.    | Passed               |

---

## Known Issues / Limitations

1. **API Dependency**
   Adding or refreshing a PM2.5 record requires an internet connection because the system retrieves data from the Open-Meteo Air Quality API.

2. **Coordinate-Based API Data**
   The application uses the configured UM Matina latitude and longitude. The selected campus locations are organizational labels and do not represent separate physical air-quality sensors.

3. **No Physical Sensors**
   AIRSENSE does not directly measure PM2.5 using hardware sensors.

4. **Local Database**
   The SQLite database is stored locally on the computer running the application. Records are not automatically synchronized between different computers.

5. **API Availability**
   If the external Open-Meteo service is unavailable or does not return a PM2.5 value, the system cannot retrieve a new reading.

---

## Author

**Name:** Wrench Maxenne Callao Singcol


**Section:** 3581

---

## GitHub Repository

https://github.com/chemrewcane/AIRSENSE_PM25_Monitoring_System
