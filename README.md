# 🗺️ U.S. States Quiz Game

A fun, interactive educational game built with **Python**, **Turtle** graphics, and **Pandas**. Test your knowledge of U.S. geography by identifying all 50 states on a map.

---

## ✨ Features

* **Interactive Map:** Correct guesses appear instantly at their specific coordinates.
* **Real-time Scoring:** Track your progress with a dynamic counter.
* **Smart Exit:** Type **"Exit"** to quit and generate a `states_to_learn.csv` file containing the states you missed.
* **Data Driven:** State names and coordinates are managed via a CSV backend.

---

## 🛠️ Installation

Ensure you have Python installed, then install the required library:

```bash
pip install pandas

```

---

## 🚀 How to Play

1. Run the script: `python main.py`
2. Type a state name in the pop-up box (e.g., "Texas" or "texas").
3. **To Quit:** Type **"Exit"** to save your progress and see what you missed.
4. **To Win:** Correctly name all 50 states!

---

## 📁 Project Structure

* `main.py` - Core game logic.
* `50_states.csv` - Data file containing state names and (x, y) coordinates.
* `blank_states_img.gif` - The background map image.
* `states_to_learn.csv` - Generated list of states you need to practice.
