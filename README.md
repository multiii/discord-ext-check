# discord-ext-checks

discord-ext-checks is a module which implements various decorator functions, to be used on discord command functions for your DiscordPY bot

## Installation:

Installation is done using pip:
<link_here>

## Usage:

Starting off, import `discord.ext.checks` and then you can use its various decorator functions.

### Examples:

```py
from discord.ext import checks

#.. Creating your Discord Bot ...

"""Checking if the author is the Server Owner"""
@bot.command()
@checks.is_guild_owner()
async def foo(ctx):
    await ctx.send(f"{ctx.author.mention} is the Server Owner!")

"""Checking if 3 arguments were passed into the function"""
@bot.command()
@checks.has_args(3)
async def bar(ctx, x, y):
    await ctx.send(f"The result is {x + y}")
    
"""Error Handling"""
@bar.error
async def bar_error(ctx, error):
    if isinstance(error, checks.NotEnoughArgs):
        await ctx.send("You have to Enter 3 Arguments (ctx, x, and y) for the command to work")
    else:
        raise error
        
"""Checking if the author's id is in the list of Authorized Members"""
authorized_members = [394320584089010179, 446670262440820746, 449864700306522112]

@bot.command()
@checks.has_user_id_in(authorized_members)
async def baz(ctx):
    await ctx.send("You are an Authorized Member.")
    
"""Error Handling"""
@baz.error
async def baz_error(ctx, error):
    if isinstance(error, checks.MissingID):
        await ctx.send("You are not Authorized.")
    else:
        raise error
        
bot.run(token)
```

## Notes:
- A Documentation for this module will be coming soon..
