# 🔧 Backend Troubleshooting Checklist for PythonAnywhere

## Quick Diagnostic Commands

### 1. **Basic Connectivity**
```bash
# Test if your domain is accessible
curl -I https://pratikshyab.pythonanywhere.com/

# Test API root
curl https://pratikshyab.pythonanywhere.com/api/v1/
```

### 2. **Check Web App Status**
1. Go to PythonAnywhere **Web** tab
2. Check if your web app is **enabled**
3. Look for any error messages in red

### 3. **Check Logs**
```bash
# Django application logs
tail -50 /home/pratikshyab/sagarmatha-investments/django-backend/logs/django.log

# PythonAnywhere error logs
tail -50 /var/log/pratikshyab.pythonanywhere.com.error.log

# Access logs
tail -50 /var/log/pratikshyab.pythonanywhere.com.access.log
```

### 4. **Database Issues**
```bash
# Test database connection
cd /home/pratikshyab/sagarmatha-investments/django-backend
source venv/bin/activate
python manage.py dbshell

# Check environment variables
python -c "from decouple import config; print('DB Host:', config('SUPABASE_DB_HOST', default='Not set'))"
```

### 5. **Common Error Solutions**

#### **500 Internal Server Error**
- Check error logs: `tail -50 /var/log/pratikshyab.pythonanywhere.com.error.log`
- Restart web app: `touch /var/www/pratikshyab_pythonanywhere_com_wsgi.py`
- Check if all dependencies are installed: `pip list`

#### **Database Connection Error**
- Verify Supabase credentials in `.env` file
- Check if your IP is whitelisted in Supabase
- Test connection: `python manage.py shell` → `from django.db import connection` → `connection.ensure_connection()`

#### **Static Files Not Loading**
- Recollect static files: `python manage.py collectstatic --noinput`
- Check static files mapping in Web tab
- Verify file permissions: `ls -la staticfiles/`

#### **Import Errors**
- Check virtual environment: `which python`
- Activate venv: `source venv/bin/activate`
- Reinstall requirements: `pip install -r requirements-pythonanywhere.txt`

#### **CORS Issues**
- Check CORS settings in `settings_pythonanywhere.py`
- Add your frontend domain to `CORS_ALLOWED_ORIGINS`
- Test with: `curl -H "Origin: https://your-frontend.com" https://pratikshyab.pythonanywhere.com/api/v1/`

### 6. **Performance Issues**

#### **Slow Response Times**
```bash
# Check memory usage
free -h

# Check running processes
ps aux | grep python

# Test response time
time curl -s https://pratikshyab.pythonanywhere.com/api/v1/
```

#### **High Memory Usage**
- Check for memory leaks in logs
- Restart web app
- Consider upgrading PythonAnywhere plan

### 7. **Environment Variables Check**
```bash
# Check if .env file exists
ls -la .env

# Check environment variables
python -c "
from decouple import config
print('SECRET_KEY:', 'Set' if config('SECRET_KEY', default='') else 'Not set')
print('DEBUG:', config('DEBUG', default='Not set'))
print('DB_HOST:', config('SUPABASE_DB_HOST', default='Not set'))
print('DB_NAME:', config('SUPABASE_DB_NAME', default='Not set'))
"
```

### 8. **API Endpoint Testing**
```bash
# Test all endpoints
curl https://pratikshyab.pythonanywhere.com/api/v1/
curl https://pratikshyab.pythonanywhere.com/api/v1/nepse/
curl https://pratikshyab.pythonanywhere.com/api/v1/nepse/overview/
curl https://pratikshyab.pythonanywhere.com/api/v1/nepse/stocks/
curl https://pratikshyab.pythonanywhere.com/api/v1/nepse/indices/
```

### 9. **Quick Fixes**

#### **Restart Everything**
```bash
# Restart web app
touch /var/www/pratikshyab_pythonanywhere_com_wsgi.py

# Restart console
# (Close and open new console session)
```

#### **Reinstall Dependencies**
```bash
cd /home/pratikshyab/sagarmatha-investments/django-backend
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements-pythonanywhere.txt
```

#### **Reset Database**
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (if needed)
python manage.py createsuperuser
```

### 10. **Emergency Recovery**

#### **If nothing works:**
1. Check PythonAnywhere service status
2. Verify your account is active
3. Check if you've exceeded resource limits
4. Contact PythonAnywhere support

#### **Backup and Restore**
```bash
# Backup current state
cp -r /home/pratikshyab/sagarmatha-investments /home/pratikshyab/backup-$(date +%Y%m%d)

# Restore from Git
cd /home/pratikshyab/sagarmatha-investments
git pull origin main
```

## 🚨 Emergency Contacts

- **PythonAnywhere Support**: https://www.pythonanywhere.com/contact/
- **Supabase Support**: https://supabase.com/support
- **Django Documentation**: https://docs.djangoproject.com/

## 📊 Health Check Script

Run the automated health check:
```bash
cd /home/pratikshyab/sagarmatha-investments/django-backend
source venv/bin/activate
python health_check.py
```

This will give you a comprehensive report of your backend status.

