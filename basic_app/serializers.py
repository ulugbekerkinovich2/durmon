import requests
from rest_framework import serializers

from basic_app import models

API_TOKEN = '5352054350:AAEU5Jd2rTODHvxIAfzPtWrSAee6WMgI9A0'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = "__all__"

    def create(self, validated_data):
        object = models.Contact.objects.create(**validated_data)
        print(object)
        chats = [935920479, -100602275265]
        for i in chats:
            requests.get(
                url=f"https://api.telegram.org/bot5352054350:AAEU5Jd2rTODHvxIAfzPtWrSAee6WMgI9A0/sendMessage?chat_id={i}&parse_mode=HTML&text={object}")

            return object
