# Pidgin English Translator

A modern web application that translates Pidgin English to various languages using OpenAI's GPT-4 model.

## Features

- Translate Pidgin English to multiple languages
- Real-time translation using GPT-4o
- FastAPI backend
- Support for multiple target languages

PidginTranslator/
├── backend/
│ ├── src/
│ │ ├── main.py # FastAPI server
│ │ └── translator.py # Translation logic
│ └── requirements.txt

## Setup

### Backend

1. Create a `.env` file in the backend directory:
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Start the server:
```bash
uvicorn src.main:app --reload
```

## Usage

1. Open http://localhost:8000 in your browser
2. Enter Pidgin English text in the input field
3. Select your target language
4. Click "Translate" or press Enter
5. View your translation

## Supported Languages

- English
- Spanish
- French
- German
- Italian
- Portuguese
- Russian
- Japanese
- Korean
- Chinese

## Technologies Used

- Backend: FastAPI, Python
- API: OpenAI GPT-4o

## License

This project is licensed under the MIT License.