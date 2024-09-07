from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from flask import Flask, request, jsonify  

# Chatbot template
template = """
Answer the question below.

Here is the conversation history: {context}

Question : {question}

Answer :    
"""

# Initialize the Llama3 model
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Initialize Flask App
app = Flask(__name__)
    
# Define the chat endpoint
@app.route('/chat', methods=['POST'])

def chat():
    print('Received request:', request.json)
    # Parse the incoming JSON data from the request
    data = request.json

    # Extract the 'context' and 'question' from the data
    context = data.get("context", "")
    question = data["question"]

    # Check if the conversation is just starting (no context)
    if not context:
        context = "Hey there, I am a mental health chatbot here to help you with any mental health problems that you may have or have a fun conversation together. Type 'exit' to quit."
        print(context)  # Print the initial message on the console

    # Invoke the Llama3 model with the input question and context
    result = chain.invoke({"context": context, "question": question})

    # Update the conversation context with the new user input and response
    context += f"\nUser: {question}\nAI: {result}"

    # Return the response and updated context in JSON format
    return jsonify({"response": result, "context": context})

# Run the Flask app
if __name__ == "__main__":
    print('Flask app is running on http://localhost:5000')
    print("Server is running. Start chatting with the mental health chatbot!")
    app.run(host='0.0.0.0', port=5000)
