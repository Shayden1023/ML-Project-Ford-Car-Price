import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "ford.pkl")
train_columns = joblib.load(BASE_DIR / "ford_columns.pkl")