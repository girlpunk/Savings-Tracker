import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import models

ACCOUNT_DEF = [
    {"text": "Starting Balance",    "type": "number"},
    {"text": "Current Balance",     "type": "number"},
    {"text": "Total Topup",         "type": "number"},
    {"text": "Average APR",         "type": "number"},
    {"text": "Returns",             "type": "number"},
    {"text": "Balance OK",          "type": "number"},
    {"text": "Name",                "type": "string"},
    {"text": "Bank Name",           "type": "string"},
    {"text": "Account Name",        "type": "string"},
    {"text": "Account Number",      "type": "string"},
    {"text": "Sort Code",           "type": "string"},
    {"text": "Predicted Interest",  "type": "number"},
    {"text": "Interest Min",        "type": "number"},
    {"text": "Interest Max",        "type": "number"},
    {"text": "Instant Withdrawal",  "type": "number"},
]


# Create your views here.
@csrf_exempt
def test():
    """Used by Grafana to test basic connectivity"""
    return JsonResponse("OK")


@csrf_exempt
def search(request):
    """Used by Grafana to find metrics"""
    return JsonResponse(["accounts", "balances"], safe=False)


@csrf_exempt
def query(request):
    response = []
    data = json.loads(request.body)
    for target in data["targets"]:
        if target["target"] == "accounts":
            if "pk" in target["data"]:
                account = models.Account.objects.get(pk=target["data"]["pk"])
                response.append({
                    "columns": ACCOUNT_DEF,
                    "rows": [
                        [
                            account.starting_balance.balance,
                            account.current_balance.balance,
                            account.total_topup,
                            account.average_APR,
                            account.returns,
                            account.balance_OK,
                            account.__str__(),
                            account.bank_name,
                            account.account_name,
                            account.account_number,
                            account.sort_code,
                            account.predicted_interest,
                            account.interest_min,
                            account.interest_max,
                            account.instant_withdrawal
                        ],
                    ],
                    "type": "table"
                })
            else:
                accounts = models.Account.objects.all()
                response.append({
                    "columns": ACCOUNT_DEF,
                    "rows": [
                        [[
                            account.starting_balance,
                            account.current_balance,
                            account.total_topup,
                            account.average_APR,
                            account.returns,
                            account.balance_OK,
                            account.__str__(),
                            account.bank_name,
                            account.account_name,
                            account.account_number,
                            account.sort_code,
                            account.predicted_interest,
                            account.interest_min,
                            account.interest_max,
                            account.instant_withdrawal
                        ] for account in accounts],
                    ],
                    "type": "table"
                })

    return JsonResponse(response, safe=False)


@csrf_exempt
def annotations(request):
    return JsonResponse([], safe=False)
