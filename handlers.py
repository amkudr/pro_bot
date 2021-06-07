from datetime import datetime
import ephem
from glob import glob
import os
from random import choice
from utils import get_smile, main_keyboard, play_random_number



def greet_user(update, context):

  text = 'Вызван /start'  
  print(text)
  context.user_data['emoji'] = get_smile(context.user_data)  
  update.message.reply_text(
    f"Здарова, бандит {context.user_data['emoji']}",
    reply_markup = main_keyboard()
    )

def find_planet(update, context):

  text = update.message.text.split()
  if len(text) == 1:
    update.message.reply_text("Введите планету")      
  else:
    try:
      planet = text[1].lower().capitalize()        
      obj_planet = getattr(ephem, planet)
      print("Задана планета")
    except:
      update.message.reply_text("Введите настоящую планету после /planet",
    reply_markup = main_keyboard())    
    location = obj_planet(datetime.now().date())
    const = constellation(location)    
    update.message.reply_text(const)   

def guess_number(update, context):
  
    print(context.args)
    if context.args:
      try:
        user_number = int(context.args[0])
        message = play_random_number(user_number)
      except (TypeError,ValueError):
        message = "Введи те целое число"
    else:
      message = "Введите число"
    update.message.reply_text(message,
    reply_markup = main_keyboard())

 
def send_shrek_picture(update, context):

  shrek_photos_list = glob('images/shrek_*.jp*g')
  shrek_pic_filename = choice(shrek_photos_list)
  chat_id = update.effective_chat.id
  context.bot.send_photo(chat_id=chat_id, photo=open(shrek_pic_filename, "rb"))
 

def talk_to_me(update, context):

    user_text = update.message.text
    print(user_text)    
    context.user_data['emoji']= get_smile(context.user_data)
    update.message.reply_text(f"{user_text} {context.user_data['emoji']}",
    reply_markup = main_keyboard())


def user_coordinates(update, context):
  context.user_data['emoji'] = get_smile(context.user_data)
  coords = update.message.location
  update.message.reply_text(
    f"Ваши координаты {coords} {context.user_data['emoji']}",
    reply_markup = main_keyboard()
  )  


def check_user_photo(update,context):
    update.message.reply_text("Ваше фото обрабатывается")
    os.makedirs('downloads', exist_ok=True)
    user_photo = context.bot.getFile(update.message.photo[-1].file_id)
    file_name = os.path.join('downloads', f"{user_photo.file_id}.jpg")
    user_photo.download(file_name)
    update.message.reply_text("Фото загружено")