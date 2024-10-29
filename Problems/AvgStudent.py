if __name__ == '__main__':
    n = int(input("How many stored student : "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter Name and Marks : ").split()

        scores = list(map(float, line))
        
        student_marks[name] = scores
    query_name = input("Enter Name : ")
    if query_name in student_marks:

        for key , value in student_marks.items():
            if key ==   query_name:
                avg = float(sum(value)/len(value))
                break
    print(f"Avg :{avg:.2f}")
        