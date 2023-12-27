from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['fam', 'name', 'otc', 'email', 'phone']



class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['summer', 'autumn', 'winter', 'spring']


class ImagesSerializer(serializers.ModelSerializer):
    image = serializers.URLField()
    date_added = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Images
        fields = ['title', 'date_added', 'image']


class PerevalsSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    status = serializers.CharField(read_only=True)
    user = UsersSerializer()
    coord = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True, required=False)

    class Meta:
        model = Perevals
        fields = ['id',
                  'beauty_title',
                  'title',
                  'other_titles',
                  'connect',
                  'add_time',
                  'level',
                  'user',
                  'coord',
                  'images',
                  'status'
                  ]
    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        coords = validated_data.pop('coord')
        level = validated_data.pop('level')
        images = validated_data.pop('images')
        user, created = Users.objects.get_or_create(**user)
        coords = Coords.objects.create(**coords)
        level = Level.objects.create(**level)
        pereval = Perevals.objects.create(**validated_data, user=user, coord=coords, level=level, status='new')

        for im in images:
            image = im.pop('image')
            title = im.pop('title')
            Images.objects.create(image=image, pereval=pereval, title=title)

        return pereval
        
    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            validating_user_fields = [
                instance_user.fam != data_user['fam'],
                instance_user.name != data_user['name'],
                instance_user.otc != data_user['otc'],
                instance_user.phone != data_user['phone'],
                instance_user.email != data_user['email'],
            ]
            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError({'Данные пользователя не могут быть изменены'})
        return data


