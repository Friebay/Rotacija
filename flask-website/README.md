# Flask Website Project

This is a simple Flask web application that guides users through a series of questions regarding their funding status and class grades. Based on user input, the application dynamically presents subsequent questions.

## Project Structure

```
flask-website
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── question.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── run.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd flask-website
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python run.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- The application starts with a landing page that asks about your funding status.
- Based on your answers, you will be directed to further questions regarding your class names and final grades.
- The application processes your input and provides relevant feedback.

## Dependencies

- Flask
- Any other necessary libraries listed in `requirements.txt`.

## License

This project is licensed under the MIT License.