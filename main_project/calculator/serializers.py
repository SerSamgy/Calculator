import re
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
        sign = instance.expression[-1]
        if re.match(r'^[\/\+\-\*]$', sign):  # if last symbol in expression is mathematical symbol
            expression = instance.expression[:-1]  # get entire expression before symbol
            if re.match(r'^\d+(?:.\d+)?[\/\+\-\*]\d+(?:.\d+)?$', expression):  # if it matches 'digit[symbol]digit'
                result = eval(expression)  # calculate
                instance.expression = str(result) + sign
                instance.result = result
        instance.save()
        return instance