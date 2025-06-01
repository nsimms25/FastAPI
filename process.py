
def checkport_commands(name: str, email: str, project_id: str, port: str) -> list:
    command_array = []
    
    author_string = f"This was created for {name}"
    email_string = f"For questions and concerns contact {email}"
    project_string = f"This is for project number {project_id}"

    command_array.append(author_string)
    command_array.append(email_string)
    command_array.append(project_string)

    #Add check optics (Nokia)
    command_array.append(f"show isis adj")
    command_array.append(f"show lag desc")
    command_array.append(f"show port {port}")
    command_array.append(f"show port {port} optical")

    return command_array

def verify_inputs(name: str, email: str, project_id: str, crl_lines: str):
    output = []
    output.append(f"The autoher name is: {name}")
    output.append(f"The auther email is: {email}")
    output.append(f"Here is the project ID: {project_id}")

    output.append("Below are the crl lines that will be used.")
    output.append(crl_lines)

    return output
