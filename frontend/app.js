const form = document.getElementById('reserva-form');
const resumen = document.getElementById('resumen');
const eventoId = 'frontend-evento-xyz';

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const data = {
    cliente_email: document.getElementById('email').value,
    zona: document.getElementById('zona').value,
    cantidad: Number(document.getElementById('cantidad').value),
  };

  const response = await fetch(`http://localhost:8001/reservas/${eventoId}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    const error = await response.json();
    resumen.textContent = `Error: ${error.detail || response.statusText}`;
    return;
  }

  const resumenResponse = await fetch(`http://localhost:8001/reservas/${eventoId}/resumen`);
  const resumenData = await resumenResponse.json();
  resumen.textContent = `Total recaudado: ${resumenData.total_recaudado}`;
});
