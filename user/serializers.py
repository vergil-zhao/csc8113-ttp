from rest_framework.serializers import ModelSerializer, CharField

from utils.signing import Key

from .models import User


class UserSerializer(ModelSerializer):

    signature = CharField(max_length=100, allow_null=False, allow_blank=False)

    def validate(self, attrs):
        super(UserSerializer).validate(attrs)

        name = attrs.get('name')
        public_key = attrs.get('public_key')
        signature = attrs.get('signature')

        key = Key(public_key=public_key)
        key.verify(signature, name.encode())

        return attrs

    class Meta:
        model = User
        fields = '__all__'

