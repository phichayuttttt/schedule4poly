import discord
import datetime
from discord.ext import tasks

TOKEN = 'MTExMDAyMDg0MzI2Nzk2OTEzNQ.GCW-Fy.Zazlennv_e1g0LoDWT8P3RwGgorueDJL4d0Ddc'
CHANNEL_ID = '890283999111548968'

schedule = {
    0: {  # Monday
        "08:10": "**MONDAY** : คอม ไทยหลัก อังกฤษ(D) ไทยเสริม ชุมนุม",
        "08:15": "วิชา : __**Computer (T. นิโก้)**__",
        "09:55": "วิชา : __**Thai (T. กุ๊)**__",
        "10:45": "วิชา : __**English (T. ดีมี่)**__",
        "11:35": "**------ พักเที่ยง ------**",
        "12:25": "วิชา : __**Thai (T. อุทัยวรรณ)**__",
        "13:15": "วิชา : __**Club (ชุมนุม)**__",
        "14:10": "||:hatching_chick:**เรียนจบละวัยรุ่น**:hatching_chick:||",
    },
    1: {  # Tuesday
        "08:10": "**TUESDAY** : คณิตเพิ่ม(2) คณิตหลัก สุขศึกษา คอม(P) นาฏศิลป์",
        "08:15": "วิชา : __**Math (T. น้าม)**__ (2 คาบติด)",
        "09:05": "วิชา : __**Math (T. น้าม)**__ (2 คาบติด)",
        "09:55": "วิชา : __**Math (T. ปรวี)**__", 
        "10:45": "วิชา : __**Health (สุขศึกษา)**__",
        "11:35": "**------ พักเที่ยง ------**",
        "12:25": "วิชา : __**Computer (T. พงศกร)**__",
        "13:15": "วิชา : __**Dance (ดนตรีนาฏศิลป์)**__",
        "14:10": "||:hatching_chick:**เรียนจบละวัยรุ่น**:hatching_chick:||",
    },
    2: {  # Wednesday
        "08:10": "**WEDNESDAY** : แนะแนว สังคม คณิตเพิ่ม(2) อังกฤษ(A)",
        "08:15": "วิชา : __**แนะแนว**__",
        "09:05": "วิชา : __**Social (T. นฤเบศ)**__",
        "09:55": "วิชา : __**Math (T. น้าม)**__ (2 คาบติด)",
        "10:45": "วิชา : __**Math (T. น้าม)**__ (2 คาบติด)",
        "11:35": "**------ พักเที่ยง ------**",
        "12:25": "วิชา : __**English (T.Alan)**__",
        "13:20": "||:hatching_chick:**เรียนจบละวัยรุ่น**:hatching_chick:||",    
    },
    3: {  # Thursday
        "08:10": "**THURSDAY** : คณิตหลัก คณิตเสริม อังกฤษ(D) ไทยเพิ่ม ไทยหลัก อังกฤษ(L)",
        "08:15": "วิชา : __**Math (T. ปรวี)**__",
        "09:05": "วิชา : __**Math (T. น้าม)**__",
        "09:55": "วิชา : __**English (T.ดีมี่)**__",
        "10:45": "วิชา : __**Thai (T. อุทัยวรรณ)**__",
        "11:35": "**------ พักเที่ยง ------**",
        "12:25": "วิชา : __**Thai (T. กุ๊)**__",
        "13:15": "วิชา : __**English (T.Lee)**__",
        "14:10": "||:hatching_chick:**เรียนจบละวัยรุ่น**:hatching_chick:||",
    },
    4: {  # Friday
        "08:10": "**FRIDAY** : พละ ประวัติ อังกฤษ(A) สังคม อังกฤษ(L) ประชุมระดับ",
        "08:15": "วิชา : __**P.E. (พละ)**__",
        "09:05": "วิชา : __**History**__",
        "09:55": "วิชา : __**English (T.Alan)**__",
        "10:45": "วิชา : __**Social (T. นฤเบศ)**__",
        "11:35": "**------ พักเที่ยง ------**",
        "12:25": "วิชา : __**English (T.Lee)**__",
        "13:15": "วิชา : __**Conference (ประชุมระดับ)**__",
        "14:10": "||:hatching_chick:**เรียนจบละวัยรุ่น**:hatching_chick:||",        
    },
    # Add schedules for other days here
}

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Synchronizing status : Connected')
    send_message.start()

previous_message = ""

@tasks.loop(seconds=0)  # Decreased interval for testing purposes
async def send_message():
    global previous_message

    channel = client.get_channel(int(CHANNEL_ID))
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    weekday = now.weekday()

    if weekday in schedule and current_time in schedule[weekday]:
        message = f" {current_time}  |  {schedule[weekday][current_time]}"
        if message != previous_message:
            await channel.send(message)
            previous_message = message

client.run(TOKEN)
