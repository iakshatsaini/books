from rest_framework import serializers
from .models import bookList

#  do not add create or update method in model serializer to create or update the data


class bookListSerializers(serializers.ModelSerializer):
    #  for single field values read only perssion which is not update
    # bookName = serializers.CharField(read_only = True)
    # For validate the any field with function based 
    def start_with_desc(value):
        if value[0].lower() != 'd':
            raise serializers.ValidationError("Book description should be start with Desc: ")
    bookDescription = serializers.CharField(validators = [start_with_desc])
    class Meta:
        model = bookList
        #  for individual fields
        # fields = ['id', 'bookName', 'authorName', 'bookDescription']
        
        # for all fields
        fields = '__all__'
        
        # For multiple fields read only permission
        # read_only_fields = ['bookName', 'authorName']
        
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