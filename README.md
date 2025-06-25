# 🛠️ Structured Data Converter with XSLT

This project demonstrates structured data transformation and stylesheet engineering using **Python** and **XSLT**. It converts between formats like XML, JSON, and CSV, while showcasing how XSLT can transform structured XML into clean HTML for display or documentation.

Inspired by Comply365's work in managing, rendering, and transforming structured content in regulated industries.

---

## 🚀 Features

- ✅ Convert XML ➝ HTML using `XSLT`
- ✅ Convert JSON ➝ XML and CSV ➝ XML using Python
- ✅ Validate XML against XSD Schema
- ✅ Preview raw and transformed outputs
- ✅ Command-line interface for automation
- 🔄 Optional Flask-based web viewer

---

## 📦 Tech Stack

- **Python 3.11+**
- `lxml` for XML/XSLT/XPath processing
- `xmlschema` for XML validation
- `csv`, `json` (native Python)
- [Optional] Flask for demo interface

---

## 📂 Examples

### ✨ XML ➝ HTML (via XSLT)

**input.xml**:
```xml
<flight>
  <number>AA123</number>
  <origin>PHX</origin>
  <destination>JFK</destination>
</flight>
