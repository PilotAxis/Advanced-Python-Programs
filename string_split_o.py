import pickle
st = " "

with open(r"C:\Users\moham\Onedrive\Documents\File Handling\myfile.info", 'rb') as fh :
    st = pickle.load(fh)
    lst = st.split('o')
    print(lst[0])
