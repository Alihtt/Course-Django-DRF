from rest_framework import relations


class UserEmailNameReletionalField(relations.RelatedField):
    def to_representation(self, value):
        return f'{value.username} - {value.email}'
