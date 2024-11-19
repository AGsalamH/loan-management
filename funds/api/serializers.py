from rest_framework import serializers
from funds.models import Fund


class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ('id', 'name', 'description', 'amount', 
                  'interest_rate', 'max_fund_amount', 'min_fund_amount',
                  'duration', 'initiated_by', 'assigned_to', 'status'
                )
