from django.db.models import Sum, F
from django.utils import timezone
from django.utils.formats import number_format
from gain.models import Gain
from categories.models import Category
from task.models import Task
from status.models import Status
from outgoing.models import Outgoing



def get_result_metrics():
    total_price_gain = Gain.objects.count()
    total_price_outgoing = Outgoing.objects.count()
    total_profit = total_price_outgoing - total_price_gain

    return dict(
        total_price_gain=number_format(total_price_gain, decimal_pos=2, force_grouping=True),
        total_price_outgoing=number_format(total_price_outgoing, decimal_pos=2, force_grouping=True),
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
    )


def get_task_metrics():
    total_task = Task.objects.count()
    total_status = Status.objects.count()
    #total_profit = total_price_outgoing - total_price_gain

    return dict(
        total_task=number_format(total_task, force_grouping=True),
        total_status=number_format(total_status, force_grouping=True),
        #total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
    )


#def get_outgoing_metrics():
    #total_outgoing = Outgoing.objects.all()
    #total_products_sold = Outflow.objects.aggregate(
        #total_products_sold=Sum('quantity')
    #)['total_products_sold'] or 0
    #total_sales_value = sum(outflow.quantity * outflow.product.selling_price for outflow in Outflow.objects.all())
    #total_sales_cost = sum(outflow.quantity * outflow.product.cost_price for outflow in Outflow.objects.all())
    #total_sales_profit = total_sales_value - total_sales_cost

    #return dict(
        #total_sales=total_sales,
        #total_products_sold=total_products_sold,
        #total_sales_value=number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        #total_outgoing=number_format(total_outgoing, decimal_pos=2, force_grouping=True),
    #)

'''
def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_total = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            total_sales=Sum(F('product__selling_price') * F('quantity'))
        )['total_sales'] or 0
        values.append(float(sales_total))

    return dict(
        dates=dates,
        values=values,
    )


def get_daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = list()

    for date in dates:
        sales_quantity = Outflow.objects.filter(created_at__date=date).count()
        quantities.append(sales_quantity)

    return dict(
        dates=dates,
        values=quantities,
    )


def get_graphic_product_category_metric():
    categories = Category.objects.all()
    return {category.name: Product.objects.filter(category=category).count() for category in categories}


def get_graphic_product_brand_metric():
    brands = Brand.objects.all()
    return {brand.name: Product.objects.filter(brand=brand).count() for brand in brands}
    '''