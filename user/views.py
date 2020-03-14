from hashlib import sha256
from base64 import b64encode

from django.utils.timezone import now

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from utils.ecdsa import Key

from .serializers import UserSerializer, User


@api_view(['GET'])
def user_list(request):
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register(request):
    name = request.data.get('name')
    public_key = request.data.get('public_key')
    signature = request.data.get('signature')
    
    key = Key(public_key=public_key)
    key.verify(signature, name.encode())

    unique_str = name + str(int(now().timestamp() * 1000))
    user_id = b64encode(sha256(unique_str.encode()).digest()).decode('ascii')
    
    serializer = UserSerializer(data={
        'name': name,
        'public_key': public_key,
        'user_id': user_id,
    })

    if serializer.is_valid():
        user = serializer.save()
        return Response(UserSerializer(user).data)

    return Response(serializer.errors, HTTP_400_BAD_REQUEST)
