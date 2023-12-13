from program import client, filters
CMD = ["/", "."]
@client.on_message(filters.command("credits", CMD))
async def check_alive(_, message):
   await message.reply_text(" Here Your Text")
