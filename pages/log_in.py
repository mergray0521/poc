install streamlit as st
pip install streamlit-authenticator
import pickle
from pathlib import path

import streamlit_authenticator as stauth

names = ["Meredith Gray", "Steve Albonico"]
usernames = ["mergray", "stevealbo"]
password = ["mg123", "sa456"]

hashed_passwords= stauth.Hasher(passwords).generate()

file_path= Path(_file_).parent / "hashed_pw.pk1"
  with file_path.open("wb") as file:
      pickle.dump(hashed_passwords, file)



