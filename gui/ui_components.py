from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QHeaderView,
)

def create_title():
    title = QLabel(
        "AIRSENSE\n"
        "PM2.5 Air Quality Monitoring & Analysis System"
    )

    title.setAlignment(
        Qt.AlignmentFlag.AlignCenter
    )

    title.setStyleSheet(
        "font-size: 24px;"
        "font-weight: bold;"
        "padding: 15px;"
    )

    return title

def create_location_section(locations):
    layout = QHBoxLayout()

    label = QLabel(
        "Select Location:"
    )

    combo = QComboBox()
    combo.addItems(
        locations
    )

    button = QPushButton(
        "Add Record"
    )

    layout.addWidget(
        label
    )

    layout.addWidget(
        combo
    )

    layout.addWidget(
        button
    )

    return (
        layout,
        combo,
        button,
    )

def create_search_section():
    layout = QHBoxLayout()

    label = QLabel(
        "Search:"
    )

    search_input = QLineEdit()

    search_input.setPlaceholderText(
        "Enter location or category..."
    )

    search_button = QPushButton(
        "Search"
    )

    clear_button = QPushButton(
        "Clear"
    )

    layout.addWidget(
        label
    )

    layout.addWidget(
        search_input
    )

    layout.addWidget(
        search_button
    )

    layout.addWidget(
        clear_button
    )

    return (
        layout,
        search_input,
        search_button,
        clear_button,
    )

def create_records_table():
    table = QTableWidget()

    table.setColumnCount(6)

    table.setHorizontalHeaderLabels(
        [
            "ID",
            "Location",
            "PM2.5",
            "Category",
            "Advisory",
            "Logged At",
        ]
    )

    table.verticalHeader().setVisible(False)

    table.setEditTriggers(
        QTableWidget.EditTrigger.NoEditTriggers
    )

    table.setSelectionBehavior(
        QTableWidget.SelectionBehavior.SelectRows
    )

    table.setSelectionMode(
        QTableWidget.SelectionMode.SingleSelection
    )

    table.horizontalHeader().setSectionResizeMode(
        QHeaderView.ResizeMode.Stretch
    )

    return table

def create_action_section():
    layout = QHBoxLayout()

    update_button = QPushButton(
        "Update Record"
    )

    delete_button = QPushButton(
        "Delete Record"
    )

    show_all_button = QPushButton(
        "Show All"
    )

    layout.addWidget(
        update_button
    )

    layout.addWidget(
        delete_button
    )

    layout.addWidget(
        show_all_button
    )

    return (
        layout,
        update_button,
        delete_button,
        show_all_button,
    )


def create_status_label():
    label = QLabel(
        "Ready."
    )

    label.setAlignment(
        Qt.AlignmentFlag.AlignCenter
    )

    label.setStyleSheet(
        "padding: 8px;"
    )

    return label

def create_central_widget():
    widget = QWidget()

    layout = QVBoxLayout(
        widget
    )

    return (
        widget,
        layout,
    )
    
def apply_records_window_style(window):
    window.setStyleSheet("""
        QMainWindow {
            background-color: #F7F9FB;
        }

        QLabel {
            color: #111111;
        }

        QLineEdit {
            background-color: white;
            border: 1px solid #B8C9D6;
            border-radius: 5px;
            padding: 6px;
        }

        QLineEdit:focus {
            border: 2px solid #2E8EB5;
        }

        QPushButton {
            background-color: #2E8EB5;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px 14px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #25799B;
            color: white;
        }

        QPushButton:pressed {
            background-color: #1F6683;
            color: white;
        }

        QTableWidget {
            background-color: white;
            border: 1px solid #2E8EB5;
            gridline-color: #B8B8B8;
            selection-background-color: #D9EAF2;
            selection-color: #222222;
            border-radius: 5px;
        }

        QHeaderView::section {
            background-color: #2E8EB5;
            color: white;
            padding: 7px;
            border: 1px solid #2E8EB5;
            font-weight: bold;
        }
    """)

def add_record_to_table(table, record, display_id=None):
    row = table.rowCount()

    table.insertRow(row)

    if display_id is None:
        display_id = row + 1

    values = [
        display_id,
        record["location"],
        record["pm25"],
        record["category"],
        record["advisory"],
        record["timestamp"],
    ]

    for column, value in enumerate(values):
        item = QTableWidgetItem(str(value))

        # Center the text in every cell.
        item.setTextAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        # Store the real SQLite ID internally.
        if column == 0:
            item.setData(
                Qt.ItemDataRole.UserRole,
                record["id"]
            )

        table.setItem(
            row,
            column,
            item
        )
        
def clear_table(table):
    table.setRowCount(0)