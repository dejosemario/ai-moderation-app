"""
List Available Gemini Models
Run this to see which models you can use
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment
load_dotenv()

# Configure API
api_key = os.getenv('GOOGLE_GEMINI_KEY')
if not api_key:
    print("❌ GOOGLE_GEMINI_KEY not set")
    exit(1)

genai.configure(api_key=api_key)

print("=" * 70)
print("🔍 Available Gemini Models")
print("=" * 70)

try:
    models = genai.list_models()
    
    print("\n✅ Models that support 'generateContent':\n")
    
    for model in models:
        # Check if model supports generateContent
        if 'generateContent' in model.supported_generation_methods:
            print(f"📌 {model.name}")
            print(f"   Display Name: {model.display_name}")
            print(f"   Description: {model.description}")
            print(f"   Max Tokens: {model.input_token_limit if hasattr(model, 'input_token_limit') else 'N/A'}")
            print()
    
    print("=" * 70)
    print("💡 To use a model, copy the name after 'models/'")
    print("   Example: models/gemini-pro → use 'gemini-pro'")
    print("=" * 70)
    
except Exception as e:
    print(f"❌ Error listing models: {str(e)}")
    print("\nThis might be due to:")
    print("  - Invalid API key")
    print("  - Network issues")
    print("  - API changes")