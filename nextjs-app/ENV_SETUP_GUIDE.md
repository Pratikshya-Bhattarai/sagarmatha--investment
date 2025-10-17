# Next.js Environment Variables Setup Guide

## Create .env.local file

Create a `.env.local` file in the `nextjs-app` directory with these variables:

```bash
# Supabase Configuration
NEXT_PUBLIC_SUPABASE_URL=https://your-project-ref.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here

# Backend API Configuration
NEXT_PUBLIC_API_URL=https://yourusername.pythonanywhere.com/api/v1
BACKEND_API_URL=https://yourusername.pythonanywhere.com/api/v1

# Kaggle API
KAGGLE_USERNAME=pratikshya7890wru
KAGGLE_KEY=9527a67925d40691ab03fe46430595e0

# Google Analytics (Optional)
NEXT_PUBLIC_GA_MEASUREMENT_ID=your-ga-measurement-id

# Development Configuration
NODE_ENV=development
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

## For Production (Vercel):

```bash
# Supabase Configuration
NEXT_PUBLIC_SUPABASE_URL=https://your-project-ref.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here

# Backend API Configuration
NEXT_PUBLIC_API_URL=https://yourusername.pythonanywhere.com/api/v1
BACKEND_API_URL=https://yourusername.pythonanywhere.com/api/v1

# Kaggle API
KAGGLE_USERNAME=pratikshya7890wru
KAGGLE_KEY=9527a67925d40691ab03fe46430595e0

# Google Analytics (Optional)
NEXT_PUBLIC_GA_MEASUREMENT_ID=your-ga-measurement-id

# Production Configuration
NODE_ENV=production
NEXT_PUBLIC_APP_URL=https://sagarmatha-investments.vercel.app
```

## How to Get Your Supabase Values

1. Go to https://app.supabase.com
2. Select your project: "Sagarmatha-Investment"
3. Go to Settings → API
4. Copy:
   - **Project URL** → Use for `NEXT_PUBLIC_SUPABASE_URL`
   - **Project API keys → anon/public** → Use for `NEXT_PUBLIC_SUPABASE_ANON_KEY`

## Add to Vercel

1. Go to your Vercel project dashboard
2. Settings → Environment Variables
3. Add each variable one by one
4. Select "Production", "Preview", and "Development" for each
5. Save and redeploy your app

## Testing

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Visit http://localhost:3000
```

