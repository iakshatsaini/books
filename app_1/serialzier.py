from rest_framework import serializers
from .models import bookList


# For validate the any field with function based 
def start_with_desc(value):
    if value[0].lower() != 'd':
        raise serializers.ValidationError("Book description should be start with Desc: ")
    
class bookListSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    bookName = serializers.CharField(max_length = 255)
    authorName = serializers.CharField(max_length = 255)
    bookDescription = serializers.CharField(max_length = 255, validators = [start_with_desc])
     
    
    def create(self, validated_data):
        return bookList.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # print("instance.bookName11: ",instance.bookName)
        instance.bookName = validated_data.get('bookName', instance.bookName)
        # print("instance.bookName22: ",instance.bookName)
        instance.authorName = validated_data.get('authorName', instance.authorName)
        instance.bookDescription = validated_data.get('bookDescription', instance.bookDescription)
        instance.save()
        return instance

    
    #  For field level validation
    
    def validate_id(self, value):
        if value >=10:
            raise serializers.ValidationError("Too much book inserted, Please delete")
        return value
    
    #  For object level validation for all data
    
    def validate(self, data):
        book = data.get("bookName")
        author = data.get("authorName")
        if book == 'Ram' and author == 'Amish':
            raise serializers.ValidationError("Book name already exist please check with another book.")
        return data