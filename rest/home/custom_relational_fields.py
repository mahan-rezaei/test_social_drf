from rest_framework import serializers


class CustomUserRelationalFields(serializers.RelatedField):
    def to_representation(self, value):
        return value.email


# class CustomQuestionRelationalFields(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.title
