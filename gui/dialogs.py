from PyQt6.QtWidgets import QMessageBox, QInputDialog

def show_success(parent, title, message):
    QMessageBox.information(parent, title, message)

def show_error(parent, title, message):
    QMessageBox.critical(parent, title, message)

def show_warning(parent, title, message):
    QMessageBox.warning(parent, title, message)

def show_info(parent, title, message):
    QMessageBox.information(parent, title, message)

def confirm_action(parent, title, message):
    result = QMessageBox.question(
        parent,
        title,
        message,
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
    )
    return result == QMessageBox.StandardButton.Yes

def choose_item(parent, title, label, items):
    return QInputDialog.getItem(
        parent,
        title,
        label,
        items,
        0,
        False,
    )