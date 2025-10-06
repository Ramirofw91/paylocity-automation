# Paylocity Benefits Automation

This project contains automated tests for the Paylocity Benefits Dashboard using Playwright and pytest.

## Setup and Usage Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Ramirofw91/paylocity-automation.git
2. Navigate into the project directory
bash
cd paylocity-automation
3. (Optional but recommended) Create and activate a virtual environment
bash
python -m venv venv
# On Linux or macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
4. Install all dependencies
bash
pip install -r requirements.txt
5. Configure your credentials
Open config.py.
Replace placeholders with your actual login info:
python
# config.py
USERNAME = "your_username"
PASSWORD = "your_password"
6. Run the tests
bash
pytest
Notes:
Ensure your config.py has valid credentials.
Use headless=False in your Playwright tests if you want to watch the browser during testing.
Adjust your setup if needed, e.g., environment variables instead of editing config.py.
