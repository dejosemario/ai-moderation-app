"""
Flask Web Application for AI Moderation App
Web interface for chatting with Gemini AI with content moderation
"""

import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from ai_client import AIClient
from moderation import ContentModerator

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Initialize AI client and moderator
try:
    ai_client = AIClient()
    moderator = ContentModerator()
    print("✅ Flask app initialized successfully")
except Exception as e:
    print(f"❌ Error initializing app: {str(e)}")
    ai_client = None
    moderator = None


@app.route('/')
def index():
    """Render the main chat interface."""
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chat requests from the web interface.
    
    Expected JSON: {"message": "user message"}
    Returns JSON: {"success": bool, "response": str, "error": str (optional)}
    """
    try:
        # Check if services are initialized
        if ai_client is None or moderator is None:
            return jsonify({
                'success': False,
                'error': 'AI services not initialized. Check your GOOGLE_GEMINI_KEY.'
            }), 500
        
        # Get user message from request
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'success': False,
                'error': 'Please enter a message.'
            }), 400
        
        # Moderate input
        is_approved, moderation_message = moderator.moderate_input(user_message)
        
        if not is_approved:
            return jsonify({
                'success': False,
                'error': moderation_message
            }), 400
        
        # Get AI response
        ai_response = ai_client.chat(user_message)
        
        if ai_response is None:
            return jsonify({
                'success': False,
                'error': 'Failed to get response from AI.'
            }), 500
        
        # Moderate output
        moderated_response = moderator.moderate_output(ai_response)
        
        # Return response
        return jsonify({
            'success': True,
            'response': moderated_response
        })
        
    except Exception as e:
        print(f"Error in /chat endpoint: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    status = {
        'status': 'healthy',
        'ai_client': ai_client is not None,
        'moderator': moderator is not None
    }
    return jsonify(status)


@app.route('/keywords')
def keywords():
    """Get list of blocked keywords."""
    if moderator is None:
        return jsonify({
            'success': False,
            'error': 'Moderator not initialized'
        }), 500
    
    return jsonify({
        'success': True,
        'keywords': moderator.get_blocked_keywords()
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template('index.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    # Get Flask configuration from environment
    flask_env = os.getenv('FLASK_ENV', 'development')
    flask_debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    flask_port = int(os.getenv('FLASK_PORT', 5000))
    
    print("\n" + "=" * 60)
    print("🌐 Starting Flask Web Server")
    print("=" * 60)
    print(f"Environment: {flask_env}")
    print(f"Debug Mode: {flask_debug}")
    print(f"Port: {flask_port}")
    print(f"URL: http://localhost:{flask_port}")
    print("=" * 60)
    print("\nPress Ctrl+C to stop the server\n")
    
    # Run the Flask app
    app.run(
        host='0.0.0.0',
        port=flask_port,
        debug=flask_debug
    )