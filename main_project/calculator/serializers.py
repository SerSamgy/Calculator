from rest_framework import serializers
from models import Solver

class SolverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solver
        fields = ('id', 'expression', 'result')

    def create(self, validated_data):
        """
        Create and return a new `Solver` instance, given the validated data.
        """
        return Solver.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Solver` instance, given the validated data.
        """
        instance.expression = validated_data.get('expression', instance.expression)
        instance.result = validated_data.get('result', instance.result)
        instance.save()
        return instance