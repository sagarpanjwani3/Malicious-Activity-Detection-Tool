# Malicious-Activity-Detection-Tool

A Python-based digital forensics utility designed to automate the extraction of potential persistence mechanisms from Windows Registry hives and generate structured PDF reports for investigators.

## 🔍 Features
* **Hive Parsing:** Programmatically accesses `NTUSER.DAT` hives using the `regipy` framework.
* **Auto-Detection:** Targets common persistence locations such as `\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`.
* **PDF Generation:** Automates the creation of a forensic report including raw data and expert analysis using `ReportLab`.
* **Extensible:** Easily adaptable to scan for other forensic artifacts (UserAssist, ShellBags, etc.).

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** * `regipy`: For registry hive manipulation.
    * `reportlab`: For PDF document generation.

## 🚀 Getting Started

### Prerequisites
You will need a copy of a Windows Registry hive (e.g., `NTUSER.DAT`). Note: To analyze a live system's hive, you must run the tool with administrative privileges or use a tool to bypass file locks.

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/sagarpanjwani3/-Malicious-Activity-Detection-Tool.git)
