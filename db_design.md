- Database design
    
    - TABS (dimension)
        - Tab id
        - Total Amount
        - Description
        - created_date

    - USERS (dimension)
        - id INTEGER, 
        - name TEXT, 
        - birthday TEXT,
        - power_level INTEGER,
        - preferred_payment_method TEXT,
        - default_split_percentage REAL DEFAULT 0 (?)

    - USER_TAB_MAP (fact)
        id INTEGER,
        user_id INTEGER,
        tab_id INTEGER,
        is_recipient INTEGER,
        amount_owed REAL

    - USER_PAYMENTS_MAP (fact)
        id INTEGER,
        user_id INTEGER,
        tab_id INTEGER,
        amount REAL,
        payment_date TEXT
    
    - events
        - logging table
        - get_logs
            - print of this table from a given date range
            
    -USER_PAYMENT_STATUS (View)
    CREATE VIEW IF NOT EXISTS USER_PAYMENT_STATUS 
    AS
    WITH AGGREGATED_USER_PAYMENTS as (
        SELECT 
        u.name, 
        up.user_id,
        up.tab_id,
        SUM(CAST(up.amount as REAL)) as payment_amount
        FROM USER_PAYMENTS_MAP up 
        INNER JOIN USERS u 
            on u.user_id = up.user_id
        GROUP BY u.name, up.user_id, up.tab_id
    ),
    PAYMENT_TAB_MAPPING AS(
        SELECT 
        aup.name, 
        utm.user_id, 
        utm.tab_id, 
        utm.amount_owed,
        utm.amount_owed - COALESCE(aup.payment_amount, 0) AS amount_remaining
        FROM USER_TAB_MAP utm
        INNER JOIN AGGREGATED_USER_PAYMENTS aup 
            on aup.tab_id = utm.tab_id
            and aup.user_id = utm.user_id
    )
    Select 
    name as Name, 
    user_id as User_id,
    tab_id as Tab_Id,
    amount_owed as Amount_Owed,
    amount_remaining as amount_remaining
    FROM PAYMENT_TAB_MAPPING