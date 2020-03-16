from hashlib import sha256
from base64 import b64encode, b64decode

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import DocumentSerializer, Document


@api_view(['GET'])
def pending_list(request):
    return Response(DocumentSerializer(Document.objects.all(), many=True).data)


@api_view(['POST'])
@parser_classes([MultiPartParser])
def send(request):
    serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        doc = serializer.save()

        # Read the whole file
        file = request.data.get('document')
        content = file.read()

        # Get the id in bytes of sender and receiver
        sender = b64decode(doc.sender)
        receiver = b64decode(doc.receiver)

        # Create unique session_id
        timestamp = str(int(doc.date_created.timestamp() * 1000))
        hash_value = sha256(sender + receiver + content + timestamp).digest()
        doc.session_id = b64encode(hash_value).decode('ascii')
        doc.save()

        return Response(DocumentSerializer(doc).data)

    return Response(serializer.errors, HTTP_400_BAD_REQUEST)
