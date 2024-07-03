from django.contrib import admin
from .models import Category, Topping, Wrapper, IceCream


class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'wrapper',
        'category',
        'is_on_main',
        'is_published',
        'output_order'
    )
    list_editable = (
        'category',
        'is_on_main',
        'is_published'
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'category',
    )
    list_display_links = (
        'description',
        'title'
    )
    empty_value_display = 'Не задано'
    filter_horizontal = ('toppings',)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(IceCream, IceCreamAdmin)
