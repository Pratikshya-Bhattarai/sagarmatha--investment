#!/usr/bin/env python
"""
Complete setup script for PythonAnywhere
This script will create the directory structure and upload all necessary files
"""

import os
import shutil
from pathlib import Path

def create_pythonanywhere_structure():
    """Create the complete directory structure for PythonAnywhere"""
    print("🏔️ Setting up Sagarmatha Backend on PythonAnywhere...")
    
    # Base directory on PythonAnywhere
    base_dir = Path("/home/pratikshyab/sagarmatha-investments/django-backend")
    
    # Create directory structure
    directories = [
        base_dir,
        base_dir / "logs",
        base_dir / "staticfiles",
        base_dir / "media",
        base_dir / "venv",
        base_dir / "sagarmatha_backend",
        base_dir / "nepse",
        base_dir / "nepse" / "management",
        base_dir / "nepse" / "management" / "commands",
        base_dir / "nepse" / "migrations",
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {directory}")
    
    return base_dir

def create_essential_files(base_dir):
    """Create essential Django files"""
    print("📝 Creating essential Django files...")
    
    # Create manage.py
    manage_py_content = '''#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

if __name__ == '__main__':
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sagarmatha_backend.settings_pythonanywhere')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
'''
    
    with open(base_dir / "manage.py", "w") as f:
        f.write(manage_py_content)
    print("✅ Created manage.py")
    
    # Create requirements file
    requirements_content = '''# PythonAnywhere specific requirements
Django==5.0.8
djangorestframework==3.15.2
django-cors-headers==4.3.1
pandas==2.2.2
numpy==1.26.4
requests==2.31.0
python-decouple==3.8
django-filter==24.2
django-extensions==3.2.3
whitenoise==6.6.0
kaggle==1.5.16
beautifulsoup4==4.12.3
lxml==5.1.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
'''
    
    with open(base_dir / "requirements-pythonanywhere.txt", "w") as f:
        f.write(requirements_content)
    print("✅ Created requirements-pythonanywhere.txt")
    
    # Create .env template
    env_template = '''# Django Settings
SECRET_KEY=your-very-secure-secret-key-here
DEBUG=False

# Database Settings (Supabase)
SUPABASE_DB_NAME=postgres
SUPABASE_DB_USER=postgres
SUPABASE_DB_PASSWORD=your-supabase-password
SUPABASE_DB_HOST=db.your-project-ref.supabase.co
SUPABASE_DB_PORT=5432

# Kaggle API
KAGGLE_USERNAME=your-kaggle-username
KAGGLE_KEY=your-kaggle-api-key
'''
    
    with open(base_dir / ".env", "w") as f:
        f.write(env_template)
    print("✅ Created .env template")
    
    # Create WSGI file
    wsgi_content = '''import os
import sys

# Add your project directory to the Python path
path = '/home/pratikshyab/sagarmatha-investments/django-backend'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'sagarmatha_backend.settings_pythonanywhere'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
'''
    
    with open(base_dir / "wsgi.py", "w") as f:
        f.write(wsgi_content)
    print("✅ Created wsgi.py")

def create_django_apps(base_dir):
    """Create Django app files"""
    print("📱 Creating Django app files...")
    
    # Create sagarmatha_backend/__init__.py
    with open(base_dir / "sagarmatha_backend" / "__init__.py", "w") as f:
        f.write("")
    
    # Create nepse/__init__.py
    with open(base_dir / "nepse" / "__init__.py", "w") as f:
        f.write("")
    
    # Create nepse/apps.py
    apps_content = '''from django.apps import AppConfig

class NepseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nepse'
'''
    
    with open(base_dir / "nepse" / "apps.py", "w") as f:
        f.write(apps_content)
    
    print("✅ Created Django app files")

def main():
    """Main setup function"""
    print("🚀 Complete PythonAnywhere Setup for Sagarmatha Backend")
    print("=" * 60)
    
    try:
        # Create directory structure
        base_dir = create_pythonanywhere_structure()
        
        # Create essential files
        create_essential_files(base_dir)
        
        # Create Django apps
        create_django_apps(base_dir)
        
        print("\n🎉 Setup completed successfully!")
        print("\n📋 Next steps:")
        print("1. Upload your actual Django files to the created directories")
        print("2. Set up your environment variables in .env file")
        print("3. Create virtual environment: python3.10 -m venv venv")
        print("4. Activate virtual environment: source venv/bin/activate")
        print("5. Install requirements: pip install -r requirements-pythonanywhere.txt")
        print("6. Run migrations: python manage.py migrate")
        print("7. Configure your web app in PythonAnywhere Web tab")
        
        return True
        
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n✅ PythonAnywhere structure created successfully!")
    else:
        print("\n❌ Setup failed. Please check the errors above.")




