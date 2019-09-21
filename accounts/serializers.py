from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate


class AuthTokenSerializer(serializers.Serializer):
    phone = serializers.CharField(label=_("Phone"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')

        if phone and password:
            user = authenticate(request=self.context.get('request'),
                                username=phone, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "phone" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('email', 'first_name', 'last_name', 'gender', 'birth_date', 'avatar', 'phone',)
        exclude = ('password', 'is_staff', 'groups', 'user_permissions', 'last_login', 'is_superuser')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'gender': {'required': True},
            'birth_date': {'required': True},
            # 'avatar'        : {'required': True},
        }

    def validate_birth_date(self, value):
        # bd = attrs.get('birth_date')
        if value >= date.today():
            raise ValidationError("Date is in the future.")

        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
