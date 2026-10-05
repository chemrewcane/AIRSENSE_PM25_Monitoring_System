from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
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
    apply_records_window_style,
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

        apply_records_window_style(self)

        self.build_interface()

        self.refresh_table()

    def build_interface(self):
        central_widget, main_layout = (
            create_central_widget()
        )

        self.setCentralWidget(
            central_widget
        )

        self._build_title(
            main_layout
        )

        self._build_search_controls(
            main_layout
        )

        self._build_table(
            main_layout
        )

        self._build_action_controls(
            main_layout
        )

    def _build_title(self, main_layout):
        title = QLabel(
            "AIRSENSE\n"
            "PM2.5 AIR POLLUTION MONITORING & ANALYSIS SYSTEM"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setStyleSheet("""
            background-color: #2E8EB5;
            color: white;
            border-radius: 8px;
            font-size: 22px;
            font-weight: bold;
            padding: 12px;
        """)

        main_layout.addWidget(
            title
        )

    def _build_search_controls(self, main_layout):
        (
            layout,
            self.search_input,
            self.search_button,
            self.clear_button,
        ) = create_search_section()

        self.search_button.clicked.connect(
            self.search_records
        )

        self.clear_button.clicked.connect(
            self.clear_search
        )

        self.search_input.returnPressed.connect(
            self.search_records
        )

        main_layout.addLayout(
            layout
        )

    def _build_table(self, main_layout):
        self.table = create_records_table()

        main_layout.addWidget(
            self.table
        )

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
            self.refresh_table
        )

        main_layout.addLayout(
            layout
        )

    def refresh_table(self):
        records = airsense.get_records()

        display_records(
            self.table,
            records,
        )

    def clear_search(self):
        self.search_input.clear()

    def search_records(self):
        keyword = (
            self.search_input
            .text()
            .strip()
        )

        if not keyword:
            show_warning(
                self,
                "Search",
                "Please enter a search keyword.",
            )
            return

        results = airsense.search_records(
            keyword
        )

        display_records(
            self.table,
            results,
        )

        if not results:
            show_info(
                self,
                "Search Results",
                f"No records matched '{keyword}'.",
            )

    def get_selected_record(self):
        selected_rows = (
            self.table
            .selectionModel()
            .selectedRows()
        )

        if not selected_rows:
            show_warning(
                self,
                "No Record Selected",
                "Please select a record first.",
            )
            return None

        row = selected_rows[0].row()

        record_id_item = (
            self.table.item(
                row,
                0,
            )
        )

        if record_id_item is None:
            return None

        try:
            record_id = record_id_item.data(
                Qt.ItemDataRole.UserRole
            )

        except Exception:
            show_error(
                self,
                "Error",
                "The selected record has an invalid ID.",
            )
            return None

        record = (
            airsense.database.get_record(
                record_id
            )
        )

        if record is None:
            show_warning(
                self,
                "Error",
                "The selected record could not be found.",
            )
        return record

    def update_record(self):
        target = (
            self.get_selected_record()
        )

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
            self._refresh_pm25(
                target
            )

        else:
            self._change_location(
                target
            )

    def _refresh_pm25(self, target):
        try:
            updated_record = (
                airsense.update_record(
                    target["id"],
                    "refresh",
                )
            )

            show_success(
                self,
                "Success",
                (
                    "PM2.5 reading updated "
                    "successfully.\n\n"
                    f"New PM2.5: "
                    f"{updated_record['pm25']} ug/m3\n"
                    f"Category: "
                    f"{updated_record['category']}"
                ),
            )

            self.refresh_table()

        except Exception as error:
            show_error(
                self,
                "Error",
                (
                    "Could not refresh the "
                    f"PM2.5 reading:\n\n{error}"
                ),
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
                (
                    "Could not update location:"
                    f"\n\n{error}"
                ),
            )

    def delete_record(self):
        target = (
            self.get_selected_record()
        )

        if target is None:
            return

        confirmed = confirm_action(
            self,
            "Delete Record",
            (
                "Are you sure you want to "
                "delete this record?\n\n"
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