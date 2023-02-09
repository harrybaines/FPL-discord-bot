import os
from dotenv import load_dotenv
from fpl import get_fpl_scout_team
import interactions

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = interactions.Client(token=TOKEN)

@bot.command(
    name="scout",
    description="Get the latest FPL scout team"
)
async def scout(ctx: interactions.CommandContext):
    await ctx.send('Getting the FPL scout team...')

    scout_team = get_fpl_scout_team()
    await ctx.send(scout_team)

bot.start()