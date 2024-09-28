import requests
import time

# Your API key (ensure it's valid and has the right permissions)
API_KEY = "AIzaSyCqxTYDTxZ9Mgq64wSPQxMaQ9lz9ipqk-s"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"

# List of stop commands
STOP_COMMANDS = ['STOP', 'EXIT', 'ABORT', 'QUIT', 'BYE', 'TERMINATE']

def generate_answer(question):
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": question
                    }
                ]
            }
        ]
    }

    retry_count = 0
    max_retries = 5  # Limit retries to avoid locking the program forever
    
    while retry_count < max_retries:
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Extract the answer from the response
            answer = response.json()
            if 'candidates' in answer and len(answer['candidates']) > 0:
                return answer['candidates'][0]['content']['parts'][0]['text']  # Adjust based on response structure
            else:
                return "No response generated."
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            break
        except requests.exceptions.RequestException as e:
            print(f"A request error occurred: {e}")
            retry_count += 1
            print(f"Retrying... ({retry_count}/{max_retries})")
            time.sleep(10)  # Wait 10 seconds before retrying

    print("Max retries reached. Try again later.")
    return None

# Example of using the function
if __name__ == "__main__":
    print("Welcome to the Chatbot! Type 'STOP', 'EXIT', 'ABORT', 'QUIT', 'BYE', or 'TERMINATE' to exit.")
    while True:
        user_input = input("Press 1 to communicate and 2 to ask: ").strip().upper()

        # Exit if stop commands are entered
        if user_input in STOP_COMMANDS:
            print("Exiting the program. Goodbye!")
            break
        
        if user_input == "2":
            question = input("Ask a question: ").strip()
            
            if question.upper() in STOP_COMMANDS:
                print("Exiting the program. Goodbye!")
                break

            answer = generate_answer(question)
            if answer:
                print(f"Answer: {answer}")
            else:
                print("Failed to get a response. Please try again later.")
        elif user_input == "1":
            print("Communicating...")
            # Add your communication logic here
        else:
            print("Invalid input, please try again.")
