"""
    Project: Virtual Try-On

    Stage: 1
    Substage: 1.7 - Environment Verification

    Description:
    Initial application startup and verification of the development environment.
"""

# ===
# Stage 1.7
# Import required libraries
# ===

import customtkinter as ctk
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

def main():
    # ===
    # Stage 1.7
    # Configure CustomTkinter
    # ===

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # ===
    # Stage 1.7
    # Create the main application window
    # ===

    app = ctk.CTk()
    app.title("Virtual Try-On")
    app.geometry("900x600")
    app.resizable(False, False)

    # ===
    # Stage 1.7
    # Create the welcome Label
    # ===

    label = ctk.CTkLabel(
        master=app,
        text="Virtual Try-On\nDevelopment Environment Ready",
        font=("Segoe UI", 22, "bold")
    )

    label.pack(expand=True)

    # ===
    # Stage 1.7
    # Start the application
    # ===

    app.mainloop()

if __name__ == "__main__":
    main()
