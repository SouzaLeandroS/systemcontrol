import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
#from ai.models import AIResult
from . import metrics


@login_required(login_url='login')
def home(request):

    result_metrics = metrics.get_result_metrics()
    #outgoing_metrics = metrics.get_outgoing_metrics()
    #profit_metrics = metrics.get_profit_metrics()
    task_metrics = metrics.get_task_metrics()
    #daily_sales_data = metrics.get_daily_sales_data()
    #daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    #graphic_product_category_metric = metrics.get_graphic_product_category_metric()
    #graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()

    context = {
        'result_metrics': result_metrics,
        'task_metrics' : task_metrics,
        #'sales_metrics': sales_metrics,
        #'daily_sales_data': json.dumps(daily_sales_data),
        #'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
        #'product_count_by_category': json.dumps(graphic_product_category_metric),
        #'product_count_by_brand': json.dumps(graphic_product_brand_metric),
    }

    return render(request, 'home.html', context)