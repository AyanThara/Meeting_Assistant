#!/bin/bash
# Smart Meeting Assistant - Automated Setup Script
# Run this script to set up everything automatically

set -e  # Exit on error

PROJECT_DIR="$HOME/Desktop/Smart-Meeting-Assistant"
BACKEND_DIR="$PROJECT_DIR/backend"
FRONTEND_DIR="$PROJECT_DIR/frontend"

echo "🚀 Smart Meeting Assistant - Automated Setup"
echo "=============================================="

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Backend Setup
echo -e "\n${YELLOW}[1/4]${NC} Setting up backend..."

cd "$BACKEND_DIR"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install --upgrade -r requirements.txt

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo -e "${YELLOW}⚠️  IMPORTANT: Update .env with your API keys!${NC}"
fi

echo -e "${GREEN}✅ Backend setup complete${NC}"

# Frontend Setup
echo -e "\n${YELLOW}[2/4]${NC} Setting up frontend..."

cd "$FRONTEND_DIR"

# Install dependencies
echo "Installing Node dependencies..."
npm install

# Create .env.local if it doesn't exist
if [ ! -f ".env.local" ]; then
    echo "Creating .env.local file from template..."
    cp .env.example .env.local
fi

echo -e "${GREEN}✅ Frontend setup complete${NC}"

# Validation
echo -e "\n${YELLOW}[3/4]${NC} Validating setup..."

cd "$BACKEND_DIR"

# Check if .env has required variables
REQUIRED_VARS=("STREAM_API_KEY" "STREAM_API_SECRET" "GOOGLE_API_KEY" "DEEPGRAM_API_KEY")
MISSING=0

for var in "${REQUIRED_VARS[@]}"; do
    if ! grep -q "^$var=" .env; then
        echo -e "${RED}❌ Missing: $var${NC}"
        MISSING=$((MISSING + 1))
    fi
done

if [ $MISSING -gt 0 ]; then
    echo -e "\n${YELLOW}⚠️  MISSING $MISSING environment variables!${NC}"
    echo "Please update .env with your API keys from:"
    echo "  • GetStream: https://getstream.io/try-for-free"
    echo "  • Gemini: https://ai.google.dev"
    echo "  • Deepgram: https://console.deepgram.com"
else
    echo -e "${GREEN}✅ All environment variables configured${NC}"
fi

# Summary
echo -e "\n${YELLOW}[4/4]${NC} Setup Summary"
echo "=============================================="
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "Next steps:"
echo "1. Update your API keys in: $BACKEND_DIR/.env"
echo ""
echo "To run the project:"
echo ""
echo "Terminal 1 (Backend):"
echo "  cd $BACKEND_DIR"
echo "  source venv/bin/activate"
echo "  python main.py"
echo ""
echo "Terminal 2 (Frontend):"
echo "  cd $FRONTEND_DIR"
echo "  npm run dev"
echo ""
echo "Then open: http://localhost:3000"
echo ""
echo "=============================================="
