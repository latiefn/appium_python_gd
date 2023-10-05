
from appium import webdriver
import unittest
import random
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AndroAppTest (unittest.TestCase):
    def setUp(self):
        desired_capabilities = {
            'platformName': 'android',
            'deviceName': 'emulator-5554', #adjust it to the emulator name
            'platformVersion': '14', #adjust it to the emulator version
            'automationName': 'uiautomator2',
            'appPackage': 'com.pajk.idpersonaldoc',
            'appActivity': 'com.pajk.idpersonaldoc.activities.HomePageActivity',
            'app': '/Users/latief/Documents/appium_python_test/app/GD.apk',
            'noReset':True,
            'fullReset':False
        }

        appium_server_url = 'http://localhost:4723'
        capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
        self.driver = webdriver.Remote(appium_server_url, options=capabilities_options)


    def test_case_1(self):


        button_profile = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/home_bottom_profile').click()
        button_profile_detail = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/rl_profile').click()
        sleep(1)
        button_profile_name = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/tv_name').click()
        sleep(1)
        name_user = "Nama User"
        change_name = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/et_content')
        random_number = random.randint(1, 999)
        name_user_random = f"{name_user} {random_number}"
        change_name.send_keys(name_user_random)
        button_save = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/tv_save').click()
        sleep(1)
        text_profile_name = self.driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]')
        text_name = text_profile_name.text
        if text_name == name_user_random:
            print ("Test Case 1 Berhasil")
        else:
            self.assertEqual(text_name, {name_user_random}, "Test Case 1 Gagal")
        sleep(1)
        self.driver.back()
        button_beranda = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/home_bottom_homepage').click()
        sleep(1)

    def test_case_2(self):
        button_profile = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/home_bottom_profile').click()
        button_profile_detail = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/rl_profile').click()
        sleep(1)
        button_profile_email = self.driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]').click()
        sleep(1)
        email_user = "mail@mail.com"
        change_email = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/et_content')
        random_number = random.randint(1, 999)
        email_user_random = f"{random_number}{email_user}"
        change_email.send_keys(email_user_random)
        button_save = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/tv_save').click()
        sleep(1)
        text_profile_email = self.driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]')
        text_email = text_profile_email.text
        if text_email == email_user_random:
            print ("Test Case 2 Berhasil")
        else:
            self.assertEqual(text_email, {email_user_random}, "Test Case 1 Gagal")
        sleep(1)
        self.driver.back()
        button_beranda = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/home_bottom_homepage').click()
        sleep(1)

    def test_case_3(self):

        button_profile = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/home_bottom_profile').click()
        button_profile_detail = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/rl_profile').click()
        sleep(1)
        button_profile_weight = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/vv_weigh').click()
        sleep(1)
        TouchAction(self.driver)   .press(x=1112, y=1798)   .move_to(x=1120, y=1663)   .release()   .perform()
        text_profile_update_weight = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/tv_content')
        text_value = text_profile_update_weight.text
        #print({text_value})
        button_profile_save = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/tv_save').click()
        sleep(1)
        text_profile_weight = self.driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[7]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]')
        text_value_2 = text_profile_weight.text
        #print({text_value_2})
        if text_value == text_value_2:
            print ("Test Case 3 Berhasil")
        else:
            self.assertEqual(text_profile_update_weight, text_profile_weight, "Test Case 2 Gagal")
        sleep(1)
        button_profile_save = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/iv_close').click()
        sleep(1)
        button_beranda = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/home_bottom_homepage').click()


    def test_case_4(self):
        button_profile = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/home_bottom_profile').click()
        button_profile_detail = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/rl_profile').click()
        sleep(1)
        button_profile_heigh = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/vv_heigh').click()
        sleep(1)
        TouchAction(self.driver)   .press(x=1112, y=1798)   .move_to(x=1120, y=1663)   .release()   .perform()
        text_profile_update_heigh = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/tv_content')
        text_value = text_profile_update_heigh.text
        #print({text_value})
        button_profile_save = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/tv_save').click()
        sleep(1)
        text_profile_heigh = self.driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[6]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]')
        text_value_2 = text_profile_heigh.text
        #print({text_value_2})
        if text_value == text_value_2:
            print ("Test Case 4 Berhasil")
        else:
            self.assertEqual(text_profile_update_heigh, text_profile_heigh, "Test Case 2 Gagal")
        sleep(1)
        button_profile_save = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/iv_close').click()
        sleep(1)
        button_beranda = self.driver.find_element(AppiumBy.ID, 'com.pajk.idpersonaldoc:id/home_bottom_homepage').click()



    def tearDown(self):
        self.driver.quit()

if __name__== '__main__':
        unittest.main()
