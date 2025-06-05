import unittest
from src.app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Crea un cliente de prueba usando la aplicación Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Envía una solicitud GET a la ruta '/'
        result = self.app.get('/')
        
        # Verifica que la respuesta sea "Hello, World!"
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Hello, World!")

    def test_par_impar(self):
        # Envía una solicitud GET a la ruta '/par-impar'
        result = self.app.get('/par-impar')

        # Verifica que la respuesta contenga "es par" o "es impar"
        self.assertEqual(result.status_code, 200)
        contenido = result.data.decode()
        self.assertTrue("nada" in contenido or "todo" in contenido)



if __name__ == "__main__":
    unittest.main()
