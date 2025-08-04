# Embedding File Search Utility

A powerful and user-friendly tool for searching and ranking files within a specified directory, using both conventional keyword and advanced semantic embedding search (with [Sentence Transformers](https://www.sbert.net/)). Includes a FastAPI web frontend with a clean interface and interactive search experience.

---

## 🚩 Project Overview

This project provides a comprehensive file search utility that can:

- List and sort files in a target directory based on keyword search suitability.
- Perform semantic (embedding-based) search to retrieve relevant files, even when keywords differ.
- Expose a REST API with an HTML frontend for instant and intuitive results.
- Support error handling, environment-based configuration, and extensibility.
- Includes multiprocessing and scoring logic for swift, robust search.

---

## ✨ Features

- **Hybrid Search Modes:** Switch between keyword (exact/partial match) and semantic (embedding-based) search.
- **Configurable Root Directory:** Set the directory to search using the `REPO_PATH` environment variable.
- **Web Interface:** Modern, interactive FastAPI frontend for querying and browsing results, powered by [Jinja2](https://palletsprojects.com/p/jinja/) templates.
- **REST API:** Easily accessible via `/search` and `/advanced_search` endpoints.
- **Error Handling:** Handles unreadable files, missing paths, and permission issues gracefully.
- **Extensible:** Modularized for additional scoring strategies or file types.

---

## 🚀 Quick Start

**1. Clone the Repository**

```bash
git clone https://github.com/Krishnarajan-K/Searching_files.git
cd Searching_files
```

**2. Create and Activate a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Set Environment Variables**

Create a `.env` file with your desired search directory:
```env
REPO_PATH=/absolute/path/to/your/files
```

**5. Run the FastAPI Webserver**

```bash
uvicorn webpage_search.main:app --host 127.0.0.1 --port 8000 --reload
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## ⚙️ Usage

- **Web UI:** Type your query and toggle “Embedding Search” for semantic search. Results are dynamically displayed and scored.
- **API:** Query `/search?query=YOUR_QUERY&embedding=true` for semantic search, or `embedding=false` for keyword.
- **Advanced Search:** `/advanced_search?query=YOUR_QUERY&search_type=combined` supports more options (see API docs).

---

## 🛠️ Contributing

Contributions, bug reports, and feature requests are welcome!
- Fork the repo and create your branch (`git checkout -b my-feature`)
- Make your changes with clear commit messages.
- Ensure code lints and tests pass.
- Submit a Pull Request explaining your improvements.

---

## 🧪 Environment Variables

The primary environment variable required:

| Name      | Description                                        | Example                                  |
|-----------|----------------------------------------------------|------------------------------------------|
| REPO_PATH | Absolute path to the directory to index and search | `/home/user/projects/my-repo`            |

Create a `.env` file in the project root with:

```
REPO_PATH=/path/to/your/search/folder
```

---

## 📸 Screenshots

App Interface:
![Screenshot 1](https://github.com/user-attachments/assets/0219cf1c-7268-4c37-998a-5a52e911477c)
![Screenshot 2](https://github.com/user-attachments/assets/71ba5a2d-7981-4ea8-a187-dbf215b3d1e0)

---

## 📄 License

MIT License © 2025 Krishnarajan-K

---

## 🔗 Links

- [GitHub Repository](https://github.com/Krishnarajan-K/Searching-files.git)
