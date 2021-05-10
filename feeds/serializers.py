from rest_framework import serializers
class EmployeeSerilizer(serializers.Serializer):
    employee_number = serializers.IntegerField()
    employee_name = serializers.CharField(max_length=30)
    employee_salary = serializers.FloatField()
