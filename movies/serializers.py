from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor


#class MovieSerializer(serializers.Serializer):
#    title = serializers.CharField()
#    genre = serializers.PrimaryKeyRelatedField(
#        queryset=Genre.objects.all(),
#    )
#    release_date = serializers.DateField()
#    actors = serializers.PrimaryKeyRelatedField(
#        queryset=Actor.objects.all(),
#        many=True,
#    )
#    resume = serializers.CharField()

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        
    def get_rate(self, obj):
        return 5
        
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("Resumo não deve ser maior do que 200 caracteres.")
        return value
    
    def validate_resume(self, value):
        if len(value) < 200:
            raise serializers.ValidationError("O resumo deve ter pelo menos 20 caracteres.")
        return value  
    
    