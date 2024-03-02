import streamlit as st
from streamlit_option_menu import option_menu
import input_output_2x2, input_output_3x3, About, Application,Home

class MultiPurpose:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):

        self.apps.append({
            "title": title,
            "function": function
        })
    def run():

        with st.sidebar:        
            app = option_menu(
                menu_title='MENU',
                options=['Home',"Application",'About'],
                icons=['house','app-indicator','person-circle','app-indicator'],
                menu_icon='menu-button-wide',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#12ab21"}}
                
                )
        if app == 'Home':
            Home.app()
        if app == "Application":
            Application.app()
        if app == 'About':
            About.app() 
       
             
    run() 