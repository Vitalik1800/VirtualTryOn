# Virtual Try-On

A desktop application for virtual accessory try-on using computer vision technologies.

Version: **1.0**

---

# Overview

Virtual Try-On allows users to preview accessories such as glasses, hats, masks, earrings, necklaces, and watches in real time using a webcam.

The application uses MediaPipe Face Mesh for facial landmark detection and OpenCV for image processing and accessory rendering.

---

# Features

- Real-time webcam processing
- Face landmark detection
- Virtual glasses
- Virtual hats
- Virtual masks
- Virtual earrings
- Virtual necklaces
- Virtual watches
- PNG accessories with alpha channel
- Screenshot capture
- Video recording
- User-friendly graphical interface
- Modular architecture
- Accessory caching
- Windows executable (PyInstaller)

---

# Technologies

- Python 3.12
- OpenCV
- MediaPipe Face Mesh
- NumPy
- CustomTkinter
- PyInstaller

---

# Project Structure

```
VirtualTryOn/
│
├── assets/
├── core/
├── utils/
├── tests/
├── docs/
│   ├── User_Guide.md
│   └── Developer_Guide.md
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Screenshots

Example application screenshots are available in:

```
docs/Screenshots/
```

Example images:

- Main Window
- Glasses
- Hats
- Masks
- Screenshot Feature
- Recording Feature

---

# Installation

## Option 1 — Release Package

1. Download the latest release.
2. Extract the archive.
3. Run:

```
Virtual Try-On.exe
```

No Python installation is required.

---

## Option 2 — Source Code

Clone the repository:

```bash
git clone https://github.com/Vitalik1800/VirtualTryOn.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

# Testing

Run all unit tests:

```bash
python -m unittest discover tests
```

The project includes:

- Unit Tests
- Integration Tests

---

# Documentation

Additional documentation is available in the **docs** directory.

- User_Guide.md
- Developer_Guide.md

---

# System Requirements

Minimum:

- Windows 10 (64-bit)
- Dual-Core CPU
- 4 GB RAM
- Webcam
- 500 MB free disk space

Recommended:

- Windows 11 (64-bit)
- Intel Core i5 / AMD Ryzen 5
- 8 GB RAM
- HD Webcam
- SSD
- 1 GB free disk space

---

# License

This project was developed as part of a bachelor's diploma project.

You may modify and use the source code for educational purposes.

---

# Author

**Vitaly Semchyshyn**

Bachelor's Degree Project

2026

---

# Version

Current release:

**v1.0**