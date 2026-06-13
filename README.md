# Student Performance Analyzer

A Python-based mini project that analyzes student performance using **Pandas** and **Matplotlib**. It calculates total marks, average marks, grades, and identifies top students and low-attendance students. Results are exported to a CSV file and visualized with a bar chart.

---

## Features

- Merges student info, subject marks, and attendance into a single DataFrame
- Calculates **total marks** and **average marks** per student
- Assigns **grades** (A / B / C / D / F) based on average marks
- Identifies **top-performing students** (average > 80)
- Flags students with **attendance below 75%**
- Generates a **bar chart** of average marks using Matplotlib
- Exports the final data to `student_data.csv`

---

## Project Structure

```
student-performance-analyzer/
├── student_performance.py   # Main analysis script
├── student_data.csv         # Output dataset with marks and attendance
└── README.md                # Project documentation
```

---

## Requirements

- Python 3.x
- pandas
- matplotlib

Install dependencies with:

```bash
pip install pandas matplotlib
```

---

## Setup & Usage

1. **Clone the repository**

```bash
git clone https://github.com/Ravi20051/student-performance-analyzer.git
cd student-performance-analyzer
```

2. **Install dependencies**

```bash
pip install pandas matplotlib
```

3. **Run the script**

```bash
python student_performance.py
```

4. **Output**

- Console output showing the full DataFrame, top students, and low-attendance students
- A bar chart displaying average marks per student
- A `student_data.csv` file saved in the same directory

---

## Grade Scale

| Grade | Average Marks |
|-------|--------------|
| A     | ≥ 90         |
| B     | 80 – 89      |
| C     | 70 – 79      |
| D     | 60 – 69      |
| F     | < 60         |

---

## Author

**Ravi** — [GitHub](https://github.com/Ravi20051)
