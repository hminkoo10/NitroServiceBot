import discord
from discord.ext import commands
import os
import asyncio
import random
import re


# 임배드 함수
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)
helpcommand = ".info (봇 정보를 확인합니다)\n.credit (크레딧을 확인합니다)\n.eval [값] (eval 함수)\n.reload {모듈이름} (모듈을 리로드합니다)\n.load {모듈이름} (모듈을 로드합니다)\n.unload {모듈이름} (모듈을 언로드합니다)\n.removemessage {청소할 메시지 수} (메시지를 청소합니다. 입력을 하지 않으면 모두 청소됩니다.)\n.ban [유저 맨션, 아이디, 이름 셋중 아무거나] {사유} (유저를 밴합니다)\n.unban [유저 맨션, 아이디, 이름 셋중 아무거나] (유저를 언밴합니다)\n.kick [유저 맨션, 아이디, 이름 셋중 아무거나] {사유} (유저를 킥합니다)\n.timeout [유저 맨션, 아이디, 이름 셋중 아무거나] [초] (유저를 타임아웃합니다)\n.removetimeout [유저 맨션, 아이디, 이름 셋중 아무거나] (유저를 타임아웃 해제합니다)\n\n여기서 []는 필수, {}는 선택, ()는 설명을 나타냅니다."

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.is_owner()
    @commands.command(name="help")
    async def help_(self,ctx):
        await ctx.reply(embed=embed("도움말",helpcommand))
    # 정보
    @commands.command()
    async def info(self, ctx):
        await ctx.reply(embed=embed(
            '정보',
            'Ver. Release 1.0 \n Made By Milky2110#5252. 이 봇은 특수목적봇이며, Nitro Service를 위해 만들어졌습니다.'
        ))

    # 크레딧
    @commands.command()
    async def credit(self, ctx):
        await ctx.reply(embed=embed(
            '크레딧', 'Milky2110 \n hminkoo10(Milky2110#5252)'))
def setup(bot):
    bot.add_cog(Core(bot))