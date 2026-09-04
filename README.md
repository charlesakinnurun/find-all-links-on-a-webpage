# 🌡️ Temperature Readings Visualizer

A simple Python project that uses **Selenium** to launch Google Chrome and dynamically generate a webpage displaying temperature readings for multiple days.

Each temperature is represented using an HTML `<progress>` bar, making it easy to visually compare the readings against a maximum temperature of **40°C**.

## 🚀 Features

* 🌡️ Displays temperature readings for multiple days
* 📊 Uses HTML `<progress>` elements for visualization
* 🐍 Built with Python
* 🌐 Uses Selenium to control Google Chrome
* ⚡ Generates the webpage dynamically without requiring a separate HTML file
* ⏱️ Automatically closes the browser after 5 seconds

## 🛠️ Technologies Used

* **Python**
* **Selenium**
* **Google Chrome**
* **HTML5**
* **CSS**

## 📋 Temperature Data

The project visualizes the following readings:

| Day   | Temperature |
| ----- | ----------: |
| Day 1 |        22°C |
| Day 2 |        28°C |
| Day 3 |        25°C |
| Day 4 |        31°C |
| Day 5 |        27°C |

The progress bars use **40°C as the maximum value**.

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/temperature-readings-visualizer.git
cd temperature-readings-visualizer
```

### 2. Install Selenium

```bash
pip install selenium
```

### 3. Install Google Chrome

Make sure Google Chrome is installed on your computer.

Recent Selenium versions can generally manage the appropriate Chrome driver automatically.

## ▶️ Usage

Run the Python script:

```bash
python temperature.py
```

Chrome will open and display the generated temperature visualization.

The browser will remain open for approximately **5 seconds** before automatically closing.

## 💡 How It Works

The temperature readings are stored in a Python list:

```python
temps = [22, 28, 25, 31, 27]
```

The program then loops through the readings using `enumerate()`:

```python
for i, temp in enumerate(temps, 1):
```

For every temperature, an HTML `<progress>` element is generated:

```html
<progress value="28" max="40"></progress>
```

Finally, Selenium loads the generated HTML directly in Chrome using a `data:` URL:

```python
driver.get("data:text/html," + html)
```

This creates a lightweight browser-based visualization without needing to create a separate HTML file.

## 📊 Example Output

The browser displays a structure similar to:

```text
Temperature Readings

Day 1  ██████████████████  22°C
Day 2  ███████████████████████  28°C
Day 3  ████████████████████  25°C
Day 4  █████████████████████████  31°C
Day 5  █████████████████████  27°C
```

## 🎯 Learning Objectives

This project demonstrates:

* Python lists
* `for` loops
* `enumerate()`
* String formatting with f-strings
* Dynamic HTML generation
* HTML `<progress>` elements
* Basic CSS styling
* Selenium WebDriver
* Browser automation
* Loading dynamically generated HTML

## 🔧 Possible Improvements

Future versions could include:

* 📈 Interactive temperature charts
* 🎨 Color-coded temperature levels
* 📅 Real dates instead of day numbers
* 📊 Average, minimum, and maximum temperatures
* 🌡️ Celsius/Fahrenheit conversion
* 💾 Exporting readings to CSV
* 🖥️ A more polished dashboard interface
* 🔄 Loading temperature data from an external source

## 📄 License

This project is open source and available under the **MIT License**.
