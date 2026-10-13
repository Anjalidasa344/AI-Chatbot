\# Smart AI Chatbot



A Python-based Smart AI Chatbot with a graphical user interface (GUI), Wikipedia-powered question answering, greeting responses, and conversation history management.



\## Features



\- Interactive desktop GUI using Python Tkinter.

\- Answers questions using the Wikipedia API.

\- Provides predefined responses to common greetings.

\- Saves conversations with date and time.

\- Allows users to view previous chat history.

\- Supports sending messages using the Send button or Enter key.

\- Includes an Exit option.



\## Technologies Used



\- Python 3

\- Tkinter

\- Requests

\- Wikipedia MediaWiki API



\## Project Structure



```text

Smart-AI-Chatbot/

│

├── smart\_chatbot.py

├── chatbot\_gui.py

├── requirements.txt

└── README.md

```



\## Installation



\### 1. Clone the repository



```bash

git clone https://github.com/Anjalidasa344/AI-Chatbot.git

```



\### 2. Open the project folder



```bash

cd AI-Chatbot/Smart-AI-Chatbot

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Run the desktop chatbot



```bash

python chatbot\_gui.py

```



Alternatively, run the command-line version:



```bash

python smart\_chatbot.py

```



\## Chatbot Commands



| Command | Description |

|---|---|

| Hi | Displays a greeting |

| History | Displays saved conversations |

| Exit | Closes the chatbot |



\## How It Works



The chatbot first checks whether the user's message matches a predefined greeting or command.



If it is a general question, the application searches Wikipedia through its API and displays the available introductory summary.



Conversations are saved locally in `chat\_history.txt`.



\## Limitations



\- An internet connection is required for Wikipedia searches.

\- Answers depend on available Wikipedia content.

\- The chatbot is retrieval-based and does not generate responses like a large language model.

\- Conversation history is stored locally.



\## Future Enhancements



\- Improved graphical interface.

\- Better question matching.

\- Additional language support.

\- Integration with a generative AI API.



\## Author



\*\*Anjali Dasa\*\*



\## License



This project is intended for educational and learning purposes.

