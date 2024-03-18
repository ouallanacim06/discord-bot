from datetime import datetime
now = datetime.now()
def handle_response(message) -> str:
    massage = message.lower()
    if message == "hello":
        return "Hi"
    if message == "how are you?":
        return "I'm fine, thank you"
    if message == "!time":     
        time = now.strftime("%H:%M:%S")
        return str(time)
    if message == "!date":
        date = now.strftime("%Y-%m-%d")
        return str(date)
    if message == "!help":
        return "`I can help you with the following commands: \n!help - to get help \n!time - to get the current time \n!date - to get the current date`"
    