from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMainWindow,
    QHeaderView,
    QSizePolicy
)

from config.config_module import CAMPUS_LOCATIONS
from features import airsense

from gui.dialogs import (
    choose_item,
    confirm_action,
    show_error,
    show_info,
    show_success,
    show_warning,
)

from gui.record_helpers import display_records

from gui.ui_components import (
    create_action_section,
    create_central_widget,
    create_records_table,
    create_search_section,
)

class RecordsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle(
            "AIRSENSE - Air Quality Records"
        )
        self.resize(1100, 650)

        screen = QApplication.primaryScreen().availableGeometry()
        window = self.frameGeometry()
        window.moveCenter(screen.center())
        self.move(window.topLeft())

        self.apply_styles()
        self.build_interface()
        self.refresh_table()

    def apply_styles(self):
        self.setStyleSheet("""
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
                border: 1px solid #C8D6DF;
                gridline-color: #D9E2E8;
                selection-background-color: #B9DDF0;
                selection-color: #17324D;
                border-radius: 5px;
            }

            QHeaderView::section {
                background-color: #2E8EB5;
                color: white;
                padding: 7px;
                border: none;
                font-weight: bold;
            }
        """)

    def build_interface(self):
        from PyQt6.QtCore import Qt

        central_widget, main_layout = create_central_widget()
        self.setCentralWidget(central_widget)

        title = QLabel(
            "AIRSENSE\n"
            "PM2.5 AIR POLLUTION MONITORING & ANALYSIS SYSTEM"
        )
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            background-color: #2E8EB5;
            color: white;
            border-radius: 8px;
            font-size: 22px;
            font-weight: bold;
            padding: 12px;
        """)
        main_layout.addWidget(title)

        add_layout = QHBoxLayout()

        location_label = QLabel("Select Location:")
        location_label.setMinimumWidth(100)
        add_layout.addWidget(location_label)

        self.location_combo = QComboBox()
        self.location_combo.addItems(CAMPUS_LOCATIONS)

        self.location_combo.setMinimumWidth(0)
        self.location_combo.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )
        
        add_layout.addWidget(self.location_combo, 1)

        self.add_button = QPushButton("Add Record")
        self.add_button.setFixedHeight(32)
        self.add_button.setFixedWidth(127)
        self.add_button.clicked.connect(self.add_record)

        add_layout.addWidget(self.add_button)
        main_layout.addLayout(add_layout)

        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Search by Location:"))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter a campus location...")
        self.search_button = QPushButton("Search")
        self.clear_button = QPushButton("Clear")
        self.search_button.clicked.connect(self.search_records)
        self.clear_button.clicked.connect(self.clear_search)
        self.search_input.returnPressed.connect(self.search_records)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        search_layout.addWidget(self.clear_button)
        main_layout.addLayout(search_layout)

        category_layout = QHBoxLayout()
        category_layout.addWidget(QLabel("Filter by Category:"))
        self.category_combo = QComboBox()
        self.category_combo.addItems([
            "All Categories",
            "Good",
            "Moderate",
            "Unhealthy for Sensitive People",
            "Unhealthy",
            "Very Unhealthy",
            "Hazardous",
        ])
        self.category_combo.currentTextChanged.connect(self.apply_filters)
        category_layout.addWidget(self.category_combo)
        category_layout.addStretch()
        main_layout.addLayout(category_layout)

        self.table = create_records_table()
        main_layout.addWidget(self.table)

        self._build_action_controls(main_layout)

    def _build_search_controls(self, main_layout):
        (
            layout,
            self.search_input,
            self.search_button,
            self.clear_button,
        ) = create_search_section()

        self.search_button.clicked.connect(self.search_records)
        self.clear_button.clicked.connect(self.clear_search)
        self.search_input.returnPressed.connect(self.search_records)
        main_layout.addLayout(layout)

    def _build_action_controls(self, main_layout):
        (
            layout,
            self.update_button,
            self.delete_button,
            self.show_all_button,
        ) = create_action_section()

        self.update_button.clicked.connect(
            self.update_record
        )

        self.delete_button.clicked.connect(
            self.delete_record
        )

        self.show_all_button.clicked.connect(
            self.show_all_records
        )

        main_layout.addLayout(layout)

    def show_all_records(self):
        self.search_input.clear()
        self.category_combo.setCurrentIndex(0)
        self.refresh_table()

    def add_record(self):
        location = self.location_combo.currentText()
        try:
            record = airsense.add_record(location)
            show_success(
                self,
                "Success",
                (
                    "Air quality record added successfully.\n\n"
                    f"Location: {record['location']}\n"
                    f"PM2.5: {record['pm25']} ug/m3\n"
                    f"Category: {record['category']}"
                ),
            )
            self.apply_filters()
        except Exception as error:
            show_error(self, "Error", f"Could not add record:\n\n{error}")

    def refresh_table(self):
        self.apply_filters()

    def apply_filters(self, *_args):
        keyword = self.search_input.text().strip()
        category = self.category_combo.currentText()

        if keyword:
            records = airsense.search_records(keyword)
        else:
            records = airsense.get_records()

        if category != "All Categories":
            records = [record for record in records if record["category"] == category]

        
        display_records(self.table, records)

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.table.horizontalHeader().setStretchLastSection(True)
    
    def clear_search(self):
        self.search_input.clear()

    def search_records(self):
        keyword = self.search_input.text().strip()
        if not keyword:
            show_warning(self, "Search", "Please enter a campus location.")
            return
        self.apply_filters()

    def get_selected_record(self):
        row = self.table.currentRow()

        if row < 0:
            show_warning(
                self,
                "No Record Selected",
                "Please select a record first.",
            )
            return None

        record_id_item = self.table.item(row, 0)

        if record_id_item is None:
            show_error(
                self,
                "Error",
                "The selected record has an invalid ID.",
            )
            return None

        record_id = record_id_item.data(
            Qt.ItemDataRole.UserRole
        )

        if record_id is None:
            try:
                record_id = int(record_id_item.text())
            except (ValueError, TypeError):
                show_error(
                    self,
                    "Error",
                    "The selected record has an invalid ID.",
                )
                return None

        record = airsense.database.get_record(int(record_id))

        if record is None:
            show_warning(
                self,
                "Error",
                "The selected record could not be found.",
            )
            return None

        return record

    def update_record(self):
        target = self.get_selected_record()

        if target is None:
            return

        options = [
            "Refresh PM2.5 reading",
            "Change location",
        ]

        choice, ok = choose_item(
            self,
            "Update Record",
            "What would you like to update?",
            options,
        )

        if not ok:
            return

        if choice == "Refresh PM2.5 reading":
            self._refresh_pm25(target)
        else:
            self._change_location(target)

    def _refresh_pm25(self, target):
        try:
            updated_record = airsense.update_record(
                target["id"],
                "refresh",
            )

            show_success(
                self,
                "Success",
                (
                    "PM2.5 reading updated successfully.\n\n"
                    f"New PM2.5: {updated_record['pm25']} ug/m3\n"
                    f"Category: {updated_record['category']}"
                ),
            )

            self.refresh_table()

        except Exception as error:
            show_error(
                self,
                "Error",
                f"Could not refresh the PM2.5 reading:\n\n{error}",
            )

    def _change_location(self, target):
        new_location, ok = choose_item(
            self,
            "Change Location",
            "Select new location:",
            CAMPUS_LOCATIONS,
        )

        if not ok:
            return

        try:
            airsense.update_record(
                target["id"],
                "location",
                new_location,
            )

            show_success(
                self,
                "Success",
                "Location updated successfully.",
            )

            self.refresh_table()

        except Exception as error:
            show_error(
                self,
                "Error",
                f"Could not update location:\n\n{error}",
            )

    def delete_record(self):
        target = self.get_selected_record()

        if target is None:
            return

        confirmed = confirm_action(
            self,
            "Delete Record",
            (
                "Are you sure you want to delete this record?\n\n"
                f"ID: {target['id']}\n"
                f"Location: {target['location']}\n"
                f"PM2.5: {target['pm25']} ug/m3"
            ),
        )

        if not confirmed:
            return

        try:
            airsense.delete_record(
                target["id"]
            )

            show_success(
                self,
                "Success",
                "Air quality record deleted successfully.",
            )

            self.refresh_table()

        except Exception as error:
            show_error(
                self,
                "Error",
                f"Could not delete record:\n\n{error}",
            )
