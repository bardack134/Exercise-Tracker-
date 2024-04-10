# Exercise-Tracker

This Python script allows users to automatically log their daily exercises and the calories burned into a Google Sheets document. The user inputs the exercise they did and its duration, and the script uses the Nutritionix API to calculate the calories burned. Then, it uses the Sheety API to add this information to a Google Sheets document.

## Table of Contents
- Description
- Tools Used
- APIs Used
- Screenshots

## Description
The Exercise-Tracker is a Python application that allows users to automatically log their daily exercises and the calories burned into a Google Sheets document. The user inputs the exercise they did and its duration, and the script uses the Nutritionix API to calculate the calories burned. Then, it uses the Sheety API to add this information to a Google Sheets document.


## Tools Used
- **Requests:** A Python library used to send HTTP requests to the Nutritionix and Sheety APIs.
- **Datetime:** A Python module used to work with dates and times, needed to record the date and time of each exercise entry.
- **Google Sheets:** Used as a database to store the exercise information.

## APIs Used
- **Nutritionix API:** Used to get data about the user’s exercise, like the calories burned. More information can be found at  https://docx.syndigo.com/developers/docs/natural-language-for-exercise
- **Sheety API:**  It's tool that allows us to communicate with Google Sheets. We use Python to　write, and manage data in Google Sheets. It’s a very useful tool for automating tasks and managing data. More information can be found at   https://sheety.co/

## Screenshots


![img1](https://github.com/bardack134/Exercise-Tracker-/assets/142977989/746919f4-5f29-4fa1-85e2-acd91a51fcd5)


![img2](https://github.com/bardack134/Exercise-Tracker-/assets/142977989/e1e3bc12-b779-43a7-bdc5-c5d7f0df54a0)
