from rest_framework import serializers
from models import Solver

class SolverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solver
        fields = ('cur_val', 'res_val', 'sign', 'result')

    def create(self, validated_data):
        """
        Create and return a new `Solver` instance, given the validated data.
        """
        return Solver.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Solver` instance, given the validated data.
        """
        instance.cur_val = validated_data.get('cur_val', instance.cur_val)
        instance.res_val = validated_data.get('res_val', instance.res_val)
        instance.sign = validated_data.get('sign', instance.sign)
        instance.result = validated_data.get('result', instance.result)
        instance.save()
        return instance