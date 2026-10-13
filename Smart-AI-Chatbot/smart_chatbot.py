
import requests
from datetime import datetime

API_URL = "https://en.wikipedia.org/w/api.php"

HEADERS = {
    "User-Agent": "AnjaliSmartChatbot/1.0 (Python educational project)"
}


# 1. Save conversation history
def save_chat(question, answer):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"\nDate: {datetime.now()}\n")
        file.write(f"You: {question}\n")
        file.write(f"Bot: {answer}\n")
        file.write("-" * 50 + "\n")


# 2. View previous chat history
def view_history():
    try:
        with open("chat_history.txt", "r", encoding="utf-8") as file:
            history = file.read()

        if history.strip():
            print("\n========== CHAT HISTORY ==========")
            print(history)
            print("==================================")
        else:
            print("Bot: No chat history available.")

    except FileNotFoundError:
        print("Bot: No previous chat history found.")


# 3. Smart greeting responses
def get_greeting(question):
    message = question.lower().strip()
    message = message.rstrip("?!., ")

    greetings = {
        "hi": "Hello! How can I help you?",
        "hello": "Hey! Nice to meet you.",
        "hey": "Hey there! What would you like to know?",
        "good morning": "Good morning! Have a great day.",
        "good afternoon": "Good afternoon! How can I help you?",
        "good evening": "Good evening! What can I do for you?",
        "how are you": "I'm doing great! Thanks for asking.",
        "thank you": "You're welcome! Happy to help.",
        "thanks": "You're welcome!",
        "who are you": "I'm your Smart AI Chatbot.",
        "what can you do": "I can answer questions, respond to greetings, and save our chat history."
    }

    return greetings.get(message)


# 4. Wikipedia question-answering system
def get_answer(question):
    try:
        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": question,
            "format": "json"
        }

        response = requests.get(
            API_URL,
            params=search_params,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()
        data = response.json()

        results = data.get("query", {}).get("search", [])

        if not results:
            return "Sorry, I couldn't find an answer."

        page_title = results[0]["title"]

        extract_params = {
            "action": "query",
            "prop": "extracts",
            "explaintext": 1,
            "exintro": 1,
            "titles": page_title,
            "format": "json"
        }

        response = requests.get(
            API_URL,
            params=extract_params,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()
        data = response.json()

        pages = data.get("query", {}).get("pages", {})

        for page in pages.values():
            answer = page.get("extract", "")

            if answer:
                return answer[:1500]

        return "I found a page, but it has no available summary."

    except requests.exceptions.Timeout:
        return "The search timed out. Please try again."

    except requests.exceptions.ConnectionError:
        return "Internet connection problem. Please check your network."

    except requests.exceptions.HTTPError as error:
        return f"Wikipedia server error: {error}"

    except ValueError:
        return "The search service returned an invalid response."

    except Exception as error:
        return f"Unexpected error: {error}"


# 5. Main chatbot function
def start_chatbot():

    print("\n================================")
    print("       SMART AI CHATBOT")
    print("================================")
    print("Ask me anything!")
    print("Type 'history' to view previous conversations.")
    print("Type 'exit' to stop.")
    print("--------------------------------")

    while True:

        question = input("\nYou: ").strip()

        if not question:
            print("Bot: Please enter a question.")
            continue

        # Exit chatbot
        if question.lower() in ["exit", "quit", "bye"]:
            print("Bot: Thank you for chatting. Goodbye!")
            break

        # View chat history
        if question.lower() == "history":
            view_history()
            continue

        # Greeting responses
        answer = get_greeting(question)

        if answer:
            print("\nBot:", answer)

        else:
            # Search Wikipedia
            print("\nBot: Searching...")
            answer = get_answer(question)
            print("\nBot:", answer)

        # Save conversation
        save_chat(question, answer)


# 6. Run chatbot
if __name__ == "__main__":
    start_chatbot()
