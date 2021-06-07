from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2
from pprint import PrettyPrinter
from telegram import ReplyKeyboardMarkup, KeyboardButton
from random import randint,choice
import settings
from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton


def play_random_number(user_number):

    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
      message = f'Ваше число {user_number}, мое число {bot_number}, вы выиграли'
    elif user_number == bot_number:
      message = f'Ваше число {user_number}, мое число {bot_number}, ничья'
    else:
      message = f'Ваше число {user_number}, мое число {bot_number}, Я ПОБЕДИЛ!'
    return message
       
def get_smile(user_data):

  if "emoji" not in user_data:
    smile = choice(settings.USER_EMOJI)
    return emojize(smile, use_aliases=True)
  return user_data['emoji']
    

def main_keyboard():
  return ReplyKeyboardMarkup([
    ['Я вызываю Шрека'],
    [KeyboardButton('Мои координаты', request_location=True)]    
    ])

def is_cat():
    stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())
    metadata = (('authorization', '831a1abb9f5e4a9db2beaa146d4a4d32'),)

    request = service_pb2.PostModelOutputsRequest(
        # This is the model ID of a publicly available General model. You may use any other public or custom model ID.
        model_id='aaa03c23b3724a16a56b629203edc62c',
        inputs=[
        resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url='images\cat1.jpg')))
        ])
    response = stub.PostModelOutputs(request, metadata=metadata)

    if response.status.code != status_code_pb2.SUCCESS:
        raise Exception("Request failed, status code: " + str(response.status.code))

    for concept in response.outputs[0].data.concepts:
        return('%12s: %.2f' % (concept.name, concept.value))    

if __name__ == "__main__":
    is_cat()
