from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DocumentSerializer, Document


@api_view(['GET'])
def pending_list(request):
    return Response(DocumentSerializer(Document.objects.all(), many=True).data)


@api_view(['POST'])
def send(request):
    pass
