# Virtual Try-On User Guide

**Project:** Virtual Try-On

**Version:** 1.0

**Author:** Vitaly Semchyshyn

---

# Table of Contents

1. Installation Guide
2. User Manual
3. Keyboard Shortcuts
4. User Interface Description
5. System Requirements

---

# 1. Installation Guide

## 1.1 System Preparation

Before launching the application, ensure that your computer meets the minimum system requirements.

A webcam is required for accessory detection and rendering.

---

## 1.2 Extracting the Release Package

Extract the release archive to any folder.

Example:

```
Virtual Try-On/
│
├── Virtual Try-On.exe
├── assets/
├── README.md
└── User_Guide.md
```

Do not remove or rename the **assets** directory.

---

## 1.3 Launching the Application

Double-click:

```
Virtual Try-On.exe
```

No Python installation is required.

---

## 1.4 Camera Permission

When the application starts, allow access to the webcam if Windows requests permission.

---

## 1.5 Troubleshooting

### Camera is not detected

- Make sure the webcam is connected.
- Close other applications using the camera.
- Restart the application.

---

### Accessories are missing

Verify that the following directory exists:

```
assets/accessories/
```

---

### Application does not start

Try running the application as Administrator.

If Windows Defender blocks the application, allow it manually.

---

# 2. User Manual

## Starting the Application

Launch:

```
Virtual Try-On.exe
```

The camera preview will appear automatically.

---

## Selecting an Accessory Category

Choose one of the available categories:

- Glasses
- Hats
- Masks

---

## Switching Accessories

Use the Previous and Next buttons or keyboard shortcuts to browse accessories.

---

## Camera Preview

The live webcam image is displayed in the center of the application window.

Detected accessories are rendered in real time.

---

## Taking Screenshots

Press the Screenshot button.

Captured images are saved to:

```
screenshots/
```

---

## Recording Video

Press the Record button.

Recorded videos are saved to:

```
recordings/
```

Press the button again to stop recording.

---

## Closing the Application

Close the window or press **Esc**.

The camera will be released automatically.

---

# 3. Keyboard Shortcuts

| Key | Action |
|------|--------|
| ← | Previous accessory |
| → | Next accessory |
| Space | Take screenshot |
| R | Start / Stop recording |
| Esc | Exit application |

---

# 4. User Interface Description

The application consists of the following components.

## Main Window

Displays all application controls.

---

## Camera Preview

Shows the live webcam stream.

---

## Accessory Category Selector

Allows choosing the accessory type.

---

## Navigation Buttons

Switch between available accessories.

---

## Screenshot Button

Captures the current frame.

---

## Record Button

Starts or stops video recording.

---

## Status Bar

Displays application status messages.

---

## Dialog Windows

Used for warnings and error notifications.

---

# 5. System Requirements

## Minimum Requirements

- Windows 10 (64-bit)
- Dual-Core Processor
- 4 GB RAM
- Webcam
- 500 MB free disk space

---

## Recommended Requirements

- Windows 11 (64-bit)
- Intel Core i5 / AMD Ryzen 5
- 8 GB RAM
- HD Webcam
- SSD
- 1 GB free disk space

---

# Support

If problems occur, verify that:

- the **assets** folder exists;
- the webcam is connected;
- the application has permission to access the camera;
- all release files are located in the same directory.

---

**Virtual Try-On**

Version 1.0