from fastapi import FastAPI
from pydantic import BaseModel
from process import checkport_commands

app = FastAPI()

class ProjectInfo(BaseModel):
    name: str
    email: str
    project_id: str
    port: str

@app.post("/submit/")
async def submit_project(info: ProjectInfo):
    processed = checkport_commands(
        name=info.name,
        email=info.email,
        project_id=info.project_id,
        port=info.port
    )
    return {
        "message": "Project processed",
        "output": processed
    }