import streamlit as st
from PIL import Image

class Drivers():
    
    driver_list = [
        {'id': 'js981101', 'name':'Jonathan Smith', 'img':'images/SmithJ.jpg', 'testimonial':'Working with Speedy Delivers has been an absolute game-changer for my delivery career. The efficient logistics, advanced technology, and supportive team make every delivery a breeze. Proud to be part of a company that truly values its drivers.'},
        {'id': 'mb960121', 'name':'Maria Blue', 'img':'images/BlueM.jpg', 'testimonial':'Being a part of Speedy Delivers is like being part of a community. The support from the team and the respect for drivers make this company stand out. The positive work environment translates to better service for our customers.'},
        {'id': 'lt991219', 'name':'Luke Troy', 'img':'images/TroyL.jpg', 'testimonial':'Speedy Delivers is not just a delivery service; it''s a platform that empowers its drivers. The technological tools provided, coupled with fair compensation, make it a driver-centric company. Grateful to be on this journey!'},
        {'id': 'ac941230', 'name':'Adrian Cooper', 'img':'images/CooperA.jpg', 'testimonial':'Having been a part of the delivery industry for quite some time, I can confidently say that Speedy Delivers stands out. The commitment to professionalism, the user-friendly technology, and the emphasis on work-life balance make it a company that truly cares about its drivers. I''m proud to be a reliable face behind the wheel for Speedy Delivers.'},
        {'id': 'sh981014', 'name':'Scarlett Hayes', 'img':'images/HayesS.jpg', 'testimonial':'Joining the Speedy Delivers team has been a career-changing decision. The focus on safety, the supportive network of fellow drivers, and the constant innovation in logistics make this company stand out in the competitive delivery landscape. Proud to be delivering smiles with every package!'},
        {'id': 'bf900605', 'name':'Brandon Foster', 'img':'images/FosterB.jpg', 'testimonial':'I''ve been navigating the streets as a delivery driver for years, and Speedy Delivers has truly elevated my experience. The emphasis on training, the fair compensation, and the state-of-the-art delivery tools have made each shift enjoyable and rewarding. This company values its drivers, and it shows.'},
        {'id': 'mt900115', 'name':'Maria Turner', 'img':'images/TurnerM.jpg', 'testimonial':'I''ve worked with several delivery companies, but Speedy Delivers sets the bar high. The dedication to punctuality, the friendly atmosphere, and the opportunities for growth make it an ideal place for delivery professionals. Proud to wear the uniform!'},
        ]

    def disp_driver(self):
        st.set_page_config(
            page_title="Speedy Delivers | Drivers"
        )
        st.markdown("# Our Drivers")
        st.markdown("""<style>
        .st-emotion-cache-18ni7ap{
            background-color: rgb(75,171,151)
        }
        [data-testid=stSidebar]{
            background-color: rgba(75,171,151, 0.8)
        }
        </style>""", unsafe_allow_html=True)
        for driver in self.driver_list:
            container = st.container()
            container.markdown("""
            <style>
            .st-emotion-cache-ocqkz7.e1f1d6gn4{
                background-color: rgba(246, 253, 195, 0.8);
                padding:5%;
                border-radius: 15px 70px;
            }
            </style>
            """, unsafe_allow_html = True)
            img_col, txt_col = st.columns([2, 3])
            image = Image.open(driver["img"])
            img_col.image(image)
        
            txt_col.markdown(f"**{driver['name']}**")
            txt_col.markdown(f"*\"*{driver['testimonial']}*\"*")

Drivers = Drivers()
Drivers.disp_driver()