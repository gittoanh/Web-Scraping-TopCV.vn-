from bs4 import BeautifulSoup
import requests
import time

headers = {
    'authority': 'www.topcv.vn',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'cookie': '_gcl_au=1.1.640844063.1632220387; _ga=GA1.2.2038296616.1632220388; cf_clearance=_yx_PjeeEHGW2cwOhHauTfIBj_tKkZg2i1vpVr3QdI0-1634549195-0-250; G_ENABLED_IDPS=google; cancel-job-waiting=1; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImUrdzl0Uk9MaHdhV2crSGZCN0ZxSVE9PSIsInZhbHVlIjoiSjdRT3ZrTGhnajIwSDVLN1loM3plclNSRFpmcGlLanBRZVRRMmRUMUZsTGliMHVnQzBPOTRwQnpZaTRmcGdEUTAwWll2aXlTXC81T0JLY3M0eVFZb3h2TXhyXC9FMDlLVVU3MkpoSmlBZmxKNHM5STRpcDEzSWUwV1IyOFRHV2N5dXJWaUEyWkU3cXY0S2VnR2VqaW1sM2c9PSIsIm1hYyI6Ijk4OTUxMDFmZTA2ZWFkZTJhMTJiZjY5YTM2NGZiY2FkYWFmN2IyNWY2ZGNiZmNlOThhNWFjNWUzZmU0NTk2MDMifQ%3D%3D; popup-ebook-cv=1; _taid=Dc2RiChXxS.1638447544277; _gid=GA1.2.110349384.1638447544; _tafp=7d42689b3e1c9c44ad846d9129540614; not_show_noti=true; XSRF-TOKEN=eyJpdiI6IktzZkFzdnRaR2oxYjZoYjljN2tjaHc9PSIsInZhbHVlIjoibFVFRXMxWjFNT2M1Tk9hR2pQVVFlbDdEVXlpK1BIZUQ1dnhVUnpCbkc3Y0lPVU5CYUprYXhPVFNXd3pJSWpJejdPcFVHK01uSHlaTzN5ZFc1WlwvNk1JXC9XbktWa0thUW9iaXM4OW9iN3B6NDNsekdIV0hheUJsMlBEUEZlQTlzaSIsIm1hYyI6ImNiYWZjYzIzODViODBjNWVmZDFiMTU3NmYyYWI2OGMyZTIxM2ZlOGJjZDlkYzdlYWRhNjEzMjVjNTdhMDg1YzYifQ%3D%3D; topcv_session=eyJpdiI6IjZ3OTNjNlhiNWFzWUZkWVdEbllrY0E9PSIsInZhbHVlIjoiV0NlSzkrM0xnbFhKeU1wQWJzaUltUVwvd1ByWHdCS1BuaXBFblcydEFXVXhqNU5LWlpPTkpHMXNKbm14QXdZSllTcjdQMHErZEhvdTlNMFAyZ29Eb0IySmNUWXZMN0hSbFRZbndXQ0dGaTNHQlM5WklQNGJMalBMT1ZWbkxpRGlpIiwibWFjIjoiOGFhNTNmMDc4M2NmYWEzNmEzNzhlZGNiZjlhZDdjYmMzNjNlMWJiMDA2OTM5ZGUwOTkyYTgyYWU0MDczYTFlMyJ9',
}

def job_scraping():
    count = 1
    with open('Posts/Job.txt', 'w', encoding="utf-8") as f:
        for page in range(1, 7):
            params = (
                ('page', page),
            )

            html_text = requests.get('https://www.topcv.vn/viec-lam-hap-dan', headers=headers, params=params).text
            soup = BeautifulSoup(html_text, 'lxml')

            jobs = soup.find_all('div', class_ = 'job-item bg-highlight job-ta result-job-hover')
            for job in jobs:
                job_title = job.find('span', class_ = 'bold transform-job-title').text
                company = job.find('p', class_ = 'company underline-box-job').a.text
                salary = job.find('label', class_ = 'salary').text
                location = job.find('label', class_ = 'address').text
                f.write(f'No. {count} \n')
                f.write(f' Job title: {job_title} \n')
                f.write(f' Company: {company}\n')
                f.write(f' Salary: {salary}\n')
                f.write(f' Location: {location}\n \n')
                count += 1

if __name__ == '__main__':
    while True:
        job_scraping()
        minutes = 10
        print(f'Waiting {minutes} minutes')
        print("Executed successfully")
        time.sleep(minutes * 60)
