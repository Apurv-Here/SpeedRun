"""
1. YoY, MoM

2. Running sum and moving average

3. Top N

4. 


-------------------------------------------------------

1. YoY

SELECT 
    EmployeeID,
    Salary,
    SUM(Salary) OVER (PARTITION BY EmployeeID ORDER BY EmployeeID) AS RunningSum
FROM 
    Employees
ORDER BY 
    EmployeeID;

    
MoM

MoM Growth = 
VAR CurrentMonthSales = SUM(Sales[Amount])  -- Calculate current month's sales
VAR LastMonthSales = 
    CALCULATE(
        SUM(Sales[Amount]), 
        PREVIOUSMONTH('Date'[Date])  -- Get the same period from the last month
    )
RETURN
    DIVIDE(CurrentMonthSales - LastMonthSales, LastMonthSales, BLANK())  -- Calculate MoM growth and handle division by zero

    

---------------------------------------------------------------

2. Running sum and moving average

Ans.

Running Sum = 
CALCULATE(
    SUM(Sales[Amount]), 
    FILTER(
        ALL('Calendar'),  -- Adjusted to use the Calendar Table
        'Calendar'[Date] <= MAX('Calendar'[Date])  -- Use the Date column from the Calendar table
    )
)




Moving Average (12 Months) = 
CALCULATE(
    AVERAGE(Sales[Amount]), -- Replace 'Sales[Amount]' with your sales or target measure
    DATESINPERIOD(
        'Calendar'[Date], -- Replace 'Calendar' with your calendar table name
        MAX('Calendar'[Date]), -- Current date in context
        -12, -- Go back 12 months
        MONTH -- Period type is months
    )
)



DATESINPERIOD(<Date_Column>, <End_Date>, <Number_of_Periods>, <Period_Type>)



top 10 interview questions

"""