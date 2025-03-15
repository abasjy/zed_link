#@chanel_h_o
from rubpy import filters, Client
from rubpy.types import Update
app = Client('h_o')
@app.on_message_updates()
async def zed_id(message:Update):
    if "@" in message.text or "https://" in message.text or ".ir" in message.text:
            info = await app.get_me()
            guid = info["user"]["user_guid"]
            if message.author_guid == guid:
                pass
            else:
                await app.delete_messages(message.object_guid,[message.message_id]) 
                await message.reply("ارسال لینک در گروه مجاز نیست.")
                
                
                











app.run()