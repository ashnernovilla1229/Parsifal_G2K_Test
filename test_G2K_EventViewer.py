# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 20:13:54 2022

@author: Openlab
"""

''' This test is for G2K Functionality'''


from selenium import webdriver

import csv  
from datetime import datetime
import os
import time
import pandas as pd


def Create_Testlog():   #This code to chech if the name of the csv already exist, if no then create the csv
   if os.path.isfile(working_directory+"\\G2K_Test.csv") is True:
       print("File Exist")
   else:
       print("File Create")
       header = ['Test_Name', 'Time_BeforeTest', 'Time_AfterTest', 'Time_Difference', 'Test_Result']
       with open('G2K_Test.csv', 'w', encoding='UTF8') as f:
           writer = csv.writer(f)
           writer.writerow(header)
           
def Logtest(TestName , BeforeTestTime, AfterTestTime, TimeDiff, TestResult): #This code is to do the time log in the csv
    with open(working_directory+"\\G2K_Test.csv",'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        f.writelines(f'\n{TestName},{BeforeTestTime},{AfterTestTime},{TimeDiff},{TestResult}')

def G2K_Webloading():
    TestName = "G2K_WebLoading"
    Time_BeforeTest = datetime.now() #Time log the start of the test after opening the browser
    
    driver.get("https://parsifal.openlab.huawei.com/") #Test Link
    
    try:
        driver.find_element_by_id("details-button").click()  #if a google warning appear run this code
        driver.find_element_by_id("proceed-link").click()
    except: 
        print("Verification Done") #If no error pass to exception
    
    Time_AfterTest = datetime.now() #Time log after pressing the submit button
    result = "Pass"
    TimeDiff = abs(Time_AfterTest - Time_BeforeTest) #Difference of before and after the test

    Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet
   
def G2K_Login():      
    TestName = "G2K_Login" # Title of the test
    try:
        Time_BeforeTest = datetime.now() #Time log the start of the test after opening the browser
        driver.find_element_by_xpath("//input[@id='userName']").send_keys("psim")    
        driver.find_element_by_xpath("//input[@id='passowrd']").send_keys("P@ssw0rd")
        driver.find_element_by_xpath("//button[@id='signInSubmit']").click()
        
        Time_AfterTest = datetime.now() #Time log after pressing the submit button
        TimeDiff = abs(Time_AfterTest - Time_BeforeTest) #Difference of before and after the test
        result = "Pass"
        Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet
        
    except:
        Time_BeforeTest, Time_AfterTest, TimeDiff = 0,0,0
        result = "Fail"
        
        Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet

def G2K_EventViewer():
    TestName = "G2K_EventViewer" # Title of the test
    try:
        driver.find_element_by_xpath("//button[contains(text(),'Operation')]").click()
        Time_BeforeTest = datetime.now() #Time log the start of the test after opening the browse
        # driver.find_element_by_id("openStartModuleCard").click()
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]/div[4]/img[1]").click()
        
        Time_AfterTest = datetime.now() #Time log after pressing the submit button
        TimeDiff = abs(Time_AfterTest - Time_BeforeTest) #Difference of before and after the test
        result = "Pass"
        Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet
        
    except:
        Time_BeforeTest, Time_AfterTest, TimeDiff = 0
        result = "Fail"
        
        Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet

##Use this code if going to run the test for G2KTesting_EventViewer
if __name__ == '__main__':

   os.chdir(os.environ['USERPROFILE']+'\\Documents') #Change the working directory

   try:   #If the folder is not yet created 
       os.mkdir("G2KTest")
       os.chdir(os.environ['USERPROFILE']+'\\Documents\\G2KTest') #Change the working directory
       working_directory = os.getcwd() #Declare the working directory
   except: #If the folder is created
       os.chdir(os.environ['USERPROFILE']+'\\Documents\\G2KTest') #Change the working directory
       working_directory = os.getcwd() #Declare the working directory

   try:
        driver = webdriver.Chrome(executable_path=r'C:\Users\Openlab\Documents\SeleniumDrivers\chromedriver.exe') 
        driver.implicitly_wait(60)  
   except:
        TestName = "G2K_WebLoading"
        Time_BeforeTest, Time_AfterTest, TimeDiff = 0,0,0
        result = "Fail"
        Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet
   
   #1. Creating a test log csv file
   Create_Testlog() 
    
   #2. Load the G2K Web Page
   G2K_Webloading()
    
   #3. Login to the EventViewer
   G2K_Login()
    
   #4. Load the Map By Clicking and Entering Page 
   G2K_EventViewer()

   #Exit the Browser
   driver.quit()
