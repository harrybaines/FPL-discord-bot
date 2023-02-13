import os
from dotenv import load_dotenv
from fpl import get_fpl_scout_team
import interactions
from interactions.ext.files import command_send
import io

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
    team_img = get_fpl_scout_team()
    
    with io.BytesIO(team_img) as fp:
        file = interactions.File(filename='team.png', fp=fp)
        await command_send(ctx, files=file)

bot.start()