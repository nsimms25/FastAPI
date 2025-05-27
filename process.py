
def checkport_commands(info):
    command_array = []
    
    author = info.author
    email = info.email
    project_id = info.project_id
    port_string = info.ports
    
    author_string = f"This was created for {author}"
    email_string = f"For questions and concerns contact {email}"
    project_string = f"This is for project number {project_id}"

    command_array.append(author_string)
    command_array.append(email_string)
    command_array.append(project_string)

    #Add check optics (Nokia)
    command_array.append(f"show isis adj")
    command_array.append(f"show lag desc")
    command_array.append(f"show port {port_string}")
    command_array.append(f"show port {port_string} optical")

    return command_array