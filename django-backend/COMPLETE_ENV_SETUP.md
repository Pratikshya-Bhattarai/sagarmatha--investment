# Complete Environment Variables Setup

## Django Backend .env file

Create a file named `.env` in the `django-backend` directory with this exact content:

```bash
# Django Configuration
SECRET_KEY=TLa4E6ko5OUnW8ea1Tbwuh3vIh7L4kgvSoE_rgLe0wRoJJ2yDyLyB0uj018RIPP9XBE
DEBUG=False

# Database Configuration (Supabase)
SUPABASE_DB_NAME=postgres
SUPABASE_DB_USER=postgres
SUPABASE_DB_PASSWORD=*$VRb6QyzCy4gHC
SUPABASE_DB_HOST=db.afneskhznrmtouqgrbla.supabase.co
SUPABASE_DB_PORT=5432

# Supabase API Configuration
NEXT_PUBLIC_SUPABASE_URL=https://afneskhznrmtouqgrbla.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFmbmVza2h6bnJtdG91cWdyYmxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4NTIyOTIsImV4cCI6MjA3NTQyODI5Mn0.8ipDAk5FuyyiRG_OkyQTtFOisOdyy9vPhx1cLPGQzdw

# Kaggle API
KAGGLE_USERNAME=pratikshya7890wru
KAGGLE_KEY=9527a67925d40691ab03fe46430595e0

# Redis (Optional)
REDIS_URL=redis://localhost:6379/0
```

## How to Create the File

### Option 1: Using Command Line
```bash
cd django-backend
echo "# Django Configuration
SECRET_KEY=TLa4E6ko5OUnW8ea1Tbwuh3vIh7L4kgvSoE_rgLe0wRoJJ2yDyLyB0uj018RIPP9XBE
DEBUG=False

# Database Configuration (Supabase)
SUPABASE_DB_NAME=postgres
SUPABASE_DB_USER=postgres
SUPABASE_DB_PASSWORD=*$VRb6QyzCy4gHC
SUPABASE_DB_HOST=db.afneskhznrmtouqgrbla.supabase.co
SUPABASE_DB_PORT=5432

# Supabase API Configuration
NEXT_PUBLIC_SUPABASE_URL=https://afneskhznrmtouqgrbla.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFmbmVza2h6bnJtdG91cWdyYmxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4NTIyOTIsImV4cCI6MjA3NTQyODI5Mn0.8ipDAk5FuyyiRG_OkyQTtFOisOdyy9vPhx1cLPGQzdw

# Kaggle API
KAGGLE_USERNAME=pratikshya7890wru
KAGGLE_KEY=9527a67925d40691ab03fe46430595e0

# Redis (Optional)
REDIS_URL=redis://localhost:6379/0" > .env
```

### Option 2: Using Notepad
```bash
cd django-backend
notepad .env
```
Then paste the content above.

## PythonAnywhere Environment Variables

Add these in your PythonAnywhere web app (Web tab → Environment variables):

| Variable Name | Value |
|---------------|-------|
| `SECRET_KEY` | `TLa4E6ko5OUnW8ea1Tbwuh3vIh7L4kgvSoE_rgLe0wRoJJ2yDyLyB0uj018RIPP9XBE` |
| `DEBUG` | `False` |
| `SUPABASE_DB_NAME` | `postgres` |
| `SUPABASE_DB_USER` | `postgres` |
| `SUPABASE_DB_PASSWORD` | `*$VRb6QyzCy4gHC` |
| `SUPABASE_DB_HOST` | `db.afneskhznrmtouqgrbla.supabase.co` |
| `SUPABASE_DB_PORT` | `5432` |
| `NEXT_PUBLIC_SUPABASE_URL` | `https://afneskhznrmtouqgrbla.supabase.co` |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFmbmVza2h6bnJtdG91cWdyYmxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4NTIyOTIsImV4cCI6MjA3NTQyODI5Mn0.8ipDAk5FuyyiRG_OkyQTtFOisOdyy9vPhx1cLPGQzdw` |
| `KAGGLE_USERNAME` | `pratikshya7890wru` |
| `KAGGLE_KEY` | `9527a67925d40691ab03fe46430595e0` |

## After Setting Up

1. **Reload your PythonAnywhere web app**
2. **Test database connection:**
   ```bash
   cd /home/pratikshyab/sagarmatha-investments/django-backend
   python manage.py migrate
   ```
3. **Check for errors in the error log**

