import httpx


def test_sistema_total_recaudado_e2e():
    base_url = "http://localhost:8001"
    evento_id = "sistema-evento-xyz"

    reserva_payload = {
        "cliente_email": "cliente@sistema.com",
        "zona": "General",
        "cantidad": 3,
    }

    post_response = httpx.post(f"{base_url}/reservas/{evento_id}", json=reserva_payload)
    assert post_response.status_code == 201

    resumen_response = httpx.get(f"{base_url}/reservas/{evento_id}/resumen")
    assert resumen_response.status_code == 200

    resumen_data = resumen_response.json()
    assert resumen_data["total_recaudado"] == 150000
