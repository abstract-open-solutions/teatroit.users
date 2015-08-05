from plone.app.users.browser.personalpreferences import UserDataPanelAdapter
from Products.CMFPlone.utils import safe_unicode


class UserDataPanelAdapter(UserDataPanelAdapter):
    """ Registration adapter """

    def _getProperty(self, name):
        """ PlonePAS encodes all unicode coming from PropertySheets.
            Decode before sending to formlib. """
        value = self.context.getProperty(name, '')
        if value:
            return safe_unicode(value)
        return value

    def get_provincia(self):
        return self._getProperty('provincia')

    def set_provincia(self, value):
        if value is None:
            value = ''
        return self.context.setMemberProperties({'provincia': value})

    provincia = property(get_provincia, set_provincia)

    def get_comune(self):
        return self._getProperty('comune')

    def set_comune(self, value):
        if value is None:
            value = ''
        return self.context.setMemberProperties({'comune': value})

    comune = property(get_comune, set_comune)

    def get_cap(self):
        return self._getProperty('cap')

    def set_cap(self, value):
        if value is None:
            value = ''
        return self.context.setMemberProperties({'cap': value})

    cap = property(get_cap, set_cap)

    def get_telefono(self):
        return self._getProperty('telefono')

    def set_telefono(self, value):
        if value is None:
            value = ''
        return self.context.setMemberProperties({'telefono': value})

    telefono = property(get_telefono, set_telefono)

    def get_compagnia_tipo(self):
        return self._getProperty('compagnia_tipo')

    def set_compagnia_tipo(self, value):
        if value is None:
            value = ''
        return self.context.setMemberProperties({'compagnia_tipo': value})

    compagnia_tipo = property(get_compagnia_tipo, set_compagnia_tipo)

    def get_redazione_argomento(self):
        return self._getProperty('redazione_argomento')

    def set_redazione_argomento(self, value):
        if value is None:
            value = ''
        return self.context.setMemberProperties({'redazione_argomento': value})

    redazione_argomento = property(get_redazione_argomento,
                                   set_redazione_argomento)

    def get_redazione_regione_editoriale(self):
        return self._getProperty('redazione_regione_editoriale')

    def set_redazione_regione_editoriale(self, value):
        if value is None:
            value = ''
        return self.context.setMemberProperties(
            {'redazione_regione_editoriale': value})

    redazione_regione_editoriale = property(get_redazione_regione_editoriale,
                                            set_redazione_regione_editoriale)
