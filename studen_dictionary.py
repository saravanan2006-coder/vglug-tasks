students = {
    "guru" : { "department": "BE EEE", "year": 3, "marks": {"physics": 90,"Engineering maths": 85,"power systems": 80} },
    "ganesan": { "department": "BE ECE", "year": 3, "marks": {"physics": 80,"Engineering maths": 75,"power systems": 70} },
    "karthik": { "department": "BE CSE", "year": 3, "marks": {"physics": 70,"Engineering maths": 65,"power systems": 60} },
}

for name, info in students.items():
    total_marks = sum(info['marks'].values())
    print("student name:", name)
    print("Department:", info['department'])
    print("Year:", info['year'])
    print("Total Marks:", total_marks)
    print("\n")
    