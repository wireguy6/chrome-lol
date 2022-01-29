


import webbot
import time
web = webbot.Browser()



print ("This project is currently beta and will be better soon. Enjoy the Chromeium created mostly by RiZe_Frostbite. DongwooPark didn't do much.")
time.sleep(1)
print('What is your Name?')

user = input ('Username:')
print('Please Wait...')
time.sleep(.5)
print('Hello,', user, 'What would you like to do today?')

print('_______________________________')
print('| Enter Google for Google      |')
print('| Enter Reddit for Reddit      |')
print('| Enter Overlord for Overlord  |')
print('| Enter Custom for your own url|')
print('| Enter YT for Youtube         |')
print('| *This is case sensitive*     |')
print('_______________________________')

Site = input('Option:')

if Site == 'Google':
	print('What would you like to search?')
	search = input('Search:')
	print(user,'has entered',search, 'Would you like to conform?')
	search_input = input('Y/N:')
	if search_input == 'Y':
		web.go_to('www.google.com')
		web.type(search)
		web.press(web.Key.ENTER)
	if search_input == 'N':
		print('Please re-run')
	else:
		print('Y for yes N for no, please re-run')

	
	
	


if Site == 'Reddit':
	print('You are now going to Reddit')
	web.go_to('www.reddit.com')

if Site == 'Overlord':
	print('You are now going to Overlord')
	web.go_to('https://hidden.rizefrostbite.repl.co/')

if Site == 'Custom':
	print('Which site would you like to go to?')
	print('Example: www.site.com')
	url = input('url:')
	if url == 'www.pornhub.com':
		print('horni')
		web.go_to(url)
  
	print(user,'Wants to go to',url,'is this correct?')
  
	url_input = input("Y/N:")

	if url_input == "N":
		print('Please Re-Run',user)

	if url_input == "Y":
		web.go_to(url)
if Site == 'YT':
	print('Would you like to search?')
	Y_or_N = input('Y/N:')
	if Y_or_N =='Y':
		print('What would you like to search')
		search_2 = input('Search:')
		web.go_to('www.youtube.com')
		web.click('Search')
		web.type(search_2)
		web.press(web.Key.ENTER)
	if Y_or_N =='N':
		web.go_to('www.youtube.com')
	else:
		print('please re-run')

	
	