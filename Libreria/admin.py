from django.contrib import admin
from .models import Editorial, Libro


def formato_pesos_chilenos(monto):
    return f"${monto:,.0f}".replace(",", ".")


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais", "correo", "monto_en_pesos")
    list_filter = ("pais",)
    search_fields = ("nombre", "pais", "correo")
    ordering = ("nombre",)

    @admin.display(description="Monto (CLP)", ordering="monto")
    def monto_en_pesos(self, obj):
        return formato_pesos_chilenos(obj.monto)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "isbn", "editorial", "precio_en_pesos")
    list_filter = ("editorial",)
    search_fields = ("titulo", "autor", "isbn", "editorial__nombre")
    ordering = ("titulo",)
    list_select_related = ("editorial",)

    @admin.display(description="Precio (CLP)", ordering="precio")
    def precio_en_pesos(self, obj):
        return formato_pesos_chilenos(obj.precio)
