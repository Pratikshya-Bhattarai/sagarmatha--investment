# 🚀 Complete Guide: Upload Django Backend to PythonAnywhere

## Step 1: Create Directory Structure on PythonAnywhere

Run these commands in your PythonAnywhere console:

```bash
# Navigate to your home directory
cd /home/pratikshyab

# Create the main project directory
mkdir -p sagarmatha-investments/django-backend

# Create subdirectories
mkdir -p sagarmatha-investments/django-backend/logs
mkdir -p sagarmatha-investments/django-backend/staticfiles
mkdir -p sagarmatha-investments/django-backend/media
mkdir -p sagarmatha-investments/django-backend/sagarmatha_backend
mkdir -p sagarmatha-investments/django-backend/nepse
mkdir -p sagarmatha-investments/django-backend/nepse/management/commands
mkdir -p sagarmatha-investments/django-backend/nepse/migrations

# Navigate to the Django backend directory
cd sagarmatha-investments/django-backend
```

## Step 2: Upload Your Django Files

### Option A: Using PythonAnywhere File Manager (Easiest)

1. Go to **Files** tab in PythonAnywhere
2. Navigate to `/home/pratikshyab/sagarmatha-investments/django-backend/`
3. Upload these files one by one:
   - `manage.py`
   - `requirements-pythonanywhere.txt`
   - `wsgi.py`
   - `wsgi_production.py`
   - All files from `sagarmatha_backend/` directory
   - All files from `nepse/` directory

### Option B: Using Git (If your code is on GitHub)

```bash
# Navigate to your home directory
cd /home/pratikshyab

# Clone your repository
git clone https://github.com/your-username/sagarmatha-investments.git

# Copy Django backend files
cp -r sagarmatha-investments/django-backend/* /home/pratikshyab/sagarmatha-investments/django-backend/
```

### Option C: Using SCP/SFTP (Advanced)

```bash
# From your local machine, upload files
scp -r django-backend/* pratikshyab@ssh.pythonanywhere.com:/home/pratikshyab/sagarmatha-investments/django-backend/
```

## Step 3: Set Up Virtual Environment

```bash
# Navigate to Django backend directory
cd /home/pratikshyab/sagarmatha-investments/django-backend

# Create virtual environment
python3.10 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements-pythonanywhere.txt
```

## Step 4: Configure Environment Variables

```bash
# Create .env file
nano .env

# Add these variables (replace with your actual values):
SECRET_KEY=your-very-secure-secret-key-here
DEBUG=False
SUPABASE_DB_NAME=postgres
SUPABASE_DB_USER=postgres
SUPABASE_DB_PASSWORD=your-supabase-password
SUPABASE_DB_HOST=db.your-project-ref.supabase.co
SUPABASE_DB_PORT=5432
KAGGLE_USERNAME=your-kaggle-username
KAGGLE_KEY=your-kaggle-api-key
```

## Step 5: Run Database Migrations

```bash
# Make sure you're in the Django backend directory
cd /home/pratikshyab/sagarmatha-investments/django-backend

# Activate virtual environment
source venv/bin/activate

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

## Step 6: Collect Static Files

```bash
# Collect static files
python manage.py collectstatic --noinput
```

## Step 7: Configure Web App

1. Go to **Web** tab in PythonAnywhere
2. Click **Add a new web app** or edit existing one
3. Choose **Manual configuration**
4. Select **Python 3.10**
5. Set these paths:
   - **Source code**: `/home/pratikshyab/sagarmatha-investments/django-backend`
   - **Working directory**: `/home/pratikshyab/sagarmatha-investments/django-backend`
   - **WSGI file**: `/home/pratikshyab/sagarmatha-investments/django-backend/wsgi.py`

## Step 8: Configure Static Files

In the **Web** tab, scroll to **Static files** and add:
- **URL**: `/static/`
- **Directory**: `/home/pratikshyab/sagarmatha-investments/django-backend/staticfiles/`
- **URL**: `/media/`
- **Directory**: `/home/pratikshyab/sagarmatha-investments/django-backend/media/`

## Step 9: Test Your Backend

```bash
# Test your API endpoints
curl https://pratikshyab.pythonanywhere.com/api/v1/
curl https://pratikshyab.pythonanywhere.com/api/v1/nepse/
```

## Step 10: Load Sample Data (Optional)

```bash
# Load sample NEPSE data
python manage.py update_nepse_data --type all --source live
```

## Troubleshooting

### If you get "No such file or directory" errors:

1. **Check if files exist:**
   ```bash
   ls -la /home/pratikshyab/sagarmatha-investments/django-backend/
   ```

2. **Check if manage.py exists:**
   ```bash
   ls -la /home/pratikshyab/sagarmatha-investments/django-backend/manage.py
   ```

3. **Check virtual environment:**
   ```bash
   ls -la /home/pratikshyab/sagarmatha-investments/django-backend/venv/
   ```

### If you get import errors:

1. **Check if virtual environment is activated:**
   ```bash
   which python
   ```

2. **Reinstall requirements:**
   ```bash
   pip install -r requirements-pythonanywhere.txt
   ```

### If you get database errors:

1. **Check environment variables:**
   ```bash
   cat .env
   ```

2. **Test database connection:**
   ```bash
   python manage.py shell
   >>> from django.db import connection
   >>> connection.ensure_connection()
   ```

## Quick Setup Script

If you want to automate the setup, run this script:

```bash
# Download and run the setup script
curl -O https://raw.githubusercontent.com/your-repo/sagarmatha-investments/main/django-backend/setup_pythonanywhere_complete.py
python setup_pythonanywhere_complete.py
```

## Final Verification

After setup, test these endpoints:

- `https://pratikshyab.pythonanywhere.com/` - Main page
- `https://pratikshyab.pythonanywhere.com/api/v1/` - API root
- `https://pratikshyab.pythonanywhere.com/admin/` - Admin panel
- `https://pratikshyab.pythonanywhere.com/api/v1/nepse/` - NEPSE data

Your backend should now be working on PythonAnywhere! 🎉

