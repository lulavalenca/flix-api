from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]

        if rate:
            return rate

        return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                "Resumo não deve ser maior do que 200 caracteres."
            )
        return value

    def validate_resume(self, value):
        if len(value) < 500:
            raise serializers.ValidationError(
                "O resumo deve ter pelo menos 20 caracteres."
            )
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
