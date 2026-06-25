from playwright.sync_api import sync_playwright


def test_reserva_vip_muestra_total_formateado():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("http://localhost:4200/reservas")

        page.fill('[data-testid="input-email-cliente"]', "test@correo.com")
        page.fill('[data-testid="select-zona-evento"]', "VIP")
        page.fill('[data-testid="input-cantidad-asientos"]', "1")

        page.click('[data-testid="btn-confirmar-reserva"]')

        resumen = page.wait_for_selector('[data-testid="seccion-resumen-total"]')
        resumen_text = resumen.text_content() or ""

        assert "150.000" in resumen_text

        browser.close()
