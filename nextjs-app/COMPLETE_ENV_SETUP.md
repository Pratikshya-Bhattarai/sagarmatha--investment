# Complete Environment Variables Setup for Next.js

## Next.js .env.local file

Create a file named `.env.local` in the `nextjs-app` directory with this exact content:

```bash
# Supabase Configuration
NEXT_PUBLIC_SUPABASE_URL=https://afneskhznrmtouqgrbla.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFmbmVza2h6bnJtdG91cWdyYmxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4NTIyOTIsImV4cCI6MjA3NTQyODI5Mn0.8ipDAk5FuyyiRG_OkyQTtFOisOdyy9vPhx1cLPGQzdw

# Backend API Configuration
NEXT_PUBLIC_API_URL=https://pratikshyab.pythonanywhere.com/api/v1
BACKEND_API_URL=https://pratikshyab.pythonanywhere.com/api/v1

# Kaggle API
KAGGLE_USERNAME=pratikshya7890wru
KAGGLE_KEY=9527a67925d40691ab03fe46430595e0

# Google Analytics (Optional - add your ID if you have one)
NEXT_PUBLIC_GA_MEASUREMENT_ID=

# Development Configuration
NODE_ENV=development
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

## How to Create the File

### Option 1: Using Command Line
```bash
cd nextjs-app
echo "# Supabase Configuration
NEXT_PUBLIC_SUPABASE_URL=https://afneskhznrmtouqgrbla.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFmbmVza2h6bnJtdG91cWdyYmxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4NTIyOTIsImV4cCI6MjA3NTQyODI5Mn0.8ipDAk5FuyyiRG_OkyQTtFOisOdyy9vPhx1cLPGQzdw

# Backend API Configuration
NEXT_PUBLIC_API_URL=https://pratikshyab.pythonanywhere.com/api/v1
BACKEND_API_URL=https://pratikshyab.pythonanywhere.com/api/v1

# Kaggle API
KAGGLE_USERNAME=pratikshya7890wru
KAGGLE_KEY=9527a67925d40691ab03fe46430595e0

# Development Configuration
NODE_ENV=development
NEXT_PUBLIC_APP_URL=http://localhost:3000" > .env.local
```

### Option 2: Using Notepad
```bash
cd nextjs-app
notepad .env.local
```
Then paste the content above.

## Vercel Environment Variables (for Production)

Add these in your Vercel project (Settings → Environment Variables):

| Variable Name | Value |
|---------------|-------|
| `NEXT_PUBLIC_SUPABASE_URL` | `https://afneskhznrmtouqgrbla.supabase.co` |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFmbmVza2h6bnJtdG91cWdyYmxhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4NTIyOTIsImV4cCI6MjA3NTQyODI5Mn0.8ipDAk5FuyyiRG_OkyQTtFOisOdyy9vPhx1cLPGQzdw` |
| `NEXT_PUBLIC_API_URL` | `https://pratikshyab.pythonanywhere.com/api/v1` |
| `BACKEND_API_URL` | `https://pratikshyab.pythonanywhere.com/api/v1` |
| `KAGGLE_USERNAME` | `pratikshya7890wru` |
| `KAGGLE_KEY` | `9527a67925d40691ab03fe46430595e0` |
| `NODE_ENV` | `production` |
| `NEXT_PUBLIC_APP_URL` | `https://sagarmatha-investments.vercel.app` |

## After Setting Up

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Run development server:**
   ```bash
   npm run dev
   ```

3. **Visit http://localhost:3000**

4. **Test Supabase connection** by checking if NEPSE data loads correctly

