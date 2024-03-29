from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Bank)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    ordering = ("name",)


@admin.register(DocAnalyst)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    ordering = ("name",)


@admin.register(CreditAnalyst)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    ordering = ("name",)


@admin.register(Planner)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    ordering = ("name",)


@admin.register(BankManager)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    ordering = ("name",)


@admin.register(Client)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    ordering = ("name",)


@admin.register(Business)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    ordering = ("name",)


@admin.register(Process)
class defaultAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "client_status",
        "bank",
        "branch",
        "available_credit_f",
        "planner",
    )
    raw_id_fields = ("client",)
    search_fields = ("client__name",)
    list_filter = (
        "client_status",
        "bank",
        "credit_analyst",
        "created_at",
        "updated_at",
    )
    date_hierarchy = "created_at"
    ordering = ("client",)
