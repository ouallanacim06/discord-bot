import discord
import respenses
async def send_message(message,user_message,is_private):
    try:
        respense = respenses.handle_response(user_message)
        await message.author.send(respense) if is_private else await message.channel.send(respense)
    except Exception as e:
        print(e)
def run_bot():
    token = "MTIxOTA2ODc5Mjk0NTExOTI2Mg.GAspHa.xK-wT1I-h92gBJR9YssvomPXn5Vczwtakmq39E"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    @client.event
    async def on_ready():
        print(f"{client.user} is running")
        print(client.latency)
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        channel = str(message.channel)
        user_message = str(message.content)
        print(f"{username}: send {user_message} in {channel}")
        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message,user_message,True)
        else:
            await send_message(message,user_message,False)
    @client.event
    async def on_reaction_add(reaction, user):
        try:
            if isinstance(reaction.emoji, discord.Emoji):
                print(f"{user} reacted with {reaction.emoji.name}")
            else:  # reaction.emoji is a str
                print(f"{user} reacted with {reaction.emoji}")
        except UnicodeEncodeError:
            print("working")

    client.run(token)