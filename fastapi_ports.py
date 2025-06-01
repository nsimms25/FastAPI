from fastapi import FastAPI
from pydantic import BaseModel
from process import checkport_commands
from process import verify_inputs

app = FastAPI()

crl_input = """BEFORE:
device1 1/1/1 <> device2 2/2/1
device1 1/1/2 <> device2 2/2/2
device1 1/1/3 <> device2 2/2/3
device1 ae1.1 <> device2 ae4.1
192.168.1.1/30 <> 192.168.1.2/30
1234 <> 9876

AFTER:
device3 3/1/1 <> device2 2/2/1
device3 3/1/2 <> device2 2/2/2
device3 3/1/3 <> device2 2/2/3
device3 ae1.1 <> device2 ae4.1
192.168.1.1/30 <> 192.168.1.2/30
3456 <> 9876
"""

author_name = "Nick"
author_email = "nick@myemail.com"
project_num = "project-001"

dict_input = {
    "crl_lines" : crl_input,
    "name" : author_name,
    "email" : author_email,
    "project_id" : project_num

}

class ProjectInfo(BaseModel):
    name: str
    email: str
    project_id: str
    crl_lines: str

@app.post("/verify/")
async def submit_project(info: ProjectInfo):
    output = verify_inputs(
        name=info.name,
        email=info.email,
        project_id=info.project_id,
        crl_lines=info.crl_lines
    )
    return {
        "message": "processed output",
        "output": output
    }
