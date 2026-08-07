# Virtual Try-On Developer Guide

**Project:** Virtual Try-On

**Version:** 1.0

**Author:** Vitaly Semchyshyn

---

# Table of Contents

1. Project Structure
2. Technologies
3. Architecture
4. Module Description
5. Development Guide

---

# 1. Project Structure

```
VirtualTryOn/
│
├── assets/
│   ├── accessories/
│   │   ├── glasses/
│   │   ├── hats/
│   │   ├── masks/
│   │
│   └── icons/
│
├── core/
│
├── utils/
│
├── docs/
│   ├── User_Guide.md
│   └── Developer_Guide.md
│
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

The project follows a modular architecture. Each package is responsible for a specific part of the application.

---

# 2. Technologies

## Programming Language

- Python 3.12

## Computer Vision

- OpenCV
- MediaPipe Face Mesh

## GUI

- CustomTkinter

## Image Processing

- NumPy

## Packaging

- PyInstaller

## Testing

- unittest

---

# 3. Architecture

The application is divided into independent modules.

```
+----------------------+
|       GUI            |
+----------+-----------+
           |
           v
+----------------------+
|  Camera Controller   |
+----------+-----------+
           |
           v
+----------------------+
|   Face Detector      |
+----------+-----------+
           |
           v
+----------------------+
| Accessory Renderer   |
+----------+-----------+
           |
           v
+----------------------+
| Accessory Manager    |
+----------+-----------+
           |
           v
+----------------------+
| Asset Storage        |
+----------------------+
```

The GUI communicates with the camera module.

The camera provides frames to the face detector.

Detected landmarks are passed to the renderer.

The renderer obtains accessory images from the Accessory Manager.

---

# 4. Module Description

## main.py

Application entry point.

Responsibilities:

- initialize application;
- create main window;
- start camera;
- launch GUI.

---

## config/

Contains application configuration.

Examples:

- application settings;
- UI constants;
- colors;
- fonts;
- default parameters.

---

## detectors/

Contains face detection modules.

Main responsibilities:

- initialize MediaPipe;
- detect facial landmarks;
- return landmark coordinates.

---

## renderers/

Responsible for drawing accessories.

Functions:

- resize accessories;
- rotate images;
- alpha blending;
- overlay on camera frame.

---

## managers/

Manages application resources.

Examples:

- AccessoryManager
- CameraManager

Responsibilities:

- load accessories;
- cache PNG images;
- switch accessories;
- release resources.

---

## utils/

Helper functions.

Examples:

- file operations;
- image utilities;
- logging;
- path handling.

---

## assets/

Contains static resources.

```
assets/
├── accessories/
├── icons/
└── images/
```

---

## tests/

Contains unit and integration tests.

Examples:

- detector tests;
- renderer tests;
- manager tests;
- application tests.

---

# 5. Development Guide

## Environment Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python main.py
```

---

## Running Unit Tests

```bash
python -m unittest discover tests
```

---

## Building the Executable

```bash
pyinstaller VirtualTryOn.spec
```

The executable will be generated in:

```
dist/
```

---

## Coding Style

Developers should follow:

- PEP 8
- descriptive variable names;
- modular architecture;
- docstrings for public classes and methods;
- logging instead of print().

---

## Adding New Accessories

1. Open:

```
assets/accessories/
```

2. Create or select a category.

3. Add PNG files with an alpha channel.

Example:

```
glasses_21.png
```

The application will detect the new accessory automatically.

---

## Versioning

Project version:

```
v1.0
```

Future releases should follow Semantic Versioning:

```
Major.Minor.Patch
```

Examples:

```
1.0
1.1
2.0
```

---

# Developer Notes

Before publishing a new release:

- run all unit tests;
- verify application startup;
- test camera functionality;
- verify accessory rendering;
- build the executable using PyInstaller;
- update the version number;
- update the documentation.

---

**Virtual Try-On**

Developer Documentation

Version 1.0