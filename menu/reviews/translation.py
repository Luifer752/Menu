from modeltranslation.translator import translator, TranslationOptions
from .models import Review


class ReviewTranslationOptions(TranslationOptions):
    fields = ("content",)


translator.register(Review, ReviewTranslationOptions)
