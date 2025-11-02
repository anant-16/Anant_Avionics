import streamlit as st
import random
import time

st.title("CubeSat Telemetry Dashboard")

temperature_plot = st.line_chart()
voltage_plot = st.line_chart()
current_plot = st.line_chart()

while True:
    temp = random.uniform(15, 40)
    volt = random.uniform(3.0, 4.2)
    curr = random.uniform(0.1, 2.0)
    
    temperature_plot.add_rows([temp])
    voltage_plot.add_rows([volt])
    current_plot.add_rows([curr])
    
    time.sleep(1)
