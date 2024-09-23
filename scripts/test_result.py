path = "../data/test_result.txt"

with open(path, "r") as f:
    test_results = f.readlines()

print("Original Results:")
for result in test_results:
    print(result.strip())

sorted_alphabetically = sorted(test_results)

with open(path, "a") as f:
    f.write("\nSorted alphabetically\n")   

    for result in sorted_alphabetically:
        f.write(result)


clean_list = [result.strip() for result in test_results]

names = []
scores = []


for entity in clean_list:
    entity_splitted = entity.split()
    name = " ".join(entity_splitted[:-1])
    score = int(entity_splitted[-1])

    names.append(name)
    scores.append(score)

grade_dict = {
    "F":[],
    "E":[],
    "D":[],
    "C":[],
    "B":[],
    "A":[]
}

for name, score in zip(names,scores):
    if score < 20:
        grade_dict["F"].append(f"{name} {score}")
    elif 20 <= score < 30:
        grade_dict["E"].append(f"{name} {score}")
    elif 30 <= score < 40:
        grade_dict["D"].append(f"{name} {score}")
    elif 40 <= score < 50:
        grade_dict["C"].append(f"{name} {score}")
    elif 50 <= score < 60:
        grade_dict["B"].append(f"{name} {score}")
    else:
        grade_dict["A"].append(f"{name} {score}")


with open(path, "a") as f:
    f.write("\nSorted results:\n") 
    for grade, students in grade_dict.items():
        f.write(f"Grade: {grade}\n")
        for student in students:
            f.write(f"{student}\n")