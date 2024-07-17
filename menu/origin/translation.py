from modeltranslation.translator import translator, TranslationOptions
from .models import Origin


class OriginTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Origin, OriginTranslationOptions)
