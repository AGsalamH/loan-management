from rest_framework import serializers

from loans.models import Loan


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('id', 'name', 'description', 'amount', 
                  'interest_rate', 'max_loan_amount', 'min_loan_amount',
                  'duration', 'requested_by', 'assigned_to', 'status'
                )
