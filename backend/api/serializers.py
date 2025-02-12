from rest_framework import serializers
from .models import Product, Category, User

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_category(self, value):
        if not Category.objects.filter(pk=value.id).exists():
            raise serializers.ValidationError("Invalid category ID. Please provide a valid category.")
        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only':True}}
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
            is_admin=validated_data.get('is_admin', False)
        )
        user.password = validated_data['password']
        user.save()
        return user
    
    
    