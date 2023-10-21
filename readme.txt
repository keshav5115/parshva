steps
    1 install django in virtual env
    2 install pandas
    3 run the server in the Parshva dir

Implimented the task in two different methods


method 1 (implimented in app dir)
    reading all the data from csv and storeing into the internal server

    urls
    http://127.0.0.1:8000/store/        (only run once)
        to store all the csv data in to the database.
        

    http://127.0.0.1:8000/product/
        with above urls user enters all the required data and supplier 
        will be selected from dropdown. After submit, PO_number option will get, based on supplier
        after selecting and submiting, the data will be stored in the database.And redirect to the
        docket

    http://127.0.0.1:8000/docket/
        can see table of data 

Note 
     Here I am storing all the csv data into the database/table called ProductOrder.

method 2
    implimented in app2 
    Here  I am storing all the csv data into the temporary list datatype
    http://127.0.0.1:8000/supplier/ by using the url,user can select supplier and Po_number
    from dropdown and similar operation can perform without storing the data into the
    database.


Note
    I have not applied the css, only html templates taken.




