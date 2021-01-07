from rest_framework import serializers

from signup.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    profile_image = serializers.ImageField(use_url=True)

    class Meta:
        model = Person
        fields = ('email', 'name', 'password', 'profile_image')
        # fields = ('email', 'name', 'password')
