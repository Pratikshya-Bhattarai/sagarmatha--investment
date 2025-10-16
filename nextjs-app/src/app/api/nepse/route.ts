import { NextRequest, NextResponse } from 'next/server'
import { getFallbackNEPSEData } from '@/lib/nepse-data'

export async function GET(request: NextRequest) {
  try {
    console.log('NEPSE API called')
    
    // Check if Django backend is available
    const djangoApiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1'
    
    try {
      // Try to fetch from Django backend
      const response = await fetch(`${djangoApiUrl}/overview/overview/`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        // Add timeout
        signal: AbortSignal.timeout(5000),
      })

      if (response.ok) {
        const data = await response.json()
        console.log('Successfully fetched data from Django backend')
        return NextResponse.json(data)
      }
    } catch (djangoError) {
      console.log('Django backend not available, using fallback data:', djangoError)
    }

    // Always use fallback data for now to ensure it works
    console.log('Using fallback NEPSE data')
    const fallbackData = getFallbackNEPSEData()
    return NextResponse.json(fallbackData)
  } catch (error) {
    console.error('Error fetching NEPSE data:', error)
    // Return fallback data on error
    const fallbackData = getFallbackNEPSEData()
    return NextResponse.json(fallbackData)
  }
}

