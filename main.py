import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from webdriver_manager.firefox import GeckoDriverManager

# Initiliaze Webdriver
try:
	driver = webdriver.Chrome(ChromeDriverManager().install())
except:
	driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

def BlackBoardLogin():

	email =  # Enter email here
	password = # Enter password here


	#Opening Blackboard.
	driver.get('https://sts.commnet.edu/adfs/ls/?SAMLRequest=lVLLTsMwEPwVa%2B%2BJHaOiYjWtCqgCCURFAgculeMsxCWxi9ep%2BHxCH6JckLhYWnlmZ3dmJ7PPrmVbDGS9yyFLBTB0xtfWveXwVC6SMcymE9JdKzdq3sfGPeJHjxTZQHSk9j859MEpr8mScrpDUtGoYn5%2Fp2Qq1Cb46I1vgc2JMMRB6so76jsMBYatNfj0eJdDE%2BOGFOcmGkNp1WrzXnkd6tT4jutBOvkW47unKB64bq0mvhpLucqAXQ8zWafjbo9jK4r0ze4cxhTrnuv6lXhLHNjCB4O7fXJ41S0hsNvrHHRWNc0ZrsdrK8zorc7WIxR1JS%2F0uqqaAUNLTWS3%2BMMi6vHWUdQu5iCFFIkYJ0KW2bkSUp1l6cUoewG2PJhwad3e3L8cq%2FYgUjdluUyWD0UJ7PkY0gCAQyRqpx5Os%2Fi7sT4GANN%2F2j3hp4rTQ%2Fn7JqZf&SigAlg=http%3A%2F%2Fwww.w3.org%2F2000%2F09%2Fxmldsig%23rsa-sha1&Signature=JaLpBJGZwIJqarl8NuQEyRvvHdv1NnORHuKFk6oLimVZkaPdx%2F6I30FO2nLJsuQGfDMYq35s%2B6zpiiyugInypWlhZxji83zVOzmw2Dhh0fBBKfLOGacI9QyeaZ0w8C49lFvc6Qh%2BcPAdeUNJqkGU%2B6Ggk8CG2Du8gTrWK0dnm34L72xwD64t0uj4CMxJ7AiV%2BGbqJtN%2F5i9yHORy4FnTpAnCam%2BMzwkQjT%2FNK%2FuQZhwhOAp5GKC5uN2i5PVcy8dlBSA4Kfy1phQoyJ6C6ZYKNwt%2FsQz7a%2BCRdJ8Qnj9lgOco69n6l22rue244vo3wC59hRHuk90XMyaMf0c8JGx%2FRQ%3D%3D') 
	print ("Comment Opened") 
	time.sleep(1) 
	
	
	#Enters your email
	username_box = driver.find_element_by_id('userNameInput') 
	username_box.send_keys('01833736@student.commnet.edu') 
	print ("Email Id entered") 
	time.sleep(1)
	
	#Enters your password 
	password_box = driver.find_element_by_id('passwordInput') 
	password_box.send_keys('LoginPortal13!?') 
	print("Password entered")
	time.sleep(1)

	#Pressing The Login Button  
	login_box = driver.find_element_by_id('submitButton') 
	login_box.click()
	proceed_box = driver.find_element_by_id('error_message_button')
	proceed_box.click()
	time.sleep(2)

	privacy_ok = driver.find_element_by_class_name('button-1')
	privacy_ok.click()



	
	print ("Done")
	input('Press Enter to quit') 
	driver.quit() 
	print("Finished")

BlackBoardLogin()