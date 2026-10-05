from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
)

from config.config_module import CAMPUS_LOCATIONS
from features import airsense
from gui.dialogs import show_error, show_success
from gui.records_window import RecordsWindow
from gui.ui_components import create_central_widget


class AirSenseWindow(QMainWindow):
    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F7F9FB;
            }

            QLabel {
                color: #111111;
            }

            QComboBox {
                background-color: white;
                border: 1px solid #B8C9D6;
                border-radius: 5px;
                padding: 6px;
            }

            QComboBox:focus {
                border: 2px solid #2E8EB5;
            }

            QPushButton {
                background-color: #2E8EB5;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 18px;
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
        """)

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "AIRSENSE - PM2.5 Air Quality Monitoring System"
        )

        self.resize(700, 350)

        screen = QApplication.primaryScreen().availableGeometry()
        window = self.frameGeometry()
        window.moveCenter(screen.center())
        self.move(window.topLeft())

        self.records_window = None

        airsense.initialize_records()

        self.apply_styles()
        self.build_interface()

    def build_interface(self):
        central_widget, main_layout = create_central_widget()
        self.setCentralWidget(central_widget)

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

        main_layout.addWidget(title)

        location_layout = QHBoxLayout()

        location_label = QLabel(
            "Select Location:"
        )

        self.location_combo = QComboBox()
        self.location_combo.addItems(
            CAMPUS_LOCATIONS
        )

        location_layout.addWidget(
            location_label
        )

        location_layout.addWidget(
            self.location_combo
        )

        main_layout.addLayout(
            location_layout
        )

        self.add_button = QPushButton(
            "Add Record"
        )

        self.add_button.clicked.connect(
            self.add_record
        )

        main_layout.addWidget(
            self.add_button
        )

        self.view_button = QPushButton(
            "View Record"
        )

        self.view_button.clicked.connect(
            self.open_records_window
        )

        main_layout.addWidget(
            self.view_button
        )

    def add_record(self):
        location = self.location_combo.currentText()

        try:
            record = airsense.add_record(
                location
            )

            show_success(
                self,
                "Success",
                (
                    "Air quality record added "
                    "successfully.\n\n"
                    f"Location: {record['location']}\n"
                    f"PM2.5: {record['pm25']} ug/m3\n"
                    f"Category: {record['category']}"
                ),
            )

            if self.records_window is not None:
                self.records_window.refresh_table()

        except Exception as error:
            show_error(
                self,
                "Error",
                f"Could not add record:\n\n{error}",
            )

    def open_records_window(self):
        if self.records_window is None:
            self.records_window = RecordsWindow(
                self
            )

        self.records_window.refresh_table()

        self.records_window.show()
        self.records_window.raise_()
        self.records_window.activateWindow()

def main():
    app = QApplication([])

    window = AirSenseWindow()
    window.show()

    return app.exec()