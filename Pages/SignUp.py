class SignUp():

    #Page Objects


    signInSignUp_xpath= "//*[text()=' Sign in / Sign up ']"
    signInTitle_xpath= "//h2[text()='Sign in']"
    enterMobileNumberTextField_css= "#loginfirst_mobileno"
    submitButton_Class = "//button[@class='btn-signpass arrowbtn']"
    firstName_Id = "reg_firstname"
    lastName_id = "reg_lastname"
    emailId_Id = "reg_email"
    password_id = "register_pwd"
    re_enterPassword_id ="register_confirm_pwd"
    verify_class= "//button[@class='btn-login']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnSignInButton(self):
        self.driver.find_element_by_xpath(self.signInSignUp_xpath).click

