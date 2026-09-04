from selenium import webdriver
import time

driver = webdriver.Chrome()
temps = [22, 28,25, 31,27]

html = "<h2> Temperature Readings</h2>"

for i, temp in enumerate(temps, 1):
    html += f"""
    <div style="margin:10px, font:18px Arial>
        Day {i}
        <progress value="{temp}" max="40"
                style="width:300px"; height:25px>
        </progress>
        {temp}°C
    </div>
    """

driver.get("data:text/html," + html)
time.sleep(5)
driver.quit()