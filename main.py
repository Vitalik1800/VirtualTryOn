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

# ===
# Stage 2.1
# Application entry point
# ===

def main():
    app = MainWindow()
    app.run()

if __name__ == "__main__":
    main()
