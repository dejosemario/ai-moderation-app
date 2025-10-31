"""
AI Client Module - Google Gemini Integration
Handles API communication with Google's Gemini AI
"""

import os
import google.generativeai as genai
from typing import Optional


class AIClient:
    """Client for interacting with Google Gemini API."""
    
    def __init__(self):
        """Initialize the AI client with API key and system prompt."""
        self.api_key = os.getenv('GOOGLE_GEMINI_KEY')
        
        if not self.api_key:
            raise ValueError("GOOGLE_GEMINI_KEY environment variable not set")
        
        # Configure Gemini API
        genai.configure(api_key=self.api_key)
        
        # Get system prompt from environment or use default
        self.system_prompt = os.getenv('SYSTEM_PROMPT', 
                                       'You are a helpful assistant. Please provide informative and safe responses.')
        
        # Get model name from environment or use default
        # Updated model names for Gemini API
        self.model_name = os.getenv('GEMINI_MODEL', 'gemini-1.5-flash-latest')
        
        # Initialize the model with system instruction
        self.model = genai.GenerativeModel(
            self.model_name,
            system_instruction=self.system_prompt
        )
        
        print(f"✅ Gemini AI Client initialized (Model: {self.model_name})")
    
    def generate_response(self, user_message: str) -> Optional[str]:
        """
        Generate a response from Gemini AI.
        
        Args:
            user_message (str): The user's input message
            
        Returns:
            Optional[str]: AI's response or None if error
        """
        try:
            response = self.model.generate_content(user_message)
            return response.text
            
        except Exception as e:
            print(f"❌ Error generating response: {str(e)}")
            return None
    
    def chat(self, user_message: str) -> str:
        """
        Simplified chat method that always returns a string.
        
        Args:
            user_message (str): The user's input message
            
        Returns:
            str: AI's response or error message
        """
        response = self.generate_response(user_message)
        
        if response is None:
            return "I'm sorry, I encountered an error processing your request."
        
        return response


if __name__ == "__main__":
    # Test the AI client
    try:
        client = AIClient()
        test_message = "Hello! Can you introduce yourself?"
        print(f"\nTest Message: {test_message}")
        response = client.chat(test_message)
        print(f"AI Response: {response}")
    except Exception as e:
        print(f"Error: {str(e)}")