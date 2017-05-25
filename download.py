from selenium import webdriver
import time

url_id = 11
url = "https://www3.reg.cmu.ac.th/regist359/public/result.php?id=5806106"
counter = 0
while url_id < 99:
    times = time.time()
    print("Snapshot Content 5806106"+str(url_id).zfill(3)+ " tarting")
    service_args = [
        '--ignore-ssl-errors=true',
        '--cookies-file=test.cookies',
        '--disk-cache=true'
        ]
    driver = webdriver.PhantomJS(service_args=service_args)
    driver.set_window_size(1366, 768) # set the window size that you need
    driver.get(url+str(url_id))
    driver.save_screenshot('2502/cmu_'+str(url_id).zfill(3)+'.png')
    print("\tSnapshot Content 5806106"+str(url_id)+" Finished! @"+str(round(time.time()-times,3)))
    url_id += 1