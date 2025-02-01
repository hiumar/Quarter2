import ollama

MODEL = "llama3.2"  # Ensure this model name is correct and supported by Ollama

# Loop to take user input and interact with the chatbot
while True:
    user_input = input("Enter your message (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Exiting the chatbot. Goodbye!")
        break

    messages = [
        {"role": "user", "content": user_input}
    ]
    
    try:
        response = ollama.chat(model=MODEL, messages=messages)
        
        # Safely access and print the response content
        if 'message' in response and 'content' in response['message']:
            print("Chat:", response['message']['content'])
        else:
            print("Unexpected response format:", response)
    except Exception as e:
        print(f"An error occurred: {e}")
