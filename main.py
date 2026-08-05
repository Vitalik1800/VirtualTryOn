"""
    Project: Virtual Try-On

    Stage: 2
    Substage: 2.1 - Create Main Window

    Description:
    Application entry point.
"""

# ===
# Stage 2.1
# Import main window
# ===

from ui.main_window import MainWindow
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(
            "virtual_try_on.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ]
)

# ===
# Stage 2.1
# Application entry point
# ===

def main():
    app = MainWindow()
    app.run()

if __name__ == "__main__":
    main()
