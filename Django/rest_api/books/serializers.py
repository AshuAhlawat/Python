from rest_framework import serializers
from .models import Novel

class NovelSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(max_length=50)
    # name = serializers.CharField(max_length=50)
    # status = serializers.CharField(max_length=10)
    
    
    # def create(self,validated_data):
        
    #     return Novel.objects.create(validated_data)
    
    # def update(self,instance,validated_data):
        
    #     instance.title = validated_data.get('user',instance.user)
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.status = validated_data.get('status',instance.status)
    #     instance.save()
        
    #     return instance
    
    class Meta:
        model = Novel
        fields = '__all__'