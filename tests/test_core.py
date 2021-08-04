''' File di test '''
# Gli import si mettono in questo modo: prima la libreria standard di Python, poi pacchetti di terze parti (tipo numpy, scipy, matplotlib)
# ed infine i nostri separati da una riga, così è più chiaro.
import unittest
                                        # Per aggiungere la libreria al path per importarla eseguire nel cmd il comando:
from smartsquare.core import square     # set PYTHONPATH=C:\Users\cerra\Documents\GitHub\smartsquare

class TestCore(unittest.TestCase):     # I nomi delle classi si scrivono in Camel Case, ossia con le parole tutte attaccate e tutte le iniziali maiuscole
                                        # (diversamente da Snake Case, con tutte le parole minuscole e l'underscore per separarle, che si usa per i metodi); vedi PEP8

    def test_float(self):
        self.assertAlmostEqual(square(2.),4.)

if name__ == '__main':
    unittest.main()