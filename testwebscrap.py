import requests # to access webpages
from bs4 import BeautifulSoup # to scrape webpages

# sample indeed url
url = "https://www.indeed.com/q-View-jobs.html?vjk=7b862fcd700ea31c"

response = requests.get(url)

if response.status_code == 200:
    # parse the HTML content 
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find job titles
    job_titles = soup.find_all('h2',{'class':'jobTitle'})

    # Print the job titles to screen
    for job in job_titles:
        print(job.get_text())

else:
    print(f"Failure to fetch webpage. Status code: {response.status_code}")

