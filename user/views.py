from hashlib import sha256
from base64 import b64encode

from django.utils.timezone import now

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import UserSerializer, User


@api_view(['GET'])
def user_list(request):
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        # Create unique user id with name and a nano timestamp
        unique_str = user.name + str(int(now().timestamp() * 1000))
        user_id = b64encode(sha256(unique_str.encode()).digest()).decode('ascii')
        user.user_id = user_id
        user.save()

        return Response(UserSerializer(user).data)

    return Response(serializer.errors, HTTP_400_BAD_REQUEST)
