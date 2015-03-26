import re
from rest_framework import serializers
from models import Solver

m_digit_only = r'^-?\d+(?:.\d+)?$'
m_symbol_only = r'^[\/\+\-\*\=]$'
m_digit_symbol = r'^-?\d+(?:.\d+)?[\/\+\-\*\=]$'
m_expression = r'^-?\d+(?:.\d+)?[\/\+\-\*]\d+(?:.\d+)?$'

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
        # by default
        # instance.expression = validated_data.get('expression', instance.expression)
        # instance.result = validated_data.get('result', instance.result)

        old_expression = instance.expression
        new_expression = validated_data.get('expression', old_expression)
        new_result = validated_data.get('result', instance.result)

        if re.match(m_digit_only, new_expression):
            instance.expression = new_expression
            instance.result = new_result
        elif re.match(m_symbol_only, new_expression):  # symbol only in request
            if re.match(m_digit_only, old_expression):  # digit only in model
                if new_expression == "=":  # stay the same
                    instance.expression = old_expression
                    instance.result = new_result
                else:  # add symbol to digit in model
                    instance.expression = old_expression + new_expression
                    instance.result = new_result
            elif re.match(m_digit_symbol, old_expression):  # digit[symbol] in model
                if new_expression == "=":  # do model expression on itself
                    instance.result = new_result
                    instance.expression = eval(old_expression + new_result)
                else:
                    old_expression[-1] = new_expression
                    instance.expression = old_expression
                    instance.result = new_result
        elif re.match(m_digit_symbol, new_expression):  # digit[symbol] in request
            if re.match(m_digit_symbol, old_expression):  # digit[symbol] in model
                if new_expression[-1] == "=":  # if last symbol in request is "="
                    instance.expression = eval(old_expression + new_expression[:-1])
                    instance.result = instance.expression
                else:
                    instance.expression = str(eval(old_expression + new_expression[:-1])) + new_expression[-1]
                    instance.result = instance.expression[:-1]
            else:
                instance.expression = new_expression
                instance.result = new_expression[:-1]
        instance.save()
        return instance