#required imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient


# declare global variables
path = 'Users/tayla/Desktop/svelte-test-table-Copy/chromedriver'
website = 'https://forexonline.bidvestbank.co.za/AvailableCurrencies'
test_list = []


### FETCH DATA FROM WEBSITES ###
def get_data(website):
    s=Service('C:/Users/tayla/Desktop/svelte-test-table/chromedriver.exe')
    driver = webdriver.Chrome(service=s)

###driver = webdriver.Chrome(path)
    driver.implicitly_wait(8) # gives an implicit wait for 20 seconds
    driver.get(website)

# to identify the table column
    #rows = driver.find_elements(By.XPATH, "//*[@class= 'table table-bordered']/tbody/tr[1]")


    for test in driver.find_elements(By.XPATH, "//*[@class= 'table table-bordered']/tbody/tr"):
    #for cells in test.find_elements(By.TAG_NAME, "td"):
        #print(cells.text)
        thisCurrency = test.find_elements(By.TAG_NAME, "td")[1].text
        thisName = test.find_elements(By.TAG_NAME, "td")[2].text
        thisBuy = test.find_elements(By.TAG_NAME, "td")[3].text
        thisSell = test.find_elements(By.TAG_NAME, "td")[4].text

        exchangeItem = {
        'currency':thisCurrency,
        'name':thisName,
        'buy':thisBuy,
        'sell':thisSell
    }

        test_list.append(exchangeItem)

    print(test_list)

#close driver
    driver.quit()

### END FETCH DATA FROM WEBSITES ###

### PUSH DATA TO MONGODB

def push_data(test_list):
    cluster = "mongodb+srv://taylaleekastis:eZuoRoQKkG2kkq15@cluster0.kmwh4kf.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(cluster)

    print(client.list_database_names())

    db = client.TestDB
    collection = db.testcollection

    print(db.list_collection_names())

    for item in test_list:
        collection.insert_one(item)


#get_data(website)

def main():
    get_data(website)
    push_data(test_list)


if __name__ == '__main__':
    main()