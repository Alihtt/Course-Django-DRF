from rest_framework import serializers


def clean_email(data):
    if 'admin' in data.lower():
        raise serializers.ValidationError('email cant be `admin`')
    else:
        return data


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password = serializers.CharField(required=True, write_only=True)
    password_confirm = serializers.CharField(required=True, write_only=True)

    def validate_username(self, data):
        if data.lower() == 'admin':
            raise serializers.ValidationError('Username cant be `admin`')
        else:
            return data

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Passwords must match')
        else:
            return data
