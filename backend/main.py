from fastapi import FastAPI
from backend.mcp_router import router  # Correct if run from project root

app = FastAPI(title="Career Assistance Portal")

# Include the router
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Career Coach API is up and running 🚀"}
