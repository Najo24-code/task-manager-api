# task-manager-api

API REST de gestión de tareas con autenticación JWT, CRUD completo y SQLite

![Python](https://img.shields.io/badge/-Python-blue) ![FastAPI](https://img.shields.io/badge/-FastAPI-blue) ![SQLite](https://img.shields.io/badge/-SQLite-blue)

## 🚀 Features

- API REST completa
- Autenticación JWT
- Base de datos SQLite

## 📦 Instalación
```bash
git clone https://github.com/Najo24-code/task-manager-api.git
cd task-manager-api
pip install -r requirements.txt
```

## 🔧 Uso
```bash
uvicorn main:app --reload
```

API disponible en: `http://localhost:8000/docs`

## 📁 Estructura
```
task-manager-api/
├── main.py          # Entry point
├── models.py        # Modelos de datos
├── database.py      # Conexión DB
├── auth.py          # Autenticación
└── requirements.txt
```

## 📝 License

MIT © 2026 Najo24-code
