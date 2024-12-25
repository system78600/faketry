from pyrogram import filters
from BrandrdXMusic import app
from BrandrdXMusic.utils.https import fetch  # Import the fetch function

url_sfw = "https://api.waifu.pics/sfw/fuck"

@app.on_message(filters.command("fuck"))
async def slap(client, message):
    # Fetch a random slap gif
    response = await fetch.get(url_sfw)
    result = response.json()  # Parse the JSON response
    img = result["url"]
    await message.reply_animation(img)
