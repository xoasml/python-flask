import csv

def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "url"])

    for job in jobs:
        url = job.find("a")["href"]
        title = job.find("strong", class_="JobCard_title__HBpZf")
        company = job.find("span", class_="JobCard_companyName__N1YrF")

        data = {
            "title": title.text,
            "company": company.text,
            "url": f"https://www.wanted.co.kr{url}",
        }

        writer.writerow(data.values())

    file.close()
