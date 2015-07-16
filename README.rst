teatroit.users
==============

Utenti e ruoli.

NOTA IMPORTANTE:

* assicurati di aver configurato le opzioni MAIL sul pannello di controllo
  perchè Plone disabilita automaticamente il form register se mancano questi
  parametri

Cosa fa:

* initializzazione gruppi

* inizializzazione ruoli

* imposta autoregistrazione a true

* abilitazione captcha su join form

* una vista landing @@register con 3 differenti percorsi di registrazione (@@utente_register, @@teatro_register e @@compagnia_register)

* preferenze personali custom

* campo email aggiuntivo su gruppo (Email2)

TODO:

* setup content rules

* login sociali (fuori, da discutere)




Tests
-----
How to test::

    ./bin/test -m teatroit.user

