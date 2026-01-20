import csv

def read_csv(filename):
    rows = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows

def generate_report(rows):
    total = len(rows)

    report_lines = []
    report_lines.append("CSV Report Summary")
    report_lines.append("------------------")
    report_lines.append(f"Total records: {total}")
    report_lines.append("")

    report_lines.append("Sample Records (first 5 rows):")
    for r in rows[:5]:
        report_lines.append(f"- ID: {r.get('id')} | Title: {r.get('title')}")

    return "\n".join(report_lines)

def save_report(text):
    with open("report.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("✅ Report saved as report.txt")

if __name__ == "__main__":
    filename = "posts.csv"   # CSV file name
    data = read_csv(filename)
    report = generate_report(data)
    save_report(report)
