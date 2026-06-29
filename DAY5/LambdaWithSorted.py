students=[
    ("a",23),
    ("b",22),
    ("c",24),
]
sorted_stud=sorted(
    students,
    key=lambda x:x[1]

)
print(sorted_stud)