from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from .config import (
    TIPO_COMPAGNIA_VOCAB,
    PROVINCIA_VOCAB,
    )


class ItemsVocab(object):

    def __init__(self, terms):
        self.TERMS = terms

    @property
    def terms(self):
        return self.TERMS

    def __call__(self, context):
        terms = [SimpleTerm(value, token, title) for value, token, title in self.terms]
        return SimpleVocabulary(terms)


compagnia_tipo_vocab = ItemsVocab(TIPO_COMPAGNIA_VOCAB)
provincia_vocab = ItemsVocab(PROVINCIA_VOCAB)
