# Flask Calculator App

A simple and beautiful calculator web application built with Flask.

## Features

- ✨ Modern and responsive UI with gradient background
- 🧮 Basic arithmetic operations (addition, subtraction, multiplication, division)
- ⌨️ Keyboard support for easy input
- 🎨 Beautiful design with smooth animations
- 🚀 Fast client-side calculations

## Installation

1. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

### Mouse Input
- Click on the number and operator buttons to build your expression
- Click `=` to calculate the result
- Click `C` to clear the display

### Keyboard Input
- Numbers: `0-9`
- Operators: `+`, `-`, `*`, `/`
- Decimal: `.`
- Calculate: `Enter` or `=`
- Clear: `Escape` or `C`
- Backspace: `Backspace`

## Project Structure

```
.
├── app.py                 # Flask application
├── templates/
│   └── calculator.html    # Calculator UI
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Technologies Used

- **Backend**: Flask 3.0.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: Modern gradient UI with responsive layout

## License

MIT License - feel free to use this project for learning or personal use!

