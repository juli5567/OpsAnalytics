import streamlit as st
import pandas as pd
import pycaret
from pycaret.classification import *

df= pd.read_csv("https://raw.githubusercontent.com/juli5567/OpsAnalytics/main/df.csv", delimiter= ";")
# initial setup
# s = setup(data = df, target = 'y', session_id=123)
final_model=load_model('Final_Model20220212')

st.title('Term Deposit Camping - Predicting Model')
st.image('https://www.crwflags.com/fotw/images/p/pt$bpi2.gif')
st.subheader('Input Parameters for prospect customer')

age = st.number_input('Age', help='Input the age in years', min_value=1, max_value=100, step=1)
default= st.selectbox('Has credit in default? If Yes select 1, No select 0', (1,0))
balance= st.number_input('Average yearly balance', help='In euros (numeric)')
housing= st.selectbox('Has housing loan? If Yes select 1, No select 0', (1,0))
loan= st.selectbox('Has personal loan? If Yes select 1, No select 0', (1,0))
contact =  st.selectbox('Contact communication type - telephone: 1, cellular: 0', (1,0))
duration = st.number_input('Last contact duration', help='In seconds (numeric)', min_value=1, step=1)
campaign = st.number_input('Number of contacts performed during this campaign and for this client', help=('numeric, includes last contact'), min_value=0, step=1)
jobinput= st.selectbox('Type of job', ('Administration','Blue-Collar','Management','Housemaid','Entrepreneur','Retired','Services','Student','Self-employed','Technician','Unemployed', 'Unknown'))
marital = st.selectbox('Marital status', ('Married','Divorced','Single'), help= ('Divorced means Divorced or Widowed'))
education = st.selectbox('Education Level', ('Primary', 'Secondary', 'Tertiary'))
poutcome =  st.selectbox('Outcome of the previous marketing campaign', ('Success', 'Failure', 'Other', 'Unknown'))

job_admin=0
job_blue_collar=0
job_entrepreneur=0
job_housemaid=0
job_management=0
job_retired=0
job_self_employed=0
job_services=0
job_student=0
job_technician=0
job_unemployed=0

if jobinput=='Administration':
        job_admin=1        
elif jobinput=='Blue-Collar':
        job_blue_collar=1        
elif jobinput=='Entrepreneur':
        job_entrepreneur=1        
elif jobinput=='Housemaid':
        job_housemaid=1
elif jobinput=='Management':
        job_management=1
elif jobinput=='Retired':
        job_retired=1
elif jobinput=='Self-employed':
        job_self_employed=1
elif jobinput=='Services':
        job_services=1
elif jobinput=='Student':
        job_student=1
elif jobinput=='Technician':
        job_technician=1
elif jobinput=='Unemployed':
        job_unemployed=1

marital_divorced=0
marital_married=0
marital_single=0

if marital=='Married':
    marital_married=1     
elif jobinput=='Divorced':
    marital_divorced=1        
elif jobinput=='Single':
    marital_single=1 

poutcome_failure=0
poutcome_other=0
poutcome_success=0
poutcome_unknown=0

if poutcome =='Success':
    poutcome_success=1        
elif poutcome=='Failure':
    poutcome_failure=1        
elif poutcome=='Other':
    poutcome_other=1 
elif poutcome=='Unknown':
    poutcome_unknown=1

education_primary=0
education_secondary=0
education_tertiary=0

if education =='Primary':
    education_primary=1        
elif education =='Secondary':
    education_secondary=1        
elif poutcome=='Tertiary':
    education_tertiary=1 
 
df1= pd.DataFrame([[age,default,balance,housing,loan,contact,duration,campaign,job_admin,job_blue_collar,job_entrepreneur,job_housemaid,
job_management,job_retired,job_self_employed,job_services,job_student,job_technician,job_unemployed,marital_divorced,marital_married,marital_single,
education_primary,education_secondary,education_tertiary,poutcome_failure,poutcome_other,poutcome_success,poutcome_unknown]],
columns=['age','default','balance','housing','loan','contact','duration','campaign','job_admin.','job_blue-collar','job_entrepreneur','job_housemaid',
'job_management','job_retired','job_self-employed','job_services','job_student','job_technician','job_unemployed','marital_divorced','marital_married','marital_single',
'education_primary','education_secondary','education_tertiary','poutcome_failure','poutcome_other','poutcome_success','poutcome_unknown'])

prediction =predict_model(final_model, df1)
label= prediction['Label']
score= prediction['Score']
print (label)
print (score)
if label.all() == 1:
    st.metric(label="Prediction", value="Yes", delta="High Probability that the client subscribes a term deposit")
    st.metric(label="Score", value=score)
    st.caption("Precision of the prediction - Value from 0 to 1")
    st.image("https://github.com/juli5567/OpsAnalytics/raw/main/Score_range.png", caption='Score Range')
else:
    st.metric(label="Prediction", value="No", delta="-Low Probability that the client subscribes a term deposit")
    st.metric(label="Score", value=score)
    st.caption("Precision of the prediction - Value from 0 to 1")
    st.caption("Score Range")
    st.image("https://github.com/juli5567/OpsAnalytics/raw/main/Score_range.png", caption='Score Range')
