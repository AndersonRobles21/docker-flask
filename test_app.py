from sample_app import sample


def test_ruta_principal():
    cliente = sample.test_client()

    respuesta = cliente.get("/")

    if respuesta.status_code != 200:
        raise AssertionError(
            f"Se esperaba código 200, pero se recibió {respuesta.status_code}"
        )