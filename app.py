import pickle
import streamlit as st 


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_note_authentication(Glucose,Bp,Insulin,BMI):
    prediction=classifier.predict([[Glucose,Bp,Insulin,BMI]])
    print(prediction)
    return prediction

def main():
    st.title("Diabetes Prediction")
    Glucose = st.text_input("Glucose")
    Bp = st.text_input("Bp")
    Insulin = st.text_input("Insulin")
    BMI = st.text_input("BMI")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Glucose,Bp,Insulin,BMI)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()
    
    
    
