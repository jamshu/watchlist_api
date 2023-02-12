from rest_framework import serializers
from watchlist_app.models import Watchlist


def check_name(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short")
    return value


class WatchlistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100,validators=[check_name])
    description = serializers.CharField(max_length=100)
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Watchlist.objects.create(**validated_data)

    def validate(self, validated_data):
        if validated_data['name'] == validated_data['description']:
            raise serializers.ValidationError("Name and description must not be same")
        return validated_data
    # def validate_name(self, value):
    #     if len(value) <2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
