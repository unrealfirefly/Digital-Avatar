-----

# Digital Avatar: Autonomous Excel MVP (PAE)

**Author:** Alexander Chermashentsev (GitHub: unrealfirefly)  
**License:** MIT (free for non-commercial use: personal projects, open-source, non-profits, research).  


-----

## 🌟 Why Digital Avatar?

Digital Avatar uses **PAE (Pattern Analysis & Emulation)** to autonomously interact with desktop applications. This means it works **fully offline, with no external APIs required.**

The current MVP (Minimum Viable Product) focuses on **Excel automation**.

**For Businesses:** This technology allows you to automate Excel reports and workflows offline without APIs. Contact me at diktofonchik@gmail.com to discuss custom solutions.

**Example:** The script autonomously opens Excel via Spotlight, reads the data from cell **B5** of the `test.xlsx` file, and outputs the result to the Terminal. This validates PAE’s ability to read, analyze, and act on local data without user intervention.

-----

## 🛠️ Tech Stack (Zero-Budget Project)

I'm not a programmer, just a guy with a vision for autonomous AI, building this with zero budget. Join me to make it real!

  - **Python**: Core language.
  - **PAE**: The **Proprietary PAE core** is being developed locally. The open source components use **PyAutoGUI** (for GUI emulation) and are preparing to integrate **OpenCV** (for visual element detection).
  - **Excel Handling**: **openpyxl** for fast reading of Excel files.
  - **Platform**: macOS (MacBook Air M1).
  - **Requirements**: Mac with 8GB RAM, 5GB disk space. Note: M1 performance may be slow with large Excel files (\~2–5s latency). Consider using DeepSeek-Coder:1b for better performance.

-----

## 🚀 Start in 5 Minutes (No Coding Required)

1.  Download the ZIP file of the project from GitHub.
2.  Create a `test.xlsx` file (e.g., cell B5 contains "Sample Data").
3.  Unzip the project and open your Terminal in the root folder.
4.  Run the Excel analyzer script:
    ```bash
    python scripts/excel_analyzer.py --file test.xlsx
    ```
5.  Check the Terminal output for the cell B5 results.

-----

## 🤝 Help Us

Your contribution will help us build cloud-independent AI that can rival Siri and Alexa.

**Contributors can help by focusing on these areas:**

  * Testing Excel scripts on various Mac/Windows setups.
  * Optimizing `openpyxl` operations on the M1 chip for faster parsing.
  * Adding support for other office suites (e.g., Google Sheets or LibreOffice).
  * Reporting issues and suggesting additional MVP features via GitHub Issues.

**Why Join?** You'll learn OpenCV and Pandas for automation, build API-free AI with a zero-budget team, and help shape the future of autonomous applications.

-----

## 📋 Project Structure & License

| File / Folder | Purpose |
| :--- | :--- |
| `scripts/excel_analyzer.py` | Core script for Excel automation. |
| `test.xlsx` | Sample Excel file (e.g., cell B5 with "Sample Data"). |
| `LICENSE` | MIT with a non-commercial clause. |

**License:** MIT License (free for personal projects, non-profits, and research).

-----

**Join the zero-budget revolution of autonomous AI!**
