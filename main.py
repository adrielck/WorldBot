import asyncio	
from datetime import time	
from random import random	
import datetime	
import discord	
import key	
import requests	
from io import BytesIO	
from PIL import Image, ImageDraw, ImageFont, ImageOps	

client = discord.Client()	

COR = 0x690FC3	
TOKEN = key.seu_token()	
msg_id = None	
msg_user = None	


@client.event	
async def on_member_join(member):	
    channel = client.get_channel("467782032374759426")	

    url = requests.get(member.avatar_url)	
    avatar = Image.open(BytesIO(url.content))	
    avatar = avatar.resize((130, 130));	
    bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)	
    mask = Image.new('L', bigsize, 0)	
    draw = ImageDraw.Draw(mask)	
    draw.ellipse((0, 0) + bigsize, fill=255)	
    mask = mask.resize(avatar.size, Image.ANTIALIAS)	
    avatar.putalpha(mask)	

    output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))	
    output.putalpha(mask)	
    output.save('avatar.PNG')	

    # avatar = Image.open('avatar.png')	
    fundo = Image.open('bemvindo.png')	
    fonte = ImageFont.truetype('BebasNeue.ttf', 70)	
    escrever = ImageDraw.Draw(fundo)	
    escrever.text(xy=(180, 164), text=member.name, fill=(0, 0, 0), font=fonte)	
    fundo.paste(avatar, (40, 90), avatar)	
    fundo.save('bv.png')	

    await client.send_file(channel, 'bv.png')	


@client.event	
async def on_member_remove(member):	
    canal = client.get_channel("467782032374759426")	
    msg = "Adeus garotinho juvenil {}".format(member.mention)	
    await client.send_message(canal, msg)	


@client.event	
async def on_ready():	
    global current_channel	
    global voice	

    await client.change_presence(game=discord.Game(name="e Programando", type=1))	

    for server in client.servers:	
        for channel in server.channels:	
            if channel.id == '154048253174743041':	
                current_channel = channel	
                voice = await client.join_voice_channel(current_channel)	


@client.event	
async def on_message(message):	

    if message.content.lower().startswith("!linguagens"):	
        embed = discord.Embed(title="Lista de linguagens disponíveis:",	
                              description="\n Python \n Ruby \n Perl  \n Node.Js \n Java \n C \n C++ \n CSharp \n HTML \n CSS \n HTML5 \n CSS3 \n JavaScript \n JQuary \n PHP \n SQL \n WhiteHat \n BlackHat \n GrayHat \n Carder \n Visual Basic \n .NET",	
                              color=0x0a00ff)	
        embed.set_footer(text="Para adiciona da !add e o Linguagen")	
        await client.send_message(message.channel, embed=embed)	

    if message.content.lower().startswith('!addpython'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='Python')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo Python foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!addruby'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='Ruby')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo Ruby foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!addperl '):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='Perl ')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo Perl  foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!addPython'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='Node.Js')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo Node.Js foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!addperllua'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='Perl LUA')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo Perl LUA foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!node.js'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='node.js')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo node.js foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!addhtml'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='HTML')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo HTML foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!addcss'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='CSS')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo Sql foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!addhtml5'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='HTML5')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo HTML5 foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!addcss3'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='CSS3')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo CSS3 foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!addjavascript'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='JavaScript')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo JavaScript foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!addsql'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='SQL')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo SQL foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

    if message.content.lower().startswith('!addphp'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='PHP')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo PHP foi adicionado no usuário {}'.format(user.mention, message.author.mention))	


    if message.content.lower().startswith('!addjquary'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='JQuary')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo JQuary foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

        if message.content.lower().startswith('!addwhitehat'):	
            try:	
                user = message.mentions[0]	
            except IndexError:	
                user = message.author	

        cargo = discord.utils.get(message.server.roles, name='WhiteHat')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo WhiteHat foi adicionado no usuário {}'.format(user.mention,	
                                                                                                           message.author.mention))	

    if message.content.lower().startswith('!addgrayhat'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='GrayHat')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo GrayHat foi adicionado no usuário {}'.format(user.mention,	
                                                                                                           message.author.mention))	
    if message.content.lower().startswith('!addcarder'):	
        try:	
            user = message.mentions[0]	
        except IndexError:	
            user = message.author	

        cargo = discord.utils.get(message.server.roles, name='Carder')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo Carder foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

        if message.content.lower().startswith('!addvisualbasic'):	
            try:	
                user = message.mentions[0]	
            except IndexError:	
                user = message.author	

        cargo = discord.utils.get(message.server.roles, name='Visual Basic')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo Visual Basic foi adicionado no usuário {}'.format(user.mention, message.author.mention))	

        if message.content.lower().startswith('!add.net'):	
            try:	
                user = message.mentions[0]	
            except IndexError:	
                user = message.author	

        cargo = discord.utils.get(message.server.roles, name='.NET')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel, ' {}, o cargo .NET foi adicionado no usuário {}'.format(user.mention, message.author.mention))	


    if message.content.lower().startswith("!aviso"):	
        try:	
            user = message.author	
            msg = message.content[7:]	

            await client.delete_message(message)	
            embed = discord.Embed(	
                title=":loudspeaker: AVISO :loudspeaker:",	
                description="{}".format(msg),	
                color=0x1CF9FF	
            )	
            embed.set_footer(	
                text="Enviado por: " + user.name,	
                icon_url=user.avatar_url	
            )	

            await client.send_message(message.channel, embed=embed)	
        finally:	
            pass	

    if message.channel == client.get_channel('470734475811225610'):	
        await client.add_reaction(message, "👍")	
        await client.add_reaction(message, "👎")	
        await client.add_reaction(message, "💩")	


    if message.content.lower().startswith('!clear'):	
        if not message.author.server_permissions.manage_messages:	
            return await client.send_message(message.channel,	
                                             "**Você não tem permissão para executar esse comando SATANÁS!!! !**")	
        try:	
            limite = int(message.content[9:]) + 1	
            await client.purge_from(message.channel)	
            await client.send_message(message.channel, ' mensagens foram deletadas com sucesso ,por {}'.format(limite,	
                                                                                                               message.author.mention))	
        except:	
            await client.send_message(message.channel, 'Eu não tenho permissão para apagar mensagens nesse servidor.')	

    if message.content.lower().startswith('!avatar'):	
        avatarembed = discord.Embed(	
            title="",	
            color=0x004aff,	
            description="[Clique aqui](" + message.author.avatar_url + ") para acessar o link de seu avatar!"	
        )	
        avatarembed.set_author(name=message.author.name)	
        avatarembed.set_image(url=message.author.avatar_url)	
        await client.send_message(message.channel, embed=avatarembed)	

    if message.content.lower().startswith("!mute"):	
        # vai verificar se quem usou o comando possui permissão de adm	
        if not message.author.server_permissions.administrator:	
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')	
        author = message.author.mention	
        user = message.mentions[0]	
        """Lembrando que tem que ter o cargo mutado no seu server"""	
        """Lembrando que vc tem que retirar todas permissões do cargo mutado"""	
        cargo = discord.utils.get(message.author.server.roles, name='mutado')	
        await client.add_roles(user, cargo)	
        await client.send_message(message.channel,	
                                  'O membro: {} foi mutado pelo Administrador: {}'.format(user.mention, author))	

    if message.content.lower().startswith("!desmultar"):	
        # vai verificar se quem usou o comando possui permissão de adm	
        if not message.author.server_permissions.administrator:	
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')	
        author = message.author.mention	
        user = message.mentions[0]	
        """Lembrando que tem que ter o cargo mutado no seu server"""	
        cargo = discord.utils.get(message.author.server.roles, name='mutado')	
        await client.remove_roles(user, cargo)	
        await client.send_message(message.channel,	
                                  'O membro: {} foi Desmultado pelo Administrador: {}'.format(user.mention, author))	

    if message.content.lower().startswith('!ajuda'):	
        try:	
            await client.send_message(message.channel, ">> Enviei meus comandos no Dm!")	
            embedhelp = discord.Embed(	
                title=None,	
                color=0x1CF9FF,	
                description=None)	
            embedhelp.set_thumbnail(url="")	
            embedhelp.add_field(name='**COMANDOS**',	
                                value='📜 \n *!linguagens \n *!serverinfo \n *!botinfo \n *!musicaon \n *!musicaoff \n *!avatar \n *!ajuda \n *!cursos \n !convite \n *!votar \n_EM BREVE MAIS_',	
                                inline=True)	
            embedhelp.add_field(name='**TOTAL**', value='`6 COMANDOS`', inline=False)	
            embedhelp.add_field(name='**SOBRE**',	
                                value='`Sou apenas um simples bot para discord\nCriado pelo pelo Adriel\nVersão: 0.1`',	
                                inline=False)	
            embedhelp.set_footer(	
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),	
                icon_url=message.author.avatar_url)	
            rr = await client.send_message(message.author, embed=embedhelp)	
            await client.add_reaction(rr, '📜')	
            await client.add_reaction(rr, '🔐')	
            await client.add_reaction(rr, '🔍')	
            await client.add_reaction(rr, '🎉')	
            await client.add_reaction(rr, '📖')	
            await client.add_reaction(rr, '⚙')	

            global msg_id	
            msg_id = rr.id	
            global msg_user	
            msg_user = message.author	
        except:	
            await client.send_message(message.channel, '>> Seu DM está desativado!')	

    if message.content.startswith("!kick"):	
        if not message.author.server_permissions.kick_members:	
            return await client.send_message(message.channel,	
                                             "**Você não tem permissão para executar esse comando bobinho(a)!**")	
        try:	
            user = message.mentions[0]	
            await client.send_message(message.channel,	
                                      "**O usuario(a) <@{}> foi kickado com sucesso do servidor.**".format(user.id))	
            await client.kick(user)	
        except:	
            await client.send_message(message.channel, "**Você deve especificar um usuario para kickar!**")	

    if message.content.startswith('!musicaon'):	
        try:	
            canal = message.author.voice.voice_channel	
            await client.join_voice_channel(canal)	
        except discord.errors.InvalidArgument:	
            await client.send_message(message.channel, "```Você precisa esta conectado a um canal de voz!```")	

        if message.content.startswith('!musicaoff'):	
            try:	
                canaldevoz = client.voice_client_in(message.server)	
                await canaldevoz.disconnect()	
            except AttributeError:	
                await client.send_message(message.channel, "O bot não esta conectado em nenhum canal de voz!")	

    elif message.content.lower().startswith("!ban"):	
        # await client.delete_message(message)	
        try:	

            if not message.author.server_permissions.administrator:	
                return await client.send_message(message.channel, '⚠️Permissão insuficiente')	
            author = message.author.mention	
            user = message.mentions[0]	
            await client.ban(user)	
            await client.send_message(message.channel,	
                                      "Usuario: {} banido do server pelo Administrador: {}".format(user.mention,	
                                                                                                   author))	
        except  discord.errors.Forbidden:	
            return await client.send_message(message.channel,	
                                             '⚠️ Nao posso banir o administrador :{}'.format(user.mention))	

    if message.content.lower().startswith('!cursos'):	
        embed = discord.Embed(title="cursos",	
                              description=" Curso Completo de HTML5 (42 aulas)\n https://goo.gl/wmNpMp \n Curso Aprenda HTM(22aulas)\n https://goo.gl/j9qAkI \n Curso completo de CSS3 (22 aulas) \n https://goo.gl/Vt86Jz \n Curso Básico de CSS (12 aulas) \n https://goo.gl/Vt86Jz \n Curso de Bootstrap (16 aulas) \nhttps://goo.gl/etyOd5 \nCurso de Less (6 aulas) \n https://goo.gl/A4JiqE \nCurso de Sass (18 aulas)(inglês) \n https://goo.gl/iykixV \n Curso de CSS3 com Sass e Compass (9 aulas) \n https://goo.gl/dqlya3 \n Curso completo de Javascript (46 aulas) \n https://goo.gl/ejyvXS \n Curso Completo de jQuery (56 aulas) \n https://goo.gl/kSOZC7 \n Curso de Angular (17 aulas) \n https://goo.gl/C9XHch \n Curso de Angular 2 (56 aulas) \n https://goo.gl/JmTqv9 \n Curso Básico de PHP (20 aulas) \n https://goo.gl/DDygB3 \n Curso Completo de PHP (108 aulas) \n https://goo.gl/bacNLk \n Curso de NodeJS (21 aulas) \n https://goo.gl/LIru11 \n Curso de Aplicações Web Ricas com ExtJS (44 aulas) \n https://goo.gl/CbbU3p \n Curso de Ruby (15 aulas) \n https://goo.gl/NO4EQC \n Curso de Ruby On Rails (49 aulas) \n https://goo.gl/zc5tfa \n Curso de Gulp (11 aulas)(inglês) \n https://goo.gl/Gcfxzn \n Curso de Grunt (16 aulas)(inglês) \n https://goo.gl/EL8156  \n Curso de Laravel (23 aulas) \n https://goo.gl/dni1CO \n Curso de CodeIgniter (12 aulas) \n https://goo.gl/iH6JDS \n The Cracker technology: \n https://mega.nz/#F!LvhxjK6Y!63aAgq22jy6YSqgjV1ydTQ```",	
                              color=0x004aff)	
        await client.send_message(message.channel, embed=embed)	

    if message.content.lower().startswith('!comandos'):	
        embed = discord.Embed(title="Comandos",	
                              description="*!linguagens \n  *!serverinfo \n !botinfo \n *!musicaon \n *!musicaoff \n *!avatar \n *!ajuda \n *!cursos \n *!convite \n *!votar \n  _EM BREVE MAIS__",	
                              color=0x004aff)	
        await client.send_message(message.channel, embed=embed)	

    if message.content.startswith('!serverinfo'):	
        user = message.author.name	

        horario = datetime.datetime.now().strftime("%H:%M:%S")	

        serverinfo_embed = discord.Embed(title="\n", description="Informaçoes principais do servidor!",	
                                         color=0x004aff)	
        serverinfo_embed.set_thumbnail(url=message.server.icon_url)	
        serverinfo_embed.set_footer(text="{} • {}".format(user, horario))	
        serverinfo_embed.add_field(name="Nome:", value=message.server.name, inline=True)	
        serverinfo_embed.add_field(name="Dono:", value=message.server.owner.mention)	
        serverinfo_embed.add_field(name="ID:", value=message.server.id, inline=True)	
        serverinfo_embed.add_field(name="Cargos:", value=len(message.server.roles), inline=True)	
        serverinfo_embed.add_field(name="Canais de texto:", value=len(	
            [message.channel.mention for channel in message.server.channels if	
             channel.type == discord.ChannelType.text]), inline=True)	
        serverinfo_embed.add_field(name="Canais de voz:", value=len(	
            [message.channel.mention for channel in message.server.channels if	
             channel.type == discord.ChannelType.voice]), inline=True)	
        serverinfo_embed.add_field(name="Membros:", value=len(message.server.members), inline=True)	
        serverinfo_embed.add_field(name="Bots:",	
                                   value=len([user.mention for user in message.server.members if user.bot]),	
                                   inline=True)	
        serverinfo_embed.add_field(name="Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"),	
                                   inline=True)	
        serverinfo_embed.add_field(name="Região:", value=str(message.server.region).title(), inline=True)	
        await client.send_message(message.channel, embed=serverinfo_embed)	

    if message.content.lower().startswith('!clear'):	
        if not message.author.server_permissions.manage_messages:	
            return  await client.send_message(message.channel,	
                                             "**Você não tem permissão para executar esse comando SATANÁS!!! !**")	
        try:	
            limite = int(message.content[9:]) + 1	
            await client.purge_from(message.channel, limit=limite)	
            await client.send_message(message.channel, '{} mensagens foram deletadas com sucesso ,por {}'.format(limite,	
                                                                                                                 message.author.mention))	
        except:	
            await client.send_message(message.channel, 'Eu não tenho permissão para apagar mensagens nesse servidor.')	

    if message.content.startswith("!convite"):	
        # await client.delete_message(message)	

        temp = await client.send_message(message.author,	
                                         "<:sesho:433317803328536576> Convite criado " + message.content[8:] + ".")	
        try:	
            invite = await client.create_invite(message.channel, max_uses=2, temporary=True, xkcd=True)	
            await client.edit_message(temp, "<:sesho:433317803328536576> Convite criado  " + message.content[11:] + str(	
                invite))	
        except:	
            await client.edit_message(temp, ":no_entry: Falha ao criar convite.")	

    if message.content.lower().startswith('!votar'):	
        await client.delete_message(message)	
        try:	
            msg = message.content[7:]	
            embedvote = discord.Embed(	
                title="**VOTAÇÃO**"	
                , color=0x1CF9FF, description=None	
            )	
            embedvote.set_thumbnail(url=message.author.avatar_url)	
            embedvote.add_field(name='`📝 Votação iniciada por:`', value=message.author.mention, inline=False)	
            embedvote.add_field(name='`🖋 Titulo:`', value="{}".format(msg), inline=False)	
            await client.send_typing(message.channel)	
            gg = await client.send_message(message.channel, embed=embedvote)	
            await client.add_reaction(gg, '✔')	
            await client.add_reaction(gg, '❌')	
        except discord.errors.HTTPException:	
            await client.send_message(message.channel, "Insira um texto para iniciar a votação")	

    if message.content.lower().startswith('!botinfo'):	
        #  await client.delete_message(message)	

        embedbot = discord.Embed(	
            title='*>> Info do Bot <<',	
            color=0x004aff,	
            description='\n'	
        )	
        embedbot.set_thumbnail(url="")	
        embedbot.add_field(name='`💮 | Nome`', value=client.user.name, inline=True)	
        embedbot.add_field(name='`◼ | Id bot`', value=client.user.id, inline=True)	
        embedbot.add_field(name='💠 | Criado em', value=client.user.created_at.strftime("%d %b %Y %H:%M"))	
        embedbot.add_field(name='📛 | Tag', value=client.user)	
        embedbot.add_field(name='‍💻 | Servidores', value=len(client.servers))	
        embedbot.add_field(name='👥 | Usuarios', value=len(list(client.get_all_members())))	
        embedbot.add_field(name='‍⚙️ | Programador', value="`Adriel`")	
        embedbot.add_field(name='<:python:443164241927864359> | Version', value="`3.6.4`")	
        embedbot.set_footer(	
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),	
            icon_url=message.author.avatar_url)	

        await client.send_message(message.channel, embed=embedbot)	


client.run(TOKEN)