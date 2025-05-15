from langchain_ollama.chat_models import ChatOllama




llm = ChatOllama(
    model = "llama3.2:3b",
    temperature = 0.8,
    num_predict = 100,
)

response = llm.invoke("tell me more about python?")
print(response)