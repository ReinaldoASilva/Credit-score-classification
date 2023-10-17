# Import Libraries

import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go 
import plotly.io as pio
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
pio.templates.default = "plotly_white"

#========================================= READ DATASET ========================================================================

data = pd.read_csv("train.csv")
print(data.head())
data.info()
data.describe()
data.isnull().sum() # no null
data["Credit_Score"].value_counts()


#========================================= DATA EXPLORATION ====================================================================

# I will start by exploring the occupation feature to know if the occupation of the person affects credit scores

fig = px.box(data,
            x= "Occupation",
            color="Credit_Score",
            title="Credit Score based on ocupation",
            color_discrete_map={'Poor':"red",
                                "Standard":"yellow",
                                "Good":"green"})
fig.show(height=1000, width=1200)
# There's no much difference in the credit scores of all occupations mentioned in the data

#--------------------------------------------------------------------------------------------------------------------------

# now let's explore whether the annual income of the person impacts your credit scores or not.
fig = px.box(data,
            x="Credit_Score",
            y="Annual_Income",
            color="Credit_Score",
            title="Credit Scores Based on Annual Income",
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})

fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
#According to the above visualization, the more earn annually, the better your credit score is.

#--------------------------------------------------------------------------------------------------------------------------

# Now let's explore whether the monthy in-hand salary impacts credit score or not
fig =px.box(data,
            x="Credit_Score",
            y="Monthly_Inhand_Salary",
            color="Credit_Score",
            title='Monthly Salary vs Credit Score',
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})

fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
# Like annual income, the more monthly in-hand salary you earn, the better your credit score will become

#--------------------------------------------------------------------------------------------------------------------------

# Now let's see if having more bank accounts impacts credit score or not.
fig = px.box(data,
            x="Credit_Score",
            y="Num_Bank_Accounts",
            color="Credit_Score",
            title='Number Bank Accounts vs Credit Score',
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})

fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
# Maintaining more that five account is not good for having a good credit score. A person should have 2 or 3\
# bank accounts only. So having more bank accounts doesn't positively  impact credit scores.

#--------------------------------------------------------------------------------------------------------------------------

# Now let's see the impact on credit score based on the number of credit cards you have
fig = px.box(data,
            x="Credit_Score",
            y="Num_Credit_Card",
            color="Credit_Score",
            title='Number Credit Cards vs Credit Score',
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})
fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
# Just like the number of banks accounts, having more credit cards will not possitively impat your credit scores.\
# Having more than three credit card does not improve your credit score. It can even negatively affect it.

#--------------------------------------------------------------------------------------------------------------------------

# Now let's see the impact on credit scores based on how much average interest you pay on loans and.
fig = px.box(data,
            x="Credit_Score",
            y="Interest_Rate",
            color="Credit_Score",
            title="Average Interest Rate vs Credit Score",
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})
fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
# If average interest rate is 4% a 11% the credit score is good. Having an average interest rate of more than 15%\
# is bad for your credit scores.

#--------------------------------------------------------------------------------------------------------------------------

# Now let's see how many loans you can take at a time for good credit score.
fig=px.box(data,
            x="Credit_Score",
            y="Num_of_Loan",
            color="Credit_Score",
            title="Loan Count vs Credit Score",
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})
fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
# To have a good credit score, you should not take more than 1 - 3 loans at a time. Having more than three loans at a time\
# will negatively impact your credit scores

#--------------------------------------------------------------------------------------------------------------------------

# Now let's see if delaying payments on the due date impacts your credit socres or not
fig=px.box(data,
            x="Credit_Score",
            y="Delay_from_due_date",
            color="Credit_Score",
            title="Delay from Due Date vs Credit Score",
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})
fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
# So you can delay your credit card payment 5 - 14 days from the due date. Delaying your payments for more than 17 days\
# from the due date will impact your credit score negativelly.

#--------------------------------------------------------------------------------------------------------------------------

# Now let's have a look at if frequently delaying payments will impact credit scores or not.
fig = px.box(data,
            x="Credit_Score",
            y="Num_of_Delayed_Payment",
            color="Credit_Score",
            title="Credit Scores based on number of Delayed Payments",
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})
fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
# So delaying 4 - 12 payments from the due date will no affect your credit scores. But delaying more than 12 payments\
# from the due date will affect your credit scores negatively

#--------------------------------------------------------------------------------------------------------------------------

# Now let's see if having more debt will affect credit score or not.
fig = px.box(data,
            x="Credit_Score",
            y="Outstanding_Debt",
            color="Credit_Score",
            title="Outstanding_Debt vs Credit Score",
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})

fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
# An outstanding debt of $380 - $1150 will not affect your credit scores.  But always having a debit of more tha $1338\
# will affect your credit scores negatively.

#--------------------------------------------------------------------------------------------------------------------------

# Now let's see if having a high credit utilization ratio will affect credit scores or not. 
fig = px.box(data,
            x="Credit_Score",
            y="Credit_Utilization_Ratio",
            color="Credit_Score",
            title="Credit Scores Based on Credit Utilization Ratio",
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})
fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)                    
# According to the above figure, your credit utilization ratio doesn't affect your credit scores.abs

#--------------------------------------------------------------------------------------------------------------------------

# Now let's see how the credit history age of a person affects credit scores
fig = px.box(data,
            x="Credit_Score",
            y="Credit_History_Age",
            color="Credit_Score",
            title=" Credit Score based on credit history age",
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})
fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
# So, having a long credit history results is better credit scores.

#--------------------------------------------------------------------------------------------------------------------------

# Now let's see if your monthly investments affect your credit scores or not.
fig = px.box(data,
            x="Credit_Score",
            y="Amount_invested_monthly",
            color="Credit_Score",
            title="Credit Scores Based on Amount Invested Monthly",
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})
fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
# The amount of money you invest monthly doens't affect your credit scores.

#--------------------------------------------------------------------------------------------------------------------------

# Now let's see if having a low amount at the end of the monthly affects credit scores or not. 
fig = px.box(data,
            x="Credit_Score",
            y="Monthly_Balance",
            color="Credit_Score",
            title=" Credit Scores Based on Monthly Balance Left",
            color_discrete_map={"Poor":"red",
                                "Standard":"yellow",
                                "Good":"green"})
fig.update_traces(quartilemethod="exclusive")
fig.show(height=1000, width=1200)
# So having a high monthly balance in your account at the end of the month is good for your credit scores.A Monthly\
# balance of lesse than $250 is bad for credit scores.

#-------------------------------------------------- MODEL -------------------------------------------------------------------

# One more importante feature(Credit Mix) in the dataset is valuable for determining credit scores.
#The credit mix feature tells about the types of credits an loans you have taken.
# as the Credit_Mix column is categorical, i will transform it into a numerical feature so that we can use it to\
#train a Machine Learnig model for the task of credit score classification
data["Credit_Mix"] = data["Credit_Mix"].map({"Standard":1,
                                            "Good":2,
                                            "Bad":0})

#--------------------------------------------------------------------------------------------------------------------------

# Now I will split the data into features and labels by selecting the features we found important for our model:
x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary", 
                   "Num_Bank_Accounts", "Num_Credit_Card", 
                   "Interest_Rate", "Num_of_Loan", 
                   "Delay_from_due_date", "Num_of_Delayed_Payment", 
                   "Credit_Mix", "Outstanding_Debt", 
                   "Credit_History_Age", "Monthly_Balance"]])

y = np.array(data[["Credit_Score"]])

#--------------------------------------------------------------------------------------------------------------------------

# Now, let's split the data into traning and test sets and proceed further by traning a credit score classification model.
xtrain, xtest,ytrain,ytest = train_test_split(x,y,
                                            test_size=0.33,
                                            random_state=42)

model = RandomForestClassifier()
model.fit(xtrain,ytrain)

#--------------------------------------------------------------------------------------------------------------------------

# Now, let's make predictions from our model by giving inputs to our model according to the features we used to train the model
print("Credit Score Prediction")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))

features = np.array([[a,b,c,d,e,f,g,h,i,j,k,l]])
print("Predict Credit Score =", model.predict(features))

# Classifying customers based on their credit scores helps banks and credit card companies immediately to issue loans to \
# customers with good creditworthiness. A person with a good credit score will get loans from any bank and financial institution. 

















