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
    QSizePolicy
)

def create_title():
    title = QLabel(
        "AIRSENSE\n"
        "PM2.5 Air Quality Monitoring & Analysis System"
    )
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title.setStyleSheet(
        "font-size: 24px;"
        "font-weight: bold;"
        "padding: 15px;"
    )
    return title

def create_location_section(locations):
    layout = QHBoxLayout()
    label = QLabel("Select Location:")
    combo = QComboBox()
    combo.addItems(locations)
    button = QPushButton("Add Record")

    layout.addWidget(label)
    layout.addWidget(combo)
    layout.addWidget(button)

    return layout, combo, button

def create_search_section():
    layout = QHBoxLayout()
    label = QLabel("Search:")
    search_input = QLineEdit()
    search_input.setPlaceholderText("Enter location or category...")
    search_button = QPushButton("Search")
    show_all_button = QPushButton("Show All")

    layout.addWidget(label)
    layout.addWidget(search_input)
    layout.addWidget(search_button)
    layout.addWidget(show_all_button)

    return layout, search_input, search_button, show_all_button

def create_records_table():
    table = QTableWidget()
    table.verticalHeader().setVisible(False)

    table.setColumnCount(6)
    table.setHorizontalHeaderLabels([
        "ID",
        "Location",
        "PM2.5",
        "Category",
        "Advisory",
        "Logged At",
    ])

    table.setEditTriggers(
        QTableWidget.EditTrigger.NoEditTriggers
    )
    table.setSelectionBehavior(
        QTableWidget.SelectionBehavior.SelectRows
    )
    table.setSelectionMode(
        QTableWidget.SelectionMode.SingleSelection
    )

    table.setMinimumWidth(0)
    table.setSizePolicy(
        QSizePolicy.Policy.Expanding,
        QSizePolicy.Policy.Expanding,
    )

    header = table.horizontalHeader()
    header.setSectionResizeMode(
        QHeaderView.ResizeMode.Stretch
    )
    header.setStretchLastSection(True)

    return table

def create_action_section():
    layout = QHBoxLayout()
    update_button = QPushButton("Update Record")
    delete_button = QPushButton("Delete Record")
    refresh_button = QPushButton("Show All")

    layout.addWidget(update_button)
    layout.addWidget(delete_button)
    layout.addWidget(refresh_button)

    return layout, update_button, delete_button, refresh_button

def create_status_label():
    label = QLabel("Ready.")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setStyleSheet("padding: 8px;")
    return label

def create_central_widget():
    widget = QWidget()
    layout = QVBoxLayout(widget)
    return widget, layout

def add_record_to_table(table, record, display_id=None):
    row = table.rowCount()
    table.insertRow(row)

    values = [
        record["id"] if display_id is None else display_id,
        record["location"],
        record["pm25"],
        record["category"],
        record["advisory"],
        record["timestamp"],
    ]

    
    for column, value in enumerate(values):
        item = QTableWidgetItem(str(value))

        item.setTextAlignment(
            Qt.AlignmentFlag.AlignCenter
            | Qt.AlignmentFlag.AlignVCenter
        )

        if column == 0:
            item.setData(
                Qt.ItemDataRole.UserRole,
                record["id"],
            )

        table.setItem(row, column, item)

def clear_table(table):
    table.setRowCount(0)
