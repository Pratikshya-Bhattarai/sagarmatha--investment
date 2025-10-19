# Environment Variables Setup Guide

## Django Backend (.env file)

Create a `.env` file in the `django-backend` directory with these variables:

```bash
# Django Configuration
SECRET_KEY=TLa4E6ko5OUnW8ea1Tbwuh3vIh7L4kgvSoE_rgLe0wRoJJ2yDyLyB0uj018RIPP9XBE
DEBUG=False

# Database Configuration (Supabase)
SUPABASE_DB_NAME=postgres
SUPABASE_DB_USER=postgres
SUPABASE_DB_PASSWORD=*$VRb6QyzCy4gHC
SUPABASE_DB_HOST=db.Sagarmatha-Investment.supabase.co
SUPABASE_DB_PORT=5432

# Supabase API Configuration
NEXT_PUBLIC_SUPABASE_URL=https://your-project-ref.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here

# Kaggle API
KAGGLE_USERNAME=pratikshya7890wru
KAGGLE_KEY=9527a67925d40691ab03fe46430595e0

# Redis (Optional)
REDIS_URL=redis://localhost:6379/0
```

## How to Get Your Supabase Values

1. Go to https://app.supabase.com
2. Select your project: "Sagarmatha-Investment"
3. Go to Settings → API
4. Copy:
   - **Project URL** → Replace `https://your-project-ref.supabase.co`
   - **Project API keys → anon/public** → Replace `your-anon-key-here`

## PythonAnywhere Environment Variables

Add these in your PythonAnywhere web app (Web tab → Environment variables):

| Variable Name | Value |
|---------------|-------|
| `SECRET_KEY` | `TLa4E6ko5OUnW8ea1Tbwuh3vIh7L4kgvSoE_rgLe0wRoJJ2yDyLyB0uj018RIPP9XBE` |
| `DEBUG` | `False` |
| `SUPABASE_DB_NAME` | `postgres` |
| `SUPABASE_DB_USER` | `postgres` |
| `SUPABASE_DB_PASSWORD` | `*$VRb6QyzCy4gHC` |
| `SUPABASE_DB_HOST` | `db.Sagarmatha-Investment.supabase.co` |
| `SUPABASE_DB_PORT` | `5432` |
| `NEXT_PUBLIC_SUPABASE_URL` | Your Supabase URL |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Your Supabase anon key |
| `KAGGLE_USERNAME` | `pratikshya7890wru` |
| `KAGGLE_KEY` | `9527a67925d40691ab03fe46430595e0` |

## Vercel Environment Variables (Next.js Frontend)

Add these in your Vercel project (Settings → Environment Variables):

| Variable Name | Value |
|---------------|-------|
| `NEXT_PUBLIC_SUPABASE_URL` | Your Supabase URL |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Your Supabase anon key |
| `NEXT_PUBLIC_API_URL` | `https://yourusername.pythonanywhere.com/api/v1` |
| `KAGGLE_USERNAME` | `pratikshya7890wru` |
| `KAGGLE_KEY` | `9527a67925d40691ab03fe46430595e0` |

## Testing Your Setup

### Test Django Backend:
```bash
cd django-backend
python manage.py shell
from django.db import connection
connection.ensure_connection()
print("Database connected!")
```

### Test Next.js Frontend:
```bash
cd nextjs-app
npm run dev
# Visit http://localhost:3000
```


