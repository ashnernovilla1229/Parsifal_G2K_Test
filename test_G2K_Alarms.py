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
        # logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet
        
    except:
        Time_BeforeTest, Time_AfterTest, TimeDiff = 0,0,0
        result = "Fail"
        
        Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet

def G2K_Operator_Alarms():
    TestName = "G2K_Operator_Alarms" # Title of the test
    try:
        driver.find_element_by_xpath("//button[contains(text(),'Operation')]").click() 
        Time_BeforeTest = datetime.now() #Time log the start of the test after opening the browser
        # driver.find_element_by_id("openStartModuleCard").click()
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/img[1]").click()
        
        Time_AfterTest = datetime.now() #Time log after pressing the submit button
        TimeDiff = abs(Time_AfterTest - Time_BeforeTest) #Difference of before and after the test
        result = "Pass"
        Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet
        
    except:
        Time_BeforeTest, Time_AfterTest, TimeDiff = 0,0,0
        result = "Fail"
        
        Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet

def G2K_Alarm_List():
    TestName = "G2K_Alarm_list" # Title of the test
    try:
       Time_BeforeTest = datetime.now()
       # driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[2]/div[1]/section[1]/div[2]/div[1]/div[2]/div[2]").click()
       driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[2]/div[1]/section[1]/div[2]/div[1]/div[1]/div[2]").click()
       time.sleep(1)
      
       G2KAlarmElement = driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[4]/div[2]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]")
       G2KAlarmElement.screenshot(datetime.now().strftime("%B_%d_%Y_%H_%M_")+"G2K_AlarmList.png")
       
       # screenshot = Image.open(datetime.now().strftime("%B_%d_%Y_%H_%M_")+"G2K_AlarmList.png")
          
       G2KAlarmList = driver.find_elements_by_class_name('AlarmItemDark_alarmData__1GGMn')

       listalarm = []
       listdatealarm = []
       
       for alarmlist in G2KAlarmList:
           # title = alarmlist.find_element_by_xpath('//*[@id="btnAlarmItemToggleExpand"]/div[2]/div[1]/div/div[1]]').text
           title_alarm = alarmlist.find_element_by_class_name('AlarmItemDark_alarmsCollapseTitle__DLpk5').text
           tile_datealarm =  alarmlist.find_element_by_class_name('AlarmItemDark_alarmsCollapseDateicon__3f-t5').text
           
           listalarm.append(title_alarm)
           listdatealarm.append(tile_datealarm)
       Time_AfterTest = datetime.now()  
       title_alarm = pd.DataFrame(listalarm, columns=['Alarm_Title'])
       tile_datealarm = pd.DataFrame(listdatealarm, columns=['Alarm_Date'])
       title_alarm['Alarm_Date'] = tile_datealarm['Alarm_Date']
       
       G2K_Alarm_List.title_alarm = title_alarm
       
       TimeDiff = abs(Time_AfterTest - Time_BeforeTest) #Difference of before and after the test
       result = "Pass"
       
       Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet

    except:
        result="Fail"
        Time_BeforeTest, Time_AfterTest, TimeDiff = 0,0,0
        
        Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet

def G2K_Alarm_Details():
    TestName = 'G2K_Alarm_Details'
    try:
        
        #This is to add the path for click all the buttons for the detailed list
        Time_BeforeTest = datetime.now()
        G2K_Alarm_Details_Button = driver.find_elements_by_class_name('AlarmItemDark_buttonUnselectd__olxC5')
        
        for alarmdetailsbutton in G2K_Alarm_Details_Button:
            alarmdetailsbutton.find_element_by_class_name('AlarmItemDark_alarmsCollapse__Tehk3').click()
        
        
        G2KAlarmDetails = driver.find_elements_by_class_name('AlarmItemDark_alarminfocontExpand__2FCom')   
        listalarmcode = [] 
        listalarmlocation = []
        listalarmtouchpoints = []
        listalarmclass = []
        i=0         
        for alarmdetails in G2KAlarmDetails:
            i=i+1
            alarmcode = alarmdetails.find_element_by_class_name('AlarmItemDark_alarminfoinsCon__3UHiY').text
            alarmlocation = alarmdetails.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/section/div[2]/div/div[1]/div/div[2]/div/div'+str([i])+'/div[2]/div/div[1]/div[3]/div[2]').text
            alarmtouchpoints = alarmdetails.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/section/div[2]/div/div[1]/div/div[2]/div/div'+str([i])+'/div[2]/div/div[1]/div[2]/div[2]').text
            alarmclass = alarmdetails.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/section/div[2]/div/div[1]/div/div[2]/div/div'+str([i])+'/div[2]/div/div[1]/div[4]/div[2]').text
            
            listalarmcode.append(alarmcode)
            listalarmlocation.append(alarmlocation)
            listalarmtouchpoints.append(alarmtouchpoints)
            listalarmclass.append(alarmclass)
            
    except:
        result="Fail"
        Time_BeforeTest, Time_AfterTest, TimeDiff = 0,0,0
        Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet
    
    listalarmcode = pd.DataFrame(listalarmcode, columns=['Alarm_Code'])
    listalarmcode['Alarm_Location'] = pd.DataFrame(listalarmlocation, columns=['Alarm_Location'])
    listalarmcode['Alarm_Touchpoints'] = pd.DataFrame(listalarmtouchpoints, columns=['Alarm_Touchpoints'])
    listalarmcode['Alarm_Class'] = pd.DataFrame(listalarmclass, columns=['Alarm_Class'])

    title_alarm = pd.concat([G2K_Alarm_List.title_alarm, listalarmcode], axis=1)
    
    os.chdir(working_directory)
    title_alarm.to_csv(datetime.now().strftime("%B_%d_%Y_%H_%M_AlarmList.csv"))
    
    Time_AfterTest = datetime.now()  
    TimeDiff = abs(Time_AfterTest - Time_BeforeTest) #Difference of before and after the test
    result = "Pass"
    
    Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet

        
##Use this code if to run test function
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
        driver.implicitly_wait(10)

    except:
        TestName = "G2K_WebLoading"
        Time_BeforeTest, Time_AfterTest, TimeDiff = 0,0,0
        result = "Fail"
        Logtest(TestName , Time_BeforeTest, Time_AfterTest, TimeDiff, result) #Datalog to the csv sheet

    
    #1. Creating a test log csv file
    Create_Testlog() 
    
    #2. Load the G2K Web Page
    G2K_Webloading()
    
    #3. Login to the Maps
    G2K_Login()
    
    #4. Load the Alarms By Clicking and Entering Page 
    G2K_Operator_Alarms()
    
    #5. Verify if the alarms are updated and get the basic summary
    G2K_Alarm_List()
    
    #6. Get All Details of the alarm
    G2K_Alarm_Details()
    
    #Exit the Browser
    driver.quit()
  
