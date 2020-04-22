from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
class Engines():
        
    def View_Engine(self,proxy_IP,proxy_Port,yt_link,dura):
        
        def printIP():
            print(driver.find_element_by_xpath('/html/body/div[2]/p[1]/strong').text)

        ####Browsr setting####
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", proxy_IP)
        profile.set_preference("network.proxy.http_port", proxy_Port)
        profile.set_preference("network.proxy.ssl", proxy_IP)
        profile.set_preference("network.proxy.ssl_port", proxy_Port)
        profile.update_preferences()
        ##################################
        

        ##For Headless ####
        options = Options()
        options.headless = True
        ######################
        driver = webdriver.Firefox(options=options,firefox_profile= profile,executable_path=r'E:\WebDrivers\geckodriver.exe')



        try:
            driver.get("http://check.torproject.org")
        except WebDriverException:
            print("Dead IP")
            file1=open('Dead_IP.txt','a')
            file1.write(proxy_IP+" "+str(proxy_Port)+"\n")
            driver.quit()
            return
        except TimeoutException:
            print("Took so long")
            file1=open('Dead_IP.txt','a')
            file1.write(proxy_IP+" "+str(proxy_Port)+"\n")
            driver.quit()
            return    
        view_du=(180)
        driver.maximize_window()
        printIP()
        time.sleep(2)
        driver.get(yt_link)
        driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button').click()
        actions = ActionChains(driver)
        actions.send_keys('m')
        actions.perform()
        print('viewing video for '+str(view_du))
        time.sleep(view_du)
        driver.quit()
        print("ended")
        return


        



