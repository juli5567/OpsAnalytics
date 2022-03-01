# Classification App - Pycaret & Streamlit

### Context
Term deposits are a major source of income for a bank. A term deposit is a cash investment held at a financial institution. Your money is invested for an agreed rate of interest over a fixed amount of time, or term. The bank has various outreach plans to sell term deposits to their customers such as email marketing, advertisements, telephonic marketing, and digital marketing.

Telephonic marketing campaigns still remain one of the most effective way to reach out to people. However, they require huge investment as large call centers are hired to actually execute these campaigns. Hence, it is crucial to identify the customers most likely to convert beforehand so that they can be specifically targeted via call.

The data used to create the classification model is related to direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification application goal is to predict the probability of the client to subscribe a term deposit.

#### Detailed Column Descriptions
bank client data:

1 - age (numeric)

2 - job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student",
"blue-collar","self-employed","retired","technician","services")

3 - marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)

4 - education (categorical: "unknown","secondary","primary","tertiary")

5 - default: has credit in default? (binary: "yes","no")

6 - balance: average yearly balance, in euros (numeric)

7 - housing: has housing loan? (binary: "yes","no")

8 - loan: has personal loan? (binary: "yes","no")
#### Related with the last contact of the current campaign:

9 - contact: contact communication type (categorical: "unknown","telephone","cellular")

10 - day: last contact day of the month (numeric)

11 - month: last contact month of year (categorical: "jan", "feb", "mar", …, "nov", "dec")

12 - duration: last contact duration, in seconds (numeric)
#### Other attributes:
13 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)

14 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)

15 - previous: number of contacts performed before this campaign and for this client (numeric)

16 - poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

Output variable (desired target):
17 - y - Will the client subscribe a term deposit? (binary: "Yes","No")

### Classification Model

Using Pycaret all the calssification models including in the library were tested to choose one with the best scoring.

![image](https://user-images.githubusercontent.com/80360561/156089058-e78ecc16-9729-4647-be86-93a19e463d09.png)
![image](https://user-images.githubusercontent.com/80360561/156089621-72435278-293a-4bd9-994b-3ed30568747e.png)
![image](https://user-images.githubusercontent.com/80360561/156089660-9b6719ec-2a6e-4d54-9a90-00f10631cced.png)
![image](https://user-images.githubusercontent.com/80360561/156089695-335a93bd-9109-4b76-acc8-2413ee9caa81.png)



### Web Application (Streamlit)
Link:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/juli5567/opsanalytics/main/app.py)

![image](https://user-images.githubusercontent.com/80360561/156090579-7f39d07b-ff19-4b50-80b9-7f210a1865bb.png)
![image](https://user-images.githubusercontent.com/80360561/156090484-8e717935-e592-4353-8763-7c8a38b676f7.png)


