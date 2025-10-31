"""
Command-Line Interface for AI Moderation App
Interactive CLI for chatting with Gemini AI with content moderation
"""

import os
from dotenv import load_dotenv
from ai_client import AIClient
from moderation import ContentModerator


def main():
    """Main CLI application loop."""
    
    # Load environment variables
    load_dotenv()
    
    # Print header
    print("=" * 60)
    print("🤖 AI Moderation Chat - Gemini Edition")
    print("=" * 60)
    print("Type 'quit' or 'exit' to end the conversation")
    print("Type 'help' for available commands")
    print("=" * 60)
    
    try:
        # Initialize AI client and moderator
        ai_client = AIClient()
        moderator = ContentModerator()
        
        print("\n✅ System ready! Start chatting...\n")
        
        # Main conversation loop
        while True:
            # Get user input
            user_input = input("\n💬 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Goodbye! Thanks for chatting!")
                break
            
            # Check for help command
            if user_input.lower() == 'help':
                print_help()
                continue
            
            # Check for keywords command
            if user_input.lower() == 'keywords':
                print_keywords(moderator)
                continue
            
            # Skip empty input
            if not user_input:
                print("⚠️  Please enter a message.")
                continue
            
            # Moderate input
            is_approved, moderation_message = moderator.moderate_input(user_input)
            
            if not is_approved:
                print(f"\n{moderation_message}")
                continue
            
            # Get AI response
            print("\n🤖 AI: ", end="", flush=True)
            ai_response = ai_client.chat(user_input)
            
            # Moderate output
            moderated_response = moderator.moderate_output(ai_response)
            
            # Print response
            print(moderated_response)
            
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! (Interrupted)")
    except ValueError as e:
        print(f"\n❌ Configuration Error: {str(e)}")
        print("\nPlease make sure:")
        print("1. You have a .env file")
        print("2. GOOGLE_GEMINI_KEY is set in .env")
        print("3. Your API key is valid")
    except Exception as e:
        print(f"\n❌ Unexpected Error: {str(e)}")
        print("Please check your configuration and try again.")


def print_help():
    """Print help information."""
    print("\n" + "=" * 60)
    print("📚 Available Commands:")
    print("=" * 60)
    print("  quit/exit/q  - Exit the application")
    print("  help         - Show this help message")
    print("  keywords     - Show list of blocked keywords")
    print("=" * 60)


def print_keywords(moderator: ContentModerator):
    """Print list of blocked keywords."""
    keywords = moderator.get_blocked_keywords()
    print("\n" + "=" * 60)
    print("🚫 Blocked Keywords:")
    print("=" * 60)
    for keyword in keywords:
        print(f"  - {keyword}")
    print("=" * 60)
    print(f"Total: {len(keywords)} keywords")


if __name__ == "__main__":
    main()