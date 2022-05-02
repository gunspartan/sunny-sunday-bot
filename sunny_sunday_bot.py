import interactions
import re
from dotenv import load_dotenv
import os
from scrape_maplestory import formatSunnySundays, getSunnySundays


load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")

bot = interactions.Client(token=discord_token)
@bot.command(
  name="sunny_sundays",
  description="Gets the Sunny Sundays from the Patch notes",
  options = [
    interactions.Option(
      name="text",
      description="Patch notes URL",
      type=interactions.OptionType.STRING,
      required=True,
    )
  ]
)
async def my_first_command(ctx: interactions.CommandContext, text: str):
  # Validate URL
  MAPLESTORY_URL = "maplestory.nexon.net/news/"
  valid_url = re.search(MAPLESTORY_URL, text)
  if (not valid_url):
    await ctx.send("Please enter the URL to the Maplestory Patch Notes.")
    return
  else:
    sunnyList = getSunnySundays(text)
    sunnyEvents = formatSunnySundays(sunnyList)
    eventEmbeds = []
    for event in sunnyEvents:
      eventTitle = event['title']
      eventDescription = event['description']
      embedMessage = interactions.Embed(
        title=eventTitle,
        description=eventDescription,
      )
      eventEmbeds.append(embedMessage)

    await ctx.send(
      embeds=eventEmbeds,
    )


bot.start()