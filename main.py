from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    docs_url = "http://localhost:8000/docs"
    message = f"Here's the link to the FastAPI documentation: {docs_url}"
    return message
