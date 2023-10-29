import logging
import os
from pathlib import Path
import time
import random


from progress.bar import Bar
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


BASE_URL_COURSE = "https://symfonycasts.com/screencast/symfony/setup"


load_dotenv()
opt = webdriver.ChromeOptions()
# opt.add_argument("headless")
opt.add_experimental_option(
    "prefs",
    {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
    },
)
driver = webdriver.Chrome(options=opt)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)


def get_course_name_by_course() -> str:
    logging.info("Retrieving the course name")
    driver.get(BASE_URL_COURSE)
    return (
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/h4/a")
        .text.lower()
        .replace(" ", "-")
    )


def login():
    logging.info("Connection to SymfonyCasts")
    driver.get("https://symfonycasts.com/login")
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(
        os.getenv("SYMFONYCASTS_USERNAME")
    )
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(
        os.getenv("SYMFONYCASTS_PASSWORD")
    )
    driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div/form/div[2]/div[2]/button"
    ).click()


def download_videos_by_course() -> None:
    total_chapter = get_number_of_chapter_by_course()
    course_name = get_course_name_by_course()
    driver.get(BASE_URL_COURSE)
    logging.info("Creating the folder")
    os.system(f"mkdir testing/{course_name}")
    bar = Bar("Downloading video", max=total_chapter)
    while len(driver.current_url.split("/")) > 5:
        download_link = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/span[2]/a"
        ).get_attribute("href")
        driver.get(download_link)
        next_link = driver.find_element(
            By.XPATH, "/html/body/div[4]/div[4]/div[3]/a"
        ).get_attribute("href")
        driver.get(next_link)
        bar.next()
        time.sleep(random.randint(1, 8))
        if "activity" not in next_link:
            continue
        next_link = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/a"
        ).get_attribute("href")
        driver.get(next_link)


def move_file() -> None:
    logging.info("Moves all mp4 files to the associated folder")
    courses_folder = Path.cwd() / "harmonious-development-with-symfony-6"
    list_video_files = [
        f for f in Path.cwd().iterdir() if f.is_file() and f.suffix == ".mp4"
    ]
    for video in list_video_files:
        video.rename(courses_folder / video.name)


def get_number_of_chapter_by_course() -> int:
    logging.info("Retrieve the total number of chapters in the course")
    driver.get(BASE_URL_COURSE)
    list_chapters = driver.find_element(
        By.XPATH, "/html/body/div[4]/div[1]/div[1]/div/div/ul"
    )
    chapters = list_chapters.find_elements(By.TAG_NAME, "li")
    return sum(
        chapter.get_attribute("class") != "py-4 pl-5 challenge-list-item"
        for chapter in chapters
    )


def download_pdf_by_course() -> None:
    driver.get(BASE_URL_COURSE)
    logging.info("Downloading PDF")
    download_link = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/span[4]/a"
    ).get_attribute("href")
    driver.get(download_link)


def worker():
    login()
    download_videos_by_course()
    download_pdf_by_course()
    time.sleep(5)
    move_file()


if __name__ == "__main__":
    worker()
