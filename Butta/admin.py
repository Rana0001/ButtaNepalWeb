from django.contrib import admin
from Butta.models import *
from django.utils.html import format_html


# Register your models here.


# admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(Contact_us)


class CustomerAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            '<img src="{}" width="60" height="60"/>'.format(object.customer_picture.url)
        )

    thumbnail.short_description = "User_Image"
    list_display = (
        "customer_id",
        "thumbnail",
        "customer_first",
        "customer_last",
        "email",
        "is_login",
    )
    list_display_links = ("customer_id", "thumbnail", "customer_first")
    list_editable = ("is_login",)
    search_fields = ("customer_first",)


admin.site.register(Customer, CustomerAdmin)


class ContactUsForm(admin.ModelAdmin):
    list_display = (
        "visitor_id",
        "visitor_name",
        "visitor_subject",
        "visitor_message",
    )
    list_display_links = ("visitor_id", "visitor_subject", "visitor_message")
    # list_editable = ("visitor_message")
    # search_fields = ("visitor_name")


admin.site.register(Contact_us, ContactUsForm)


class OrderForm(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            '<img src="{}" width="60" height="60"/>'.format(object.butta.url)
        )

    thumbnail.short_description = "Butta"
    list_display = (
        "order_id",
        "thumbnail",
        "fullname",
        "country_name",
        "email",
        "payment_method",
        "address",
    )
    list_display_links = ("thumbnail", "email")


admin.site.register(Order, OrderForm)
