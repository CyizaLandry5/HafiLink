# HafiLink - Local File Transfer (PC ↔ Phone) over Wi‑Fi

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Offline](https://img.shields.io/badge/Offline-Local%20LAN%20Only-success)

**HafiLink** is a simple, dependency‑free Python project that allows fast file sharing between nearby devices on the same Wi‑Fi or hotspot network - no internet, no cloud, no extra software.

**Name meaning:** *Hafi* (Kinyarwanda) = **near** → **HafiLink = “connect devices that are near.”**

---

## Features

* Download: PC ➝ Phone
* Upload: Phone ➝ PC
* Works fully offline
* No external libraries

---

## Requirements

* Python **3.10+**
* Phone & PC connected to the **same network**

---

## Step 1 - Find your PC IP (Windows)

Open Command Prompt and run:

```
ipconfig
```

Look for a line like:

```
IPv4 Address . . . . . : 192.168.x.x
```

That is your PC’s address.

---

## Step 2 - Download Mode (PC ➝ Phone)

Start the download server in the folder you want to share:

```
python -m http.server 5555 --bind 0.0.0.0
```

On your phone browser open:

```
http://<PC_IP>:5555
```

You can now browse and download files from the PC.

---

## Step 3 - Upload Mode (Phone ➝ PC)

Run the upload server:

```
python upload_server.py
```

On your phone browser open:

```
http://<PC_IP>:5555
```

Choose a file and upload it.

Uploaded files will appear in:

```
uploads/
```

---

## Security Notice

Use HafiLink only on **private local networks**. Always start the server inside a folder that contains only files you want to share.

---

## Made By

**MPAYIMANA CYIZA Landry** - [https://cyizalandry.com](https://cyizalandry.com)

---

## Li

MIT License
