#!/usr/bin/env python
"""
Quick fix script for database issues on PythonAnywhere
This script will create the necessary database tables and load sample data
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_database():
    """Setup database tables and load sample data"""
    print("🔧 Fixing database issues...")
    
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sagarmatha_backend.settings_pythonanywhere')
    django.setup()
    
    print("✅ Django setup complete")
    
    # Create migrations
    print("📝 Creating migrations...")
    try:
        execute_from_command_line(['manage.py', 'makemigrations'])
        print("✅ Migrations created successfully")
    except Exception as e:
        print(f"❌ Migration creation failed: {e}")
        return False
    
    # Apply migrations
    print("🗄️ Applying migrations...")
    try:
        execute_from_command_line(['manage.py', 'migrate'])
        print("✅ Migrations applied successfully")
    except Exception as e:
        print(f"❌ Migration application failed: {e}")
        return False
    
    # Create superuser (optional)
    print("👤 Creating superuser...")
    try:
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("✅ Superuser created (username: admin, password: admin123)")
        else:
            print("✅ Superuser already exists")
    except Exception as e:
        print(f"⚠️ Superuser creation failed: {e}")
    
    # Load sample data
    print("📊 Loading sample data...")
    try:
        execute_from_command_line(['manage.py', 'update_nepse_data', '--type', 'all', '--source', 'live'])
        print("✅ Sample data loaded successfully")
    except Exception as e:
        print(f"⚠️ Sample data loading failed: {e}")
        print("This is optional - your API will still work")
    
    print("\n🎉 Database setup complete!")
    print("\n📋 Next steps:")
    print("1. Test your API: curl https://pratikshyab.pythonanywhere.com/api/v1/")
    print("2. Check admin panel: https://pratikshyab.pythonanywhere.com/admin/")
    print("3. Test NEPSE data: curl https://pratikshyab.pythonanywhere.com/api/v1/nepse/")
    
    return True

if __name__ == "__main__":
    success = setup_database()
    if success:
        print("\n✅ Database fix completed successfully!")
    else:
        print("\n❌ Database fix failed. Please check the errors above.")
        sys.exit(1)

