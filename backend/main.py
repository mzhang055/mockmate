from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from api.controllers import upload, questions, pdf

# Add logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "https://www.simplymockit.com", 
        "https://simplymockit.com",
        "https://mockmate-sage.vercel.app/"
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="")
app.include_router(questions.router, prefix="")
app.include_router(pdf.router, prefix="") 