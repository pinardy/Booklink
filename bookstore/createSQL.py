import csv
import urllib.request
import io
import random
from PIL import Image

def populateBook(bookCSV,outputFile,imageDir,numRow):
    #bookCSV: CSV file that contains unorganised book dataset
    #outputFile: Target file to contain SQL INSERT queries for book
    #imageDir: Local image folder to download to
    #numRow: Number of row of INSERT to create

    w = open(outputFile,'w')
    bookList = []

    with open(bookCSV, newline='') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        
        next(reader)
        count = 0
        while(count<numRow):
            # Read each row of CSV data
            row = next(reader)
            
            # URL of image file
            targetURL = row[-1].strip('"')
            
            # Check if image file is suitable for use
            file = io.BytesIO(urllib.request.urlopen(targetURL).read())
            img = Image.open(file)
            if(img.size[0] < 10 or img.size[1] < 10):
                # Image is deemed too small
                pass
            else:
                # Generate ISBN13 from ISBN10
                isbn10 = row[0].strip('"')
                count_padded = str(count).zfill(3)
                isbn13 = isbn10 + count_padded
                            
                # Get other attributes
                title = row[1].strip('"')
                authors = row[2].strip('"')
                yearPublish = row[3].strip('"')
                publisher = row[4].strip('"')
                
                # Generate random cost
                cost = int(random.normalvariate(50,20))
                
                # Generate INSERT values in SQL format
                print("Generating INSERT book for " + isbn13)
                insertString = "INSERT into book VALUES(\"{0}\",\"{1}\",\"{2}\",{3},{4},\"{5}\",\"{6}\");".format(title,authors,publisher,yearPublish,cost,isbn10,isbn13)
                w.write(insertString + '\n')
                
                # Downloading image file
                filename = imageDir + isbn13 + ".jpg"
                print("Saving " + targetURL + " to " + filename)
                local_filename, headers = urllib.request.urlretrieve(targetURL,filename)
                html = open(local_filename)
                html.close()
                
                # Append to list of all books
                bookList.append(isbn13)
                
                count += 1
                
    w.close()
    
    # Return list of ISBN13 for future functions
    return bookList

def populateInventory(bookList,outputFile):
    # bookList: List of ISBN13
    # outputFile: Target file to contain SQL INSERT queries for inventory

    w = open(outputFile,'w')
    for isbn13 in bookList:
        # Generate random stock amount
        stock = int(random.normalvariate(50,10))
        
        # Generate INSERT values in SQL format
        print("Generating INSERT inventory for " + isbn13)
        insertString = "INSERT into inventory VALUES(\"{0}\",{1});".format(isbn13,stock)
        w.write(insertString + "\n")
    
    w.close()
    
def populateUser(nameList,outputFile):
    #nameList: List that contains unorganised book dataset
    #outputFile: Target file to contain SQL INSERT queries for auth_user

    w = open(outputFile,'w')
    
    for name in nameList:
        # Generate attributes
        password = "password"
        last_login = "2017-11-26 10:24:19.726710"
        is_superuser = 0
        username = name
        first_name = ""
        last_name = ""
        email = name + "@yahoo.com"
        is_staff = 0
        is_active = 1
        date_joined = "2017-11-26 10:24:19.726710"
    
        # Generate INSERT values in SQL format
        print("Generating INSERT auth_user for " + name)
        insertString = "INSERT into auth_user (password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined) VALUES(\"{0}\",\"{1}\",{2},\"{3}\",\"{4}\",\"{5}\",\"{6}\",{7},{8},\"{9}\");".format(password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined)
        w.write(insertString + "\n")
    
    w.close()
    
def populatePurchaseHistory(nameList,bookList,outputFile,numRow):
    #nameList: List that contains unorganised book dataset
    #bookList: List of ISBN13
    #outputFile: Target file to contain SQL INSERT queries for purchaseHistory
    #numRow: Number of row of INSERT to create for each USER (number of books bought by each user)

    w = open(outputFile,'w')
    
    for name in nameList:
        # Decide "numRow" random books to be purchased by user
        booksPurchased = random.sample(bookList, k=numRow)
        print("Generating INSERT purchaseHistory for " + name)
        
        for book in booksPurchased:
            # Generate a random amount of book purchased for each book
            amount = random.randint(1,3)
            
            date = "2017-11-26"
            
            insertString = "INSERT into purchase_history (user_id,ISBN13,no_copies,order_date) VALUES(\"{0}\",\"{1}\",{2},\"{3}\");".format(name,book,amount,date)
            w.write(insertString + "\n")
            
    w.close()

def populateFeedback(nameList,bookList,outputFile,numRow):
    #nameList: List that contains unorganised book dataset
    #bookList: List of ISBN13
    #outputFile: Target file to contain SQL INSERT queries for feedback
    #numRow: Number of row of INSERT to create for each BOOK (number of user who feedbacks each book)
    
    w = open(outputFile,'w')
    feedbackList = []
    
    for book in bookList:
        # Decide "numRow" random users to feedback on the book
        feedbackedBy = random.sample(nameList, k=numRow)
        print("Generating INSERT feedback for " + book)
        
        # Generate a random mean feedback of the book
        meanScore = random.randint(0,10)
        
        date = "2017-11-26"
        
        for name in feedbackedBy:
            # Generate a random feedback to be given by user
            score = int(random.normalvariate(meanScore,1.5))
            if (score < 0): score = 0
            elif (score > 10): score = 10
            
            responseList = {
                0: "Trees have been wasted in the production of this book.",
                1: "A waste of time, don't bother with this book.",
                2: "Absolutely terrible.",
                3: "At least it's a better book than Twilight.",
                4: "It's okay. I guess.",
                5: "Not too bad of a book, but leaves more to be desired.",
                6: "An interesting book if you can look past its flaws.",
                7: "I like this book!",
                8: "Great book, can't wait for more works from this author!",
                9: "I can read this again and again without ever feeling bored!",
                10: "This is possibly the best book in the entire world.",
            }
            
            textResponse = responseList[score]
            
            feedbackList.append((book,name))
            
            insertString = "INSERT into feedback VALUES(\"{0}\",\"{1}\",\"{2}\",{3},\"{4}\");".format(name,book,date,score,textResponse)
            w.write(insertString + "\n")
            
    w.close()
    
    # Return tuple list of ISBN13 and user for future functions
    return feedbackList

def populateRating(nameList,feedbackList,outputFile,numRow):
    #nameList: List that contains unorganised book dataset
    #feedbackList: List that contains feedback information (tuple of book and user)
    #outputFile: Target file to contain SQL INSERT queries for rating

    w = open(outputFile,'w')
    
    for book,feedbackUser in feedbackList:
        otherUsers = nameList.copy()
        otherUsers.remove(feedbackUser)
        
        # Decide "numRow" random users to rate feedback
        ratedBy = random.sample(otherUsers, k=numRow)
        print("Generating INSERT rating for " + feedbackUser + "'s feedback of " + book)

        for ratingUser in ratedBy:
            # Generate a random rating to feedback
            score = random.randint(0,2)
            
            date = "2017-11-26"
            
            insertString = "INSERT into rating VALUES(\"{0}\",\"{1}\",\"{2}\",\"{3}\",{4});".format(ratingUser,feedbackUser,book,date,score)
            w.write(insertString + "\n")
    
    w.close()
    

##### Main Function ##### 
if __name__ == "__main__":

    bookCSV = "bookDataset.csv"
    bookOutputFile = "populateBook"
    imageDir = "booklist/static/images/book-covers_PROJECT/"
    
    inventoryOutputFile = "populateInventory"
    
    nameList = ["tom","mike","john","samuel","max","sarah","mary","anna","emma","elizabeth"]
    userOutputFile = "populateUser"
    
    purchaseHistoryOutputFile = "populatePurchaseHistory"
    
    feedbackOutputFile = "populateFeedback"
    
    ratingOutputFile = "populateRating"
    
    bookList = populateBook(bookCSV,bookOutputFile,imageDir,50)
    populateInventory(bookList,inventoryOutputFile)
    populateUser(nameList,userOutputFile)
    populatePurchaseHistory(nameList,bookList,purchaseHistoryOutputFile,5)
    feedbackList = populateFeedback(nameList,bookList,feedbackOutputFile,4)
    populateRating(nameList,feedbackList,ratingOutputFile,3)
    
    print("Done")