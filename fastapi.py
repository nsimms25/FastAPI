from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from process import checkport_commands

app = FastAPI()

