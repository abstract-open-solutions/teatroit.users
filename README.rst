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

* creazione content rule custom basata su collective.contentrules.mailtogroup

* configurazione automatica della content rule (disabilitata). Nota bene: cambiare mittente mail ed evitare modifiche
  TTW alla regola (tenere allineato il codice!)

* analisi login sociali su google doc condiviso

Tests
-----
How to test::

    ./bin/test -m teatroit.user

