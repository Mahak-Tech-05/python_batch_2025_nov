#sort code in lambda
students = [(19,'ramlal'),(18,'chiku') , (20,'billu')]
storted_students = sorted(students,key=lambda x:x[1])
print(storted_students)
