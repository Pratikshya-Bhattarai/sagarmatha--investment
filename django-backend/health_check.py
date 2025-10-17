#!/usr/bin/env python
"""
Health check script for Sagarmatha Investments Backend
Run this script to verify all components are working correctly
"""

import os
import sys
import django
from django.conf import settings
from django.db import connection
from django.test import RequestFactory
import requests
import json

def check_environment():
    """Check environment variables and configuration"""
    print("🔍 Checking environment...")
    
    required_vars = [
        'SECRET_KEY',
        'SUPABASE_DB_HOST',
        'SUPABASE_DB_NAME',
        'SUPABASE_DB_USER',
        'SUPABASE_DB_PASSWORD'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
        return False
    else:
        print("✅ All required environment variables are set")
        return True

def check_database():
    """Check database connectivity"""
    print("🔍 Checking database connection...")
    
    try:
        connection.ensure_connection()
        print("✅ Database connection successful")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def check_django_setup():
    """Check Django setup and configuration"""
    print("🔍 Checking Django setup...")
    
    try:
        # Check if Django can start
        django.setup()
        
        # Check settings
        print(f"✅ Django version: {django.get_version()}")
        print(f"✅ DEBUG mode: {settings.DEBUG}")
        print(f"✅ Allowed hosts: {settings.ALLOWED_HOSTS}")
        
        return True
    except Exception as e:
        print(f"❌ Django setup failed: {e}")
        return False

def check_api_endpoints():
    """Check if API endpoints are accessible"""
    print("🔍 Checking API endpoints...")
    
    base_url = "https://pratikshyab.pythonanywhere.com"
    endpoints = [
        "/api/v1/",
        "/api/v1/nepse/",
        "/api/v1/nepse/overview/",
        "/api/v1/nepse/stocks/",
        "/api/v1/nepse/indices/",
    ]
    
    working_endpoints = []
    failed_endpoints = []
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=10)
            if response.status_code == 200:
                working_endpoints.append(endpoint)
                print(f"✅ {endpoint} - Status: {response.status_code}")
            else:
                failed_endpoints.append(endpoint)
                print(f"❌ {endpoint} - Status: {response.status_code}")
        except Exception as e:
            failed_endpoints.append(endpoint)
            print(f"❌ {endpoint} - Error: {e}")
    
    if failed_endpoints:
        print(f"❌ Failed endpoints: {', '.join(failed_endpoints)}")
        return False
    else:
        print("✅ All API endpoints are working")
        return True

def check_static_files():
    """Check if static files are properly configured"""
    print("🔍 Checking static files...")
    
    try:
        static_root = settings.STATIC_ROOT
        if os.path.exists(static_root):
            print(f"✅ Static files directory exists: {static_root}")
            return True
        else:
            print(f"❌ Static files directory not found: {static_root}")
            return False
    except Exception as e:
        print(f"❌ Static files check failed: {e}")
        return False

def check_logs():
    """Check if log files are accessible"""
    print("🔍 Checking log files...")
    
    log_file = os.path.join(settings.BASE_DIR, 'logs', 'django.log')
    if os.path.exists(log_file):
        print(f"✅ Log file exists: {log_file}")
        
        # Check recent log entries
        with open(log_file, 'r') as f:
            lines = f.readlines()
            recent_lines = lines[-5:] if len(lines) >= 5 else lines
            print("Recent log entries:")
            for line in recent_lines:
                print(f"  {line.strip()}")
        return True
    else:
        print(f"❌ Log file not found: {log_file}")
        return False

def main():
    """Run all health checks"""
    print("🚀 Starting Sagarmatha Backend Health Check...")
    print("=" * 50)
    
    checks = [
        check_environment,
        check_django_setup,
        check_database,
        check_static_files,
        check_logs,
        check_api_endpoints,
    ]
    
    results = []
    for check in checks:
        try:
            result = check()
            results.append(result)
        except Exception as e:
            print(f"❌ Health check failed: {e}")
            results.append(False)
        print()
    
    # Summary
    print("=" * 50)
    print("📊 Health Check Summary:")
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✅ All checks passed ({passed}/{total})")
        print("🎉 Your backend is working perfectly!")
    else:
        print(f"⚠️  {total - passed} checks failed ({passed}/{total})")
        print("🔧 Please review the failed checks above")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

