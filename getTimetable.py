from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()
USER_ID = os.getenv("USER_ID")
PASSWORD = os.getenv("PASSWORD")

driver = webdriver.Chrome()
driver.get("https://everytime.kr/login")
time.sleep(2)

username = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[1]/input[1]")
password = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/div[1]/input[2]")

username.send_keys(USER_ID)  # 실제 사용자 이름(이메일)으로 변경
password.send_keys(PASSWORD)  # 실제 비밀번호로 변경

login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/input")
login_button.click()
time.sleep(1)

# 로그인 후 시간표 페이지로 이동
driver.get("https://everytime.kr/timetable")
time.sleep(5)

# # 데이터 추출
# data = []
# # 요일별 데이터 추출
# for day in range(1, 6):  # 월요일부터 금요일까지
#     day_data = []
#     subjects = driver.find_elements(By.XPATH, f'//td[{day}]/div[@class="cols"]/div[@class="subject"]')
#     for subject in subjects:
#         # 각 과목의 정보 추출
#         title = subject.find_element(By.TAG_NAME, 'h3').text
#         instructor = subject.find_element(By.TAG_NAME, 'em').text
#         location = subject.find_element(By.TAG_NAME, 'span').text
#         day_data.append((title, instructor, location))
#     data.append(day_data)

# print(data)

# 웹드라이버 종료
driver.quit()
