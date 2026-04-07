def process_command(text):
    text = text.lower()

    if "detect" in text:
        return {
            "action": "detect",
            "message": "Running detection"
        }

    elif "safety" in text:
        return {
            "action": "safety",
            "message": "Checking safety conditions"
        }

    elif "shutdown" in text:
        return {
            "action": "shutdown",
            "message": "Emergency shutdown initiated"
        }

    elif "status" in text:
        return {
            "action": "twin",
            "message": "Fetching system status"
        }

    return {
        "action": "unknown",
        "message": "Command not recognized"
    }