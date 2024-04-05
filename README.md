# Exercise-Tracker-
This Python script allows users to automatically log their daily exercises and the calories burned into a Google Sheets document. The user inputs the exercise they did and its duration, and the script uses the Nutritionix API to calculate the calories burned. Then, it uses the Sheety API to add this information to a Google Sheets document.

**Tools used:**

Requests:  used to send HTTP requests to the Nutritionix and Sheety APIs.

Datetime: used to work with dates and times, needed to record the date and time of each exercise entry.

os: A Python module used to access environment variables where the API keys are stored.

Nutritionix API: Used to get data about the user’s exercise, like the calories burned. https://docx.syndigo.com/developers/docs/natural-language-for-exercise

Sheety API: Used to add the exercise information to a Google Sheets document. https://sheety.co/

Google Sheets: Used as a database to store the exercise information.

![img1](https://github.com/bardack134/Exercise-Tracker-/assets/142977989/746919f4-5f29-4fa1-85e2-acd91a51fcd5)


![img2](https://github.com/bardack134/Exercise-Tracker-/assets/142977989/e1e3bc12-b779-43a7-bdc5-c5d7f0df54a0)
