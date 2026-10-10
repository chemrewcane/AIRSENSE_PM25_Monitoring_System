from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QHeaderView

from gui.ui_components import (
    add_record_to_table,
    clear_table,
)

def category_color(category):
    colors = {
        "Good": "#C8E6C9",
        "Moderate": "#FFF3CD",
        "Unhealthy for Sensitive People": "#FFE0B2",
        "Unhealthy": "#FFCDD2",
        "Very Unhealthy": "#E1BEE7",
        "Hazardous": "#D7CCC8",
    }
    return colors.get(category, "#FFFFFF")

def color_record_row(table, row, category):
    color = category_color(category)
    for column in range(table.columnCount()):
        item = table.item(row, column)
        if item:
            item.setBackground(QColor(color))

def display_records(table, records):
    clear_table(table)

    for index, record in enumerate(records, start=1):
        add_record_to_table(
            table,
            record,
            display_id=index,
        )

        row = table.rowCount() - 1

        color_record_row(
            table,
            row,
            record["category"],
        )

    table.horizontalHeader().setSectionResizeMode(
        QHeaderView.ResizeMode.Stretch
    )
