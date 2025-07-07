# 🌍 Global Student Migration Analysis

This project analyzes **global student migration trends** from 2019–2023 using data stored in a SQLite database.  
It explores insights such as:
- Top destination countries
- Top origin countries
- Most popular courses
- Main reasons for studying abroad
- Trends in enrollment over time

## 📂 Project Structure

```
📁 global_student_migration_project/
 ├── intstud.py             # Script to load CSV data into SQLite
 ├── analysis.py            # Script to query the DB and generate charts
 ├── global_student_migration.db   # SQLite database (created by intstud.py)
 ├── global_student_migration.csv  # Original dataset (example)
 ├── top5reason.png         # Example chart output
 └── README.md              # Project overview and instructions
```

---

## 📊 Insights Included

✔️ **Top 10 Destination Countries**  
✔️ **Top 10 Origin Countries**  
✔️ **Top 10 Courses of Enrollment**  
✔️ **Top 5 Reasons for Enrollment**  
✔️ **Migration Trend Over Years**

---

## ⚙️ How to Run This Project

1. **Clone this repository**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Install required Python packages**
   ```bash
   pip install pandas matplotlib
   ```

3. **Prepare the database**  
   - Place your CSV file (`global_student_migration.csv`) in the project folder.  
   - Run the `intstud.py` script to create and populate the SQLite database:
     ```bash
     python intstud.py
     ```

4. **Run the analysis**  
   - Run `analysis.py` to query the data and generate plots:
     ```bash
     python analysis.py
     ```
   - Charts will display in pop-up windows. You can also save them as `.png`.

---

## 📁 Example Data Format

Your CSV should look like this:

| origin_country | destination_country | course_name | enrollment_reason | year_of_enrollment |
|----------------|---------------------|--------------|-------------------|--------------------|
| India          | USA                 | Computer Science | Quality of Education | 2022 |
| Nigeria        | UK                  | Engineering      | Job Opportunities     | 2021 |
| ...            | ...                 | ...              | ...                   | ...  |

---

## 📌 Notes

- Ensure your CSV uses UTF-8 encoding.
- The SQLite database (`global_student_migration.db`) will be created in the same folder.
- All queries are run using `pandas` and `sqlite3`.

---

## 📣 Contributing

Pull requests are welcome! Feel free to open an issue if you spot bugs, want new insights, or have ideas for improvements.

---

## 📬 Contact

Created by **[Dayv-3]**  
📧 achenejedavid54@gmail.com

