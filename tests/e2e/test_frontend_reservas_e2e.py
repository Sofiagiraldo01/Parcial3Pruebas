from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_reserva_vip_muestra_total_formateado():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://localhost:4200/reservas")

    driver.find_element(By.CSS_SELECTOR, '[data-testid="input-email-cliente"]').send_keys("test@correo.com")
    driver.find_element(By.CSS_SELECTOR, '[data-testid="input-cantidad-asientos"]').send_keys("1")

    zona = driver.find_element(By.CSS_SELECTOR, '[data-testid="select-zona-evento"]')
    if zona.tag_name == "select":
        from selenium.webdriver.support.ui import Select

        Select(zona).select_by_value("VIP")
    else:
        zona.send_keys("VIP")

    driver.find_element(By.CSS_SELECTOR, '[data-testid="btn-confirmar-reserva"]').click()

    resumen = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="seccion-resumen-total"]'))
    )
    resumen_text = resumen.text

    assert "150.000" in resumen_text

    driver.quit()
