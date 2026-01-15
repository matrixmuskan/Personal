#!/bin/bash

# Setup script for Streamlit Template
# This script helps you quickly set up the development environment

echo "🚀 Setting up Streamlit Template..."
echo ""

# Check if uv is installed
if ! command -v uv &> /dev/null
then
    echo "❌ uv is not installed."
    echo "📦 Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    echo "✅ uv installed successfully!"
    echo ""
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
uv venv
echo "✅ Virtual environment created!"
echo ""

# Install dependencies
echo "📥 Installing dependencies..."
source .venv/bin/activate
uv pip install -r requirements.txt
echo "✅ Dependencies installed!"
echo ""

echo "🎉 Setup complete!"
echo ""
echo "To run the app:"
echo "  1. Activate the virtual environment:"
echo "     source .venv/bin/activate"
echo "  2. Run the Streamlit app:"
echo "     streamlit run app.py"
echo ""
echo "The app will open in your browser at http://localhost:8501"

