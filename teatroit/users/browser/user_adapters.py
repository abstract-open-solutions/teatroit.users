from plone.app.users.browser.account import AccountPanelSchemaAdapter


class BaseUserDataPanelAdapter(AccountPanelSchemaAdapter):
    def _getProperty(self, name):
        """ PlonePAS encodes all unicode coming from PropertySheets.
            Decode before sending to formlib. """
        value = self.context.getProperty(name, '')
        if value:
            return safe_unicode(value)
        return value


class UtenteUserDataPanelAdapter(BaseUserDataPanelAdapter):

    def get_provincia(self):
        return self._getProperty('provincia')

    def set_provincia(self, value):
        if value is None:
            value = ''
        return self.context.setMemberProperties({'provincia': value})

    provincia = property(get_provincia, set_provincia)


class TeatroUserDataPanelAdapter(UtenteUserDataPanelAdapter):

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


class CompagniaUserDataPanelAdapter(BaseUserDataPanelAdapter):

    def get_tipo(self):
        return self._getProperty('tipo')

    def set_tipo(self, value):
        if value is None:
            value = ''
        return self.context.setMemberProperties({'tipo': value})

    tipo = property(get_tipo, set_tipo)
