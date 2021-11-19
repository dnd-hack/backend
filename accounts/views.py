import random


from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from accounts.models import User
from accounts.serializers import RegisterUserSerializer
from hack_dnd.data.nick import nick_dict


def make_nick():
    while(True):
        nickname = nick_dict[random.randrange(0, 27)] + str(random.randrange(10000,100000))
        try :
            user = User.objects.get(nickname=nickname)
            if (user):
                continue
            else :
                return nickname
        except:
            return nickname

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_id = request.data['user_id']
        user = User.objects.filter(user_id=user_id)
        if (user):
            return Response({"error": "id_exists"})
        password = request.data['password']
        if (password):
            nickname = make_nick()
            newuser = User.objects.create(user_id=user_id,
                                          password=password,
                                          username=nickname)
            return Response({"nickname": newuser.username})

class IsIDExist(APIView):

    def post(self, request):
        id = request.data['id']
        try:
            user = User.objects.get(user_id=id)
            if (user):
                return Response({"result": True})
            else :
                return Response({"result": False})
        except:
            return Response({"result": False})