PROJECTNAME = 'teatroit.users'

GROUPS = (
   ('redattori', 'Redattori', []),   # ruolo Redattore
   ('caporedattori', 'Caporedattori', ('Reviewer',)),
   ('direttori', 'Direttori', ('Reviewer',)),
   ('compagnie', 'Compagnie', ('',)),  # ruolo Compagnia
   ('teatri', 'Teatri', ('')),  # ruolo Teatro
   )
