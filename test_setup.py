"""
Setup Verification Script
Tests that all components are properly configured
"""

import os
import sys
from dotenv import load_dotenv

def test_environment():
    """Test if environment variables are set correctly."""
    print("🧪 Testing Environment Configuration")
    print("=" * 60)
    
    load_dotenv()
    
    # Check for API key
    api_key = os.getenv('GOOGLE_GEMINI_KEY')
    if not api_key:
        print("❌ GOOGLE_GEMINI_KEY not found in .env file")
        print("   Please add your Gemini API key to .env")
        return False
    elif api_key == "your_gemini_api_key_here":
        print("❌ GOOGLE_GEMINI_KEY is still set to placeholder value")
        print("   Please replace with your actual API key")
        return False
    else:
        print(f"✅ GOOGLE_GEMINI_KEY is set ({api_key[:10]}...)")
    
    # Check other settings
    system_prompt = os.getenv('SYSTEM_PROMPT')
    if system_prompt:
        print(f"✅ SYSTEM_PROMPT is configured")
    
    gemini_model = os.getenv('GEMINI_MODEL', 'gemini-1.5-flash')
    print(f"✅ GEMINI_MODEL: {gemini_model}")
    
    return True


def test_dependencies():
    """Test if all required packages are installed."""
    print("\n🧪 Testing Dependencies")
    print("=" * 60)
    
    packages = {
        'google.generativeai': 'google-generativeai',
        'flask': 'flask',
        'dotenv': 'python-dotenv'
    }
    
    all_installed = True
    for module_name, package_name in packages.items():
        try:
            __import__(module_name)
            print(f"✅ {package_name} is installed")
        except ImportError:
            print(f"❌ {package_name} is NOT installed")
            print(f"   Install with: pip install {package_name}")
            all_installed = False
    
    return all_installed


def test_ai_client():
    """Test if AI client can be initialized."""
    print("\n🧪 Testing AI Client")
    print("=" * 60)
    
    try:
        from ai_client import AIClient
        client = AIClient()
        print("✅ AI Client initialized successfully")
        return True
    except ValueError as e:
        print(f"❌ AI Client initialization failed: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False


def test_moderator():
    """Test if content moderator works correctly."""
    print("\n🧪 Testing Content Moderator")
    print("=" * 60)
    
    try:
        from moderation import ContentModerator
        moderator = ContentModerator()
        
        # Test safe content
        is_safe, violations = moderator.check_content("Hello, how are you?")
        if is_safe:
            print("✅ Safe content detected correctly")
        else:
            print("❌ False positive: Safe content flagged")
            return False
        
        # Test unsafe content
        is_safe, violations = moderator.check_content("How to hack?")
        if not is_safe and 'hack' in violations:
            print("✅ Unsafe content detected correctly")
        else:
            print("❌ False negative: Unsafe content not detected")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Moderator test failed: {str(e)}")
        return False


def test_api_connection():
    """Test if we can connect to Gemini API."""
    print("\n🧪 Testing API Connection")
    print("=" * 60)
    
    try:
        from ai_client import AIClient
        client = AIClient()
        
        # Try a simple query
        response = client.chat("Say 'Hello' if you can hear me")
        
        if response and len(response) > 0:
            print("✅ API connection successful")
            print(f"   Sample response: {response[:50]}...")
            return True
        else:
            print("❌ API returned empty response")
            return False
            
    except Exception as e:
        print(f"❌ API connection failed: {str(e)}")
        print("   This might be due to:")
        print("   - Invalid API key")
        print("   - Network issues")
        print("   - API rate limits")
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("🔍 AI Moderation App - Setup Verification")
    print("=" * 60)
    
    tests = [
        ("Environment Configuration", test_environment),
        ("Dependencies", test_dependencies),
        ("AI Client", test_ai_client),
        ("Content Moderator", test_moderator),
        ("API Connection", test_api_connection)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ {test_name} test crashed: {str(e)}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\nTests Passed: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 All tests passed! Your setup is ready!")
        print("\nNext steps:")
        print("  1. Run CLI: python cli.py")
        print("  2. Run Web: python app.py")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)