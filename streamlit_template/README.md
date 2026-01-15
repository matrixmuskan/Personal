# 🚀 Streamlit Demo Application

A beautiful and interactive Streamlit application template ready to deploy on Streamlit Community Cloud.

## ✨ Features

- 📊 Interactive data visualizations (Line, Bar, and Area charts)
- 🎨 Customizable settings via sidebar
- 📈 Real-time metrics display
- 💬 Interactive user input forms
- 🎨 Modern UI with custom styling
- 📱 Responsive layout

## 🛠️ Local Development Setup

### Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

### Installation with uv (Recommended)

1. **Install uv** (if not already installed):
```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. **Clone and navigate to the project**:
```bash
cd streamlit_template
```

3. **Create a virtual environment with uv**:
```bash
uv venv
```

4. **Activate the virtual environment**:
```bash
# On macOS/Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

5. **Install dependencies**:
```bash
uv pip install -r requirements.txt
```

6. **Run the Streamlit app**:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Alternative: Installation with pip

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🚀 Deploy to Streamlit Community Cloud

### Step 1: Push to GitHub

1. Create a new repository on GitHub
2. Push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### Step 2: Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository, branch, and main file (`app.py`)
5. Click "Deploy"

Your app will be live in minutes! 🎉

## 📁 Project Structure

```
streamlit_template/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .venv/             # Virtual environment (created locally)
```

## 🎨 Customization

### Modify the App

Edit `app.py` to customize:
- Page title and icon in `st.set_page_config()`
- Sidebar options and controls
- Chart types and visualizations
- Metrics and data displays
- Color schemes and styling

### Add Dependencies

To add new Python packages:

```bash
# With uv
uv pip install package-name

# Update requirements.txt
uv pip freeze > requirements.txt
```

Or manually add the package to `requirements.txt` and reinstall.

## 📚 Learn More

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Community Forum](https://discuss.streamlit.io)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [uv Documentation](https://github.com/astral-sh/uv)

## 🤝 Contributing

Feel free to fork this template and customize it for your needs!

## 📝 License

This project is open source and available under the MIT License.

## 💡 Tips

- Use `st.cache_data` decorator for expensive computations
- Keep your app responsive by limiting data size
- Test locally before deploying
- Check Streamlit Community Cloud logs if deployment fails
- Use secrets management for API keys (see [Streamlit Secrets](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management))

---

Built with ❤️ using [Streamlit](https://streamlit.io)

