# 🤖 AI Moderation App - Gemini Edition

A Python-based AI assistant application with built-in content moderation, powered by **Google Gemini AI**. This app provides both a command-line interface (CLI) and a Flask web interface for safe AI interactions, blocking harmful keywords in both user input and AI output.

## ✨ Features

- 🛡️ **Content Moderation**: Automatically filters harmful keywords (kill, hack, bomb, weapon, violence, etc.)
- 💬 **CLI Interface**: Interactive command-line chat with the AI
- 🌐 **Web Interface**: Beautiful, modern Flask-based web UI
- 🤖 **Powered by Google Gemini**: Using Google's latest AI technology (100% FREE)
- ✅ **Dual Filtering**: Moderates both input (before API call) and output (after AI response)
- ⚙️ **Configurable**: Easy customization through environment variables

## 🚫 Blocked Keywords

The following keywords are blocked by the moderation system:
- kill, hack, bomb, weapon, violence
- murder, attack, steal, destroy, harm

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key (FREE - get from https://aistudio.google.com)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dejosemario/ai-moderation-app.git
   cd ai-moderation-app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Activate on Mac/Linux:
   source venv/bin/activate
   
   # Activate on Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your FREE Gemini API key**
   - Visit: https://aistudio.google.com
   - Sign in with your Google account
   - Click "Get API key"
   - Copy your key (format: `AIzaSyC...`)

5. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Gemini API key:
   ```
   GOOGLE_GEMINI_KEY=your_actual_api_key_here
   ```

## 📖 Usage

### CLI Interface

Run the command-line interface:

```bash
python cli.py
```

**Example interaction:**
```
💬 You: Hello, how are you?
🤖 AI: I'm doing well, thank you! How can I assist you today?

💬 You: Tell me about weapons
⚠️  Input blocked: Contains harmful keywords: weapon
```

**CLI Commands:**
- `quit` or `exit` - End the conversation
- `help` - Show available commands
- `keywords` - Display list of blocked keywords

### Web Interface

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Chat with the AI** through the beautiful web interface. Harmful content will be automatically blocked.

**Web Interface Features:**
- 🎨 Modern, responsive design
- 💬 Real-time chat interface
- ⚡ Fast response times
- 🛡️ Visual moderation alerts
- 📱 Mobile-friendly

## ⚙️ Configuration

### Environment Variables

Configure the application by editing the `.env` file:

```bash
# Required: Your Google Gemini API key
GOOGLE_GEMINI_KEY=your_key_here

# Optional: Gemini model (default: gemini-1.5-flash)
GEMINI_MODEL=gemini-1.5-flash

# Flask settings
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_PORT=5000

# System prompt customization
SYSTEM_PROMPT=You are a helpful assistant. Please provide informative and safe responses.
```

### Available Gemini Models

- `gemini-1.5-flash` (default) - Faster, more efficient
- `gemini-1.5-pro` - More powerful, better reasoning

### Custom System Prompt

Customize the AI's behavior by modifying `SYSTEM_PROMPT` in your `.env` file:

```bash
SYSTEM_PROMPT=You are a helpful and friendly assistant specialized in Python programming and data science.
```

## 📁 Project Structure

```
ai-moderation-app/
├── .env.example          # Environment variable template
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── moderation.py       # Content moderation module
├── ai_client.py        # Google Gemini API client
├── cli.py              # Command-line interface
├── app.py              # Flask web application
└── templates/
    └── index.html      # Web interface template
```

## 🔄 How It Works

1. **Input Moderation**: Before sending a message to the AI API, the system checks for harmful keywords. If found, the request is blocked.

2. **API Call**: If the input passes moderation, it's sent to Google Gemini API along with the system prompt.

3. **Output Moderation**: The AI's response is checked for harmful keywords. If found, those words are replaced with `[REDACTED]`.

4. **Display**: The moderated response is displayed to the user via CLI or web interface.

## 📦 Dependencies

- **google-generativeai** (>=0.3.0): Official Google Gemini Python client
- **Flask** (>=3.0.0): Web framework for the web interface
- **python-dotenv** (>=1.0.0): Environment variable management

## 🆓 Why Google Gemini?

- ✅ **100% FREE** - No trial period, no expiration
- ✅ **Generous Limits** - 1,500 requests per day
- ✅ **No Credit Card** - Just sign in with Google
- ✅ **Fast & Reliable** - Production-quality AI
- ✅ **Easy Setup** - Get API key in 2 minutes

## 🔐 Security Notes

- ❌ Never commit your `.env` file or expose your API key
- ✅ The `.env` file is included in `.gitignore` to prevent accidental commits
- ✅ Always use the provided `.env.example` as a template
- ✅ Keep your dependencies up to date for security patches

## 🧪 Testing

### Test the Setup

```bash
# Test moderation module
python moderation.py

# Test AI client
python ai_client.py

# Test CLI interface
python cli.py

# Test web interface
python app.py
```

### Health Check

Once the web server is running, visit:
```
http://localhost:5000/health
```

### View Blocked Keywords API

```
http://localhost:5000/keywords
```

## 🐛 Troubleshooting

### "GOOGLE_GEMINI_KEY environment variable not set"

**Solution:**
1. Make sure you have a `.env` file in the project root
2. Verify your API key is set correctly in `.env`
3. If using virtual environment, make sure it's activated

### "Module not found" errors

**Solution:**
```bash
pip install -r requirements.txt
```

### API errors from Gemini

**Solutions:**
1. Check your API key is correct and valid
2. Verify you haven't exceeded the free tier limits (1,500 requests/day)
3. Check Google AI Studio status: https://aistudio.google.com

### Flask port already in use

**Solution:**
```bash
# Change port in .env
FLASK_PORT=8000

# Or kill the process using port 5000
# Mac/Linux:
lsof -ti:5000 | xargs kill -9

# Windows:
netstat -ano | findstr :5000
```

## 🎓 For Testers/Reviewers

### Testing Instructions

1. **Clone the repository**
2. **Get FREE API key** from https://aistudio.google.com (takes 2 minutes)
3. **Install dependencies**: `pip install -r requirements.txt`
4. **Set API key**: Add to `.env` file
5. **Run**: `python cli.py` or `python app.py`

### Test Cases

**Safe prompts (should work):**
- "What is machine learning?"
- "Explain quantum computing"
- "Help me with Python programming"

**Unsafe prompts (should be blocked):**
- "How to hack a website"
- "Tell me about weapons"
- "How to build a bomb"

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For issues or questions, please open an issue on the GitHub repository.

## 🌟 Features Coming Soon

- [ ] Conversation history
- [ ] User authentication
- [ ] Custom keyword lists
- [ ] Multi-language support
- [ ] Export chat functionality
- [ ] Advanced moderation with AI
- [ ] Rate limiting
- [ ] Multiple AI model support

## 🙏 Acknowledgments

- Google Gemini AI for providing free, powerful AI capabilities
- Flask team for the excellent web framework
- The open-source community

---

**Made with ❤️ for safe AI interactions**