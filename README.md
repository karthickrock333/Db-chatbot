# SS Chatbot

SS Chatbot is a Flask-based web application that combines audio transcription, natural language processing, and database querying to create an interactive chatbot experience. The chatbot is designed to answer questions about sales data stored in a Snowflake database.

![image](https://github.com/user-attachments/assets/83b7d75a-0d7e-4186-8dc2-70044fccc844)


## Features

- Audio recording and transcription using OpenAI's Whisper model
- Natural language processing to understand user queries
- Database querying using SQLDatabaseChain from LangChain
- Web interface for interacting with the chatbot

## Prerequisites

- Python 3.7+
- Snowflake database account
- OpenAI API key
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ss-chatbot.git
   cd ss-chatbot
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Update the Snowflake database connection string in `chatbot.py`:
   ```python
   db = SQLDatabase.from_uri("snowflake://Username:Password@Account/Database/Schema?role=Role&warehouse=Warehouse")
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Use the web interface to interact with the chatbot. You can type questions or use the audio recording feature to ask questions about the sales data.

## Project Structure

- `app.py`: Main Flask application
- `audio_helper.py`: Functions for audio recording and transcription
- `chatbot.py`: Chatbot logic and database interaction
- `few_shots.py`: Example queries for few-shot learning
- `templates/index.html`: HTML template for the web interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
