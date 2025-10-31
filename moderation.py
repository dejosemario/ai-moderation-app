"""
Content Moderation Module
Provides input and output filtering for harmful keywords
"""

from typing import List, Tuple


class ContentModerator:
    """Moderates content by checking for harmful keywords."""
    
    # List of blocked keywords
    BLOCKED_KEYWORDS = [
        'kill',
        'hack',
        'bomb',
        'weapon',
        'violence',
        'murder',
        'attack',
        'steal',
        'destroy',
        'harm'
    ]
    
    def __init__(self, custom_keywords: List[str] = None):
        """
        Initialize the content moderator.
        
        Args:
            custom_keywords: Optional list of additional keywords to block
        """
        self.blocked_keywords = self.BLOCKED_KEYWORDS.copy()
        
        if custom_keywords:
            self.blocked_keywords.extend(custom_keywords)
    
    def check_content(self, text: str) -> Tuple[bool, List[str]]:
        """
        Check if text contains any blocked keywords.
        
        Args:
            text (str): Text to check
            
        Returns:
            Tuple[bool, List[str]]: (is_safe, list_of_violations)
                - is_safe: True if no violations found
                - list_of_violations: List of blocked keywords found
        """
        if not text:
            return True, []
        
        text_lower = text.lower()
        violations = []
        
        for keyword in self.blocked_keywords:
            if keyword in text_lower:
                violations.append(keyword)
        
        is_safe = len(violations) == 0
        return is_safe, violations
    
    def moderate_input(self, user_input: str) -> Tuple[bool, str]:
        """
        Moderate user input before sending to AI.
        
        Args:
            user_input (str): User's input message
            
        Returns:
            Tuple[bool, str]: (is_approved, message)
                - is_approved: True if input is safe
                - message: Error message if blocked, empty string if approved
        """
        is_safe, violations = self.check_content(user_input)
        
        if not is_safe:
            violation_list = ', '.join(violations)
            message = f"⚠️  Input blocked: Contains harmful keywords: {violation_list}"
            return False, message
        
        return True, ""
    
    def moderate_output(self, ai_response: str) -> str:
        """
        Moderate AI output by replacing harmful keywords.
        
        Args:
            ai_response (str): AI's response
            
        Returns:
            str: Moderated response with keywords replaced
        """
        is_safe, violations = self.check_content(ai_response)
        
        if not is_safe:
            # Replace blocked keywords with [REDACTED]
            moderated_text = ai_response
            for keyword in violations:
                import re
                pattern = re.compile(re.escape(keyword), re.IGNORECASE)
                moderated_text = pattern.sub('[REDACTED]', moderated_text)
            
            return moderated_text
        
        return ai_response
    
    def get_blocked_keywords(self) -> List[str]:
        """
        Get the list of currently blocked keywords.
        
        Returns:
            List[str]: List of blocked keywords
        """
        return self.blocked_keywords.copy()


if __name__ == "__main__":
    # Test the moderator
    moderator = ContentModerator()
    
    # Test input moderation
    print("Testing Input Moderation:")
    print("-" * 50)
    
    test_inputs = [
        "Hello, how are you?",
        "How to hack a system?",
        "Tell me about weapons",
        "What is machine learning?"
    ]
    
    for test_input in test_inputs:
        is_approved, message = moderator.moderate_input(test_input)
        if is_approved:
            print(f"✅ Approved: {test_input}")
        else:
            print(f"❌ {message}")
    
    print("\n" + "=" * 50)
    print("Testing Output Moderation:")
    print("-" * 50)
    
    test_outputs = [
        "AI systems are fascinating!",
        "Never attempt to hack into systems.",
        "Violence is never the answer."
    ]
    
    for test_output in test_outputs:
        moderated = moderator.moderate_output(test_output)
        if moderated != test_output:
            print(f"⚠️  Moderated: {test_output}")
            print(f"   Result: {moderated}")
        else:
            print(f"✅ Clean: {test_output}")