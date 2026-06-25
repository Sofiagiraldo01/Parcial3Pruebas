from src.database.models import ReservaDB


def test_crear_reserva_integra_api_y_bd(client_con_bd, db_session):
    payload = {
        "cliente_email": "test@correo.com",
        "zona": "VIP",
        "cantidad": 2,
    }

    response = client_con_bd.post("/reservas/concierto-2026", json=payload)

    assert response.status_code == 201

    reserva = db_session.query(ReservaDB).filter_by(cliente_email="test@correo.com").one_or_none()
    assert reserva is not None
    assert reserva.cliente_email == payload["cliente_email"]
