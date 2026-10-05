#AIRSENSE: PM2.5 Air Pollution Monitoring & Analysis System

from database.database import create_database
from gui.main_window import main as start_gui

def main():
    create_database()
    start_gui()

if __name__ == "__main__":
    main()