This is a Selenium based personal project which involves checking the internet speed and comparing it with ideal speed. 

program starts with going to the ookla website for checking internet speed
  - it goes past every pop up and also waits for the website to get loaded.
  - website service checks the speed and provides the upload and download speed
  - the selenium webdriver scraps the data from the website and saves it into the database for furthur comparing

now if the current speed of internet is lower than the ideal speed which was promised by the provider
  - the program logs into twitter with credentials to twitter (X Now) and writes a tweet aimed at the internet provider and complains.
if the current speed is more or equal to the ideal speed which was promised
  - the program logs into twitter with credentials to twitter and writes a tweet to the provier appreciating the service. 
