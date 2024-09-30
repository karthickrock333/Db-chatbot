few_shots2 = [
    {'Question': "Can you provide the first and last names of all providers who are listed as Orthopedic specialists?",
     'SQLQuery': "SELECT PROVIDERFIRSTNAME, PROVIDERLASTNAME FROM provider WHERE SPECIALTY = 'Orthopedic' limit 1;",
     'SQLResult': "Result of the SQL query",
     'Answer': "0"},

    {'Question': "What is the provider type for the provider named 'Makayla Ellis'?",
     'SQLQuery': "SELECT PROVIDERTYPE FROM provider WHERE PROVIDERFIRSTNAME = 'Makayla' AND PROVIDERLASTNAME = 'Ellis';",
     'SQLResult': "Result of the SQL query",
     'Answer': "DO"},

    {
        'Question': "Could you provide me with the patient IDs for all clinical encounters where the encounter type is 'CL'?",
        'SQLQuery': "select PATIENTID FROM CILINCALENCOUNTER WHERE CLINICALENCOUNTERTYPE='CL'",
        'SQLResult': "Result of the SQL query",
        'Answer': " "},

    {
        'Question': "Can you provide the patient IDs for clinical encounters where the encounter type is 'CL' and the parent context ID is 2001?",
        'SQLQuery': "select PATIENTID FROM CILINCALENCOUNTER WHERE CLINICALENCOUNTERTYPE='CL' AND CONTEXTPARENTCONTEXTID = 2001",
        'SQLResult': "Result of the SQL query",
        'Answer': " "},

    {'Question': "What is the patient's email address and their primary provider's last name?",
     'SQLQuery': "SELECT p.EMAIL, prv.PROVIDERLASTNAME FROM patient p JOIN provider prv ON p.PRIMARYPROVIDERID = prv.PROVIDERID limit 1;",
     'SQLResult': "Result of the SQL query",
     'Answer': " "},

    {'Question': "how many patient we have the name start with Shelley?",
     'SQLQuery': "select count(*) from patient where firstname like 'Shelley%'",
     'SQLResult': "Result of the SQL query",
     'Answer': "2"}

]

few_shots = [
    {'Question': "top product by revenue?",
     'SQLQuery': "SELECT m_productnum, SUM(m_fulfilled_revenue) AS total_revenue FROM sales GROUP BY m_productnum ORDER BY total_revenue DESC LIMIT 5",
     'SQLResult': "Result of the SQL query",
     'Answer': "The top product by revenue is FR4134GY-4032 with a total revenue of 871.0."},
    {'Question': "qty on hand of top selling product?",
     'SQLQuery': "SELECT a.m_productnum, a.revenue, inventory.m_qty_on_hand  from (SELECT sales.m_productnum, sum(sales.m_fulfilled_revenue) as revenue  FROM sales group by sales.m_productnum order by revenue desc limit 1) a left join  inventory   on a.m_productnum = inventory.m_part ",
     'SQLResult': "Result of the SQL query",
     'Answer': "42"},
    {'Question': "Who is the President of India?",
     'SQLQuery': '''select "The question is not relevant"''',
     'SQLResult': "Result of the SQL query",
     'Answer': "The question is not relevant"},
    {'Question': "what is the sales in the last 5 days?",
     'SQLQuery': '''SELECT sum(m_fulfilled_revenue) as total_sales FROM sales WHERE m_datefulfillment BETWEEN DATE_SUB(CURDATE(), INTERVAL 5 DAY) AND CURDATE() ''',
     'SQLResult': "Result of the SQL query",
     'Answer': "0"},
    {'Question': "Total revenue generated from fulfilled items",
     'SQLQuery': ''' SELECT SUM(m_fulfilled_revenue) AS total_revenue FROM sales WHERE m_soitem_status = 'Fulfilled'; ''',
     'SQLResult': "Result of the SQL query",
     'Answer': "4788.24"},
    {'Question': " over all revenue generated from fulfilled items?",
     'SQLQuery': ''' SELECT sum(sales.m_fulfilled_revenue) as revenue FROM sales where sales.m_datefulfillment is not null ''',
     'SQLResult': "Result of the SQL query",
     'Answer': "4788.24"},
    {'Question': "Items with a negative margin",
     'SQLQuery': '''SELECT * FROM sales WHERE m_item_margin < 0; ''',
     'SQLResult': "Result of the SQL query",
     'Answer': "null"},
    {'Question': "Number of unique sales orders",
     'SQLQuery': ''' SELECT COUNT(DISTINCT m_soid) AS num_sales_orders FROM sales;''',
     'SQLResult': "Result of the SQL query",
     'Answer': "14"},
    {'Question': "Number of units fulfilled for the Boot Barn Dorag Cap Skull ",
     'SQLQuery': "SELECT SUM(m_qtyfulfilled) AS total_qty_fulfilled FROM sales WHERE m_soitem_desc = 'Boot Barn Dorag Cap Skull';",
     'SQLResult': "Result of the SQL query",
     'Answer': "8"},
    {'Question': "Number of units fulfilled for the Boot Barn Dorag Cap Skull ",
     'SQLQuery': "SELECT SUM(m_qtyfulfilled) AS total_qty_fulfilled FROM sales WHERE m_soitem_desc = 'Boot Barn Dorag Cap Skull';",
     'SQLResult': "Result of the SQL query",
     'Answer': "8"}

]

