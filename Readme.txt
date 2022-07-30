Online shopping for local market

    This is a web application created with the idea that, as online shopping websites grow larger local shops find
    it harder to compete in the market. But local shops has a huge advantage over online website in person experience,
    immediate purchase means no waiting for product to arrive. only sector it gets hampered is people need to visit to 
    shop to check the availability of the required product and roam over cities to find it. Hence This web application.
    counsumers can create account and search for the required product in local shops and later visit that specific shop 
    to buy it when time is available. also shop owner can sign up and login and maintain their shops database for counsumers 
    to see. it also brings the sense of competion among shop owners hence reducing the price of products indirectly.
    
Tools or languages used

    Project is made using python 3 language. module used to develop web application is flask and database is created using mysql.
   
    
Project StartUp

    following commans are needed to create databases before web application works smoothly :
    
    create database shopping;

    create database shops;

    use shopping;

    create table shop_list (id_shop int primary key auto_increment, shop_name varchar(10), shop_pass varchar (10), shop_add varchar (20) )auto_increment=1;

    create table cust_list (id_cust int primary key auto_increment, cust_name varchar(10), cust_pass varchar (10), cust_add varchar (20) )auto_increment=1;

    use shops;
    
Contents inside database 
    
Database 1: shopping

        Table 1 : cust_list

        id_cust cust_name cust_pass cust_add

        Table 2 : shop_list

        id_shop shop_name shop_pass shop_add

Database 2: shops

        Table 1 : (shop name)
        
        id item_name item_price item_quantity
        
        
