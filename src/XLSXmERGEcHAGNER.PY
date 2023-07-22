path = r"C:\Users\HP\Downloads\4B.csv"
fp = open(path, "r")
new = open("new.csv", "w")
for line in fp:
    timestamp, email, title, regnos, names =  line.split(",")
    timestamp = timestamp.strip()
    email = email.strip()
    title = title.strip()
    regnos = [regno.strip() for regno in regnos.split("-")]
    names = [name.strip() for name in names.split("-")]
    print(timestamp, email, title, regnos, names)

    new.write(timestamp + "," + email + "," + title + "," + regnos[0] + "," + names[0] + "\n")
    for i in range(1, len(regnos)):
        new.write("," * 3 + regnos[i] + "," + names[i] + "\n")
fp.close()
new.close()


