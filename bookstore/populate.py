import MySQLdb as mdb
import csv
import sys

def insertValuesFromFile(inputFile):
    con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")
    
    print("Inserting values from " + inputFile)
    errorCount = 0
    
    with open(inputFile, newline='') as f:
        with con:
            cur = con.cursor()
            for row in f:                
                try:
                    cur.execute(row[:-1])
                except:
                    errorCount += 1
                    print("EXCEPTION: Error encounted at following INSERT:")
                    print(row[:-1])
                    continue
                
    print("DONE - Insertion of " + inputFile + " completed")
    if(errorCount > 0):
        print("ERROR - " + str(errorCount) + " rows could not be inserted")
    print("\n")

##### Main Function ##### 
if __name__ == "__main__":
    bookFile = "populateBook"
    inventoryFile = "populateInventory"
    userFile = "populateUser"
    purchaseHistoryFile = "populatePurchaseHistory"
    feedbackFile = "populateFeedback"
    ratingFile = "populateRating"
    
    # Insert rows in File that were generated from createSQL.py
    insertValuesFromFile(bookFile)
    insertValuesFromFile(inventoryFile)
    insertValuesFromFile(userFile)
    insertValuesFromFile(purchaseHistoryFile)
    insertValuesFromFile(feedbackFile)
    insertValuesFromFile(ratingFile)
    
    print("Done")