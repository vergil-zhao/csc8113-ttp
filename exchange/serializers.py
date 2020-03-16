from hashlib import sha256

from rest_framework.serializers import ModelSerializer

from utils.signing import Key
from user.models import User

from .models import Document


class DocumentSerializer(ModelSerializer):

    def validate(self, attrs):
        attrs = super(DocumentSerializer).validate(attrs)

        self.validate_signature(attrs, True)

        if attrs.get('receiver') is not None:
            self.validate_signature(attrs, False)

        return attrs

    @staticmethod
    def validate_signature(attrs, sender=True):
        user_id = attrs.get('sender' if sender else 'receiver')
        user = User.objects.get(user_id=user_id)
        key = Key(public_key=user.public_key)

        file = attrs.get('document')
        content = file.read()

        key.verify(attrs.get('sig_sender' if sender else 'sig_receiver'), content)

    class Meta:
        model = Document
        fields = '__all__'
