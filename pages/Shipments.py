import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
import numpy as np
from fpdf import FPDF
from datetime import datetime, timedelta

class Shipment:
    
    def shipment(self):        
        st.set_page_config(
            page_title="Speedy Delivers | Shipments",
            page_icon="👋",
        )
        st.markdown("# Shipments")
        st.markdown("""<style>
            .st-emotion-cache-18ni7ap{
            background-color: rgb(75,171,151)
            }
            [data-testid=stSidebar]{
                background-color: rgba(75,171,151, 0.8)
            }
            </style>""", unsafe_allow_html=True)
        
        self.conn = st.connection('shipments_db', type='sql')
        with self.conn.session as s:
            s.execute('CREATE TABLE IF NOT EXISTS shipments (shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,  sender TEXT, recipient TEXT, destination TEXT, order_date DATE, status DEFAULT "Awaiting Delivery");')
            s.commit()
        

        tab1, tab2, tab3 = st.tabs(["Add Shipment", "Track Shipment", "All Shipments"])
        
        with tab1:
            st.header("Add New Shipment!")
            st.write("Enter shipment details for the new shipment.")
            with st.form("Enter Shipment Details", clear_on_submit=True):
                sender = st.text_input('Sender')
                recipient = st.text_input('Recipient')
                delivery_address = st.text_input('Address')
                order_date = st.text_input('Order Date')
                submit = st.form_submit_button("Submit")
            if submit:
                st.cache_data.clear()
                with self.conn.session as s:
                    s.execute('INSERT INTO shipments (sender, recipient, destination, order_date) VALUES (:sender, :rec, :dest, :order_date);', params=dict(sender = sender, rec = recipient, dest = delivery_address, order_date = order_date))
                    # s.execute('CREATE TABLE IF NOT EXISTS shipments (shipment_id INTEGER NOT NULL, sender VARCHAR, recipient VARCHAR, destination VARCHAR, status VARCHAR DEFAULT ''In_Warehouse'', PRIMARY KEY (shipment_id))')
                    # s.execute('INSERT INTO shipments (shipment_id, sender, receiver, destination, status) VALUES (12221, ''Pratistha'', ''Anna'', ''HSM112'', ''Delivered'')')
                    s.commit()
            
        with tab2:
            st.header("Track Your Shipment!")
            st.write("Enter your tracking id to track your shipment.")
            with st.form("Track Your Shipment"):
                tracking_id = st.text_input("Tracking Id")
                submit = st.form_submit_button("Track")
            if submit:
                shipment_det = self.conn.query('select * from shipments where shipment_id = :s_id', params=dict(s_id=tracking_id))
                df = pd.DataFrame(shipment_det)
                st.dataframe(df)
        
        with tab3:
            st.header("All Shipments")
            self.get_all_shipments()
            with st.form('clear'):
                clear = st.form_submit_button("Clear DB")
            if clear:
                st.cache_data.clear()
                with self.conn.session as s:
                    s.execute('DELETE FROM shipments;')
                    s.commit()
            
            with st.form('Export Shipments DB!'):
                period = st.selectbox('Select Time Range', ('Last 7 Days', 'Last 30 Days', 'All'))
                export = st.form_submit_button("Export to CSV")
                pdf = FPDF(orientation="P", unit="mm", format="A4")
                pdf.add_page()
                pdf.set_font("Helvetica", size=12)
                pdf.image("images/logo.png", 10, 8, 33)
                pdf.cell(80)
                pdf.cell(50, 10, "Shipments Record", border=2, align="C")
                pdf.ln(20)
                pdf.cell(80)
                if period == 'Last 7 Days':
                    shipments_hist = self.conn.query('SELECT * FROM shipments WHERE order_date BETWEEN date(\'now\', \'-7 days\') AND date(\'now\');')
                    df = pd.DataFrame(shipments_hist)   
                    date_now = datetime.now().date()
                    date_from = date_now - timedelta(days=7)
                    pdf.cell(50, 10, f'From {str(date_from)} to {str(date_now)}', align="C")               
                elif period == 'Last 30 Days':
                    shipments_hist = self.conn.query('SELECT * FROM shipments WHERE order_date BETWEEN date(\'now\', \'-30 days\') AND date(\'now\');')
                    df = pd.DataFrame(shipments_hist)
                    date_now = datetime.now().date()
                    date_from = date_now - timedelta(days=30)
                    pdf.cell(50, 10, f'From {str(date_from)} to {str(date_now)}', align="C")  
                elif period == 'All':
                    shipments_hist = self.conn.query('SELECT * FROM shipments;')
                    df = pd.DataFrame(shipments_hist)
                    date_now = datetime.now().date()
                    pdf.cell(50, 10, f'All records up to {str(date_now)}', align="C")  
                

                pdf.ln(20)
                
                with pdf.table() as table:
                    headers = df.columns.tolist()
                    rows = df.values.tolist()
                    print('headers:', headers, 'rows:', rows)
                    header_row = table.row()
                    for header in headers:
                        header_row.cell(header)
                    for df_row in rows:
                        row = table.row()
                        for value in df_row:
                            row.cell(str(value))
                pdf.ln(20)
                pdf.set_font("Helvetica", size=8)
                pdf.write_html("""
                    <i>Speedy Delivers 2023</i>
                    <br><a href="https://github.com/kansakarpratistha/StreamlitApp.git" style="text-decoration: none;">Github repository</a>"""
                )
                pdf.output('shipment_data.pdf')

            self.shipments_map()

    @st.cache_data(ttl=3600) #caching data upto 3600 seconds, i.e. 1 hour
    def get_all_shipments(_self):
        all_shipments = _self.conn.query('select * from shipments')
        df = pd.DataFrame(all_shipments)
        data_ed = st.data_editor(df,
            column_config = {
                "shipment_id" : "Shipment Id",
                "sender" : "Sender",
                "recipient" : "Recipient",
                "destination" : "Delivery Address",
                "order_date" : "Order Date",
                "status" : st.column_config.SelectboxColumn('Status', options = ('Awaiting Delivery', 'Out for Delivery', 'Delivered', 'Could not be Delivered'), required = True)
            },
            key = "shipment_key",
            use_container_width=False, 
            num_rows = "fixed", 
            disabled=("shipment_id", "sender", "recipient", "destination"),
            on_change= _self.update_data,
            args = ["shipment_key", df]
            ) 
    
    def update_data(self, key_name, df):
        new_state = st.session_state[key_name]
        print(new_state['edited_rows'])
        for key, value in new_state['edited_rows'].items():
            shipment_id = df.loc[key]['shipment_id']
            for chg in value.items():
                print(chg)
                ch_col, ch_val = chg
                with self.conn.session as s:
                    s.execute(f'UPDATE shipments SET {ch_col} = "{ch_val}" WHERE shipment_id = {shipment_id}')
                    s.commit()

    def shipments_map(self):
        geolocator = Nominatim(user_agent='Speedy Delivers')
        shipment_loc = (self.conn.query('select destination from shipments').values).tolist()
        print(type(shipment_loc))
        lon = []
        lat = []
        for loc in shipment_loc:
            location = geolocator.geocode(loc)
            lon.append(location.longitude)
            lat.append(location.latitude)
        print(lat, lon)
        df = pd.DataFrame({'lat': lat, 'lon': lon})
        st.map(df, size=10)

    def track_shipment(self, tracking_id):
        pass

Shipment = Shipment()
Shipment.shipment()