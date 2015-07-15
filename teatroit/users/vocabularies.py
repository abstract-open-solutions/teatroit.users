from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from .config import TIPO_COMPAGNIA_VOCAB


class ItemsVocab(object):

    def __init__(self, terms):
        self.TERMS = terms

    @property
    def terms(self):
        return self.TERMS

    def __call__(self, context):
        terms = [SimpleTerm(value, token, title) for value, token, title in self.terms]
        return SimpleVocabulary(terms)


tipo_compagnia_vocab = ItemsVocab(TIPO_COMPAGNIA_VOCAB)
