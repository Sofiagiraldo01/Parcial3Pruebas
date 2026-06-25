from src.database.models import ReservaDB
from sqlalchemy.orm import Session


class ReservasRepositorio:
    def __init__(self, db: Session):
        self.db = db

    def guardar_reserva(self, evento_id: str, cliente_email: str, zona: str, cantidad: int) -> ReservaDB:
        reserva = ReservaDB(
            evento_id=evento_id,
            cliente_email=cliente_email,
            zona=zona,
            cantidad=cantidad,
        )
        self.db.add(reserva)
        self.db.commit()
        self.db.refresh(reserva)
        return reserva

    def calcular_total_evento(self, evento_id: str) -> int:
        reservas = self.db.query(ReservaDB).filter_by(evento_id=evento_id).all()
        total = 0
        for reserva in reservas:
            if reserva.zona == "VIP":
                precio = 150000
            elif reserva.zona == "General":
                precio = 50000
            else:
                precio = 0
            total += precio * reserva.cantidad
        return total
