PROJECTNAME = 'teatroit.users'

GROUPS = (
   ('redattori', 'Redattori', ('Redattore',)),
   ('caporedattori', 'Caporedattori', ('Reviewer',)),
   ('direttori', 'Direttori', ('Reviewer',)),
   ('compagnie', 'Compagnie', ('Compagnia',)),
   ('teatri', 'Teatri', ('Teatro',)),
   )

TIPO_COMPAGNIA_VOCAB = (('compagnia-teatrale', 'compagnia-teatrale', 'Compagnia teatrale'),
                        ('associazione-culturale', 'associazione-culturale', 'Associazione culturale'),
                        ('scuola', 'scuola', 'Scuola'),
                        )
