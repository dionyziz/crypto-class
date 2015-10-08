from django.contrib import admin
from .models import Base64Quote, Rot13Quote, SubstitutionQuote

admin.site.register(Base64Quote)
admin.site.register(Rot13Quote)
admin.site.register(SubstitutionQuote)
