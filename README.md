# LearnHub

An e-learning platform built with Django.

## Local setup — Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.

## Planned features

- Course catalog
- Lessons
- Learner accounts
- Enrollment and lesson progress