from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['fam', 'name', 'otc', 'email', 'phone']
        def save(self, **kwargs):
            self.is_valid()
            user = Users.objects.filter(email=self.validated_data.get('email'))
            if user.exists():
                return user.first()
            else:
                return Users.objects.create(
                    email=self.validated_data.get('email'),
                    fam=self.validated_data.get('fam'),
                    name=self.validated_data.get('name'),
                    otc=self.validated_data.get('otc'),
                    phone=self.validated_data.get('phone'),
                )


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
    status = "new"
    user = UsersSerializer()
    coord = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True, required=False)

    class Meta:
        model = Perevals
        fields = ['beauty_title',
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
            coords = validated_data.pop('coords')
            level = validated_data.pop('level')
            images = validated_data.pop('images')
            pick_user = Users.objects.filter(email=user['email'])
            if pick_user.exists():
                user_serializer = UsersSerializer(data=user)
                user_serializer.is_valid(raise_exception=True)
                user = user_serializer.save()
            else:
                user = Users.objects.create(**user)

            coords = Coords.objects.create(**coords)
            level = Level.objects.create(**level)
            pereval = Perevals.objects.create(**validated_data, user=user, coords=coords, level=level, status='new')

            for image in images:
                data = image.pop('data')
                title = image.pop('title')
                Images.objects.create(data=date_added, pereval=pereval, title=title)

            return pereval



