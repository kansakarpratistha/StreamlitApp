import streamlit as st
from PIL import Image
import pandas as pd
import io
class Drivers():
    # driver_list = [
    #     {'name':'Jonathan Smith', 'img':'images/SmithJ.jpg', 'testimonial':'Working with Speedy Delivers has been an absolute game-changer for my delivery career. The efficient logistics, advanced technology, and supportive team make every delivery a breeze. Proud to be part of a company that truly values its drivers.', 'rating':4},
    #     {'name':'Maria Blue', 'img':'images/BlueM.jpg', 'testimonial':'Being a part of Speedy Delivers is like being part of a community. The support from the team and the respect for drivers make this company stand out. The positive work environment translates to better service for our customers.', 'rating':5},
    #     {'name':'Luke Troy', 'img':'images/TroyL.jpg', 'testimonial':'Speedy Delivers is not just a delivery service; it''s a platform that empowers its drivers. The technological tools provided, coupled with fair compensation, make it a driver-centric company. Grateful to be on this journey!', 'rating':4},
    #     {'name':'Adrian Cooper', 'img':'images/CooperA.jpg', 'testimonial':'Having been a part of the delivery industry for quite some time, I can confidently say that Speedy Delivers stands out. The commitment to professionalism, the user-friendly technology, and the emphasis on work-life balance make it a company that truly cares about its drivers. I''m proud to be a reliable face behind the wheel for Speedy Delivers.', 'rating':4},
    #     {'name':'Scarlett Hayes', 'img':'images/HayesS.jpg', 'testimonial':'Joining the Speedy Delivers team has been a career-changing decision. The focus on safety, the supportive network of fellow drivers, and the constant innovation in logistics make this company stand out in the competitive delivery landscape. Proud to be delivering smiles with every package!', 'rating':4},
    #     {'name':'Brandon Foster', 'img':'images/FosterB.jpg', 'testimonial':'I''ve been navigating the streets as a delivery driver for years, and Speedy Delivers has truly elevated my experience. The emphasis on training, the fair compensation, and the state-of-the-art delivery tools have made each shift enjoyable and rewarding. This company values its drivers, and it shows.', 'rating':5},
    #     {'name':'Maria Turner', 'img':'images/TurnerM.jpg', 'testimonial':'I''ve worked with several delivery companies, but Speedy Delivers sets the bar high. The dedication to punctuality, the friendly atmosphere, and the opportunities for growth make it an ideal place for delivery professionals. Proud to wear the uniform!', 'rating':5}
    # ]

    def disp_driver(self):
        st.set_page_config(
            page_title="Speedy Delivers | Drivers"
        )
        self.conn = st.connection('testimonials_db', type='sql')
        with self.conn.session as s:
            s.execute('CREATE TABLE IF NOT EXISTS testimonials (name TEXT NOT NULL, img VARCHAR, testimonial TEXT NOT NULL, rating NUMBER);')
            s.commit()
        st.markdown("# Our Drivers")
        st.markdown("""<style>
            .st-emotion-cache-18ni7ap{
                background-color: rgb(75,171,151)
            }
            [data-testid=stSidebar]{
                background-color: rgba(75,171,151, 0.8)
            }
            </style>""", unsafe_allow_html=True)
        tab1, tab2 = st.tabs(['Testimonials', 'Add Testimonials'])
        with tab1:
            all_testimonials = self.conn.query('select * from testimonials')
            df = pd.DataFrame(all_testimonials)
            for index, row in df.iterrows():
                container = st.container()
                container.markdown("""
                <style>
                    img{
                        width: 250px; height: 250px; object-fit: cover;
                    }
                    .st-emotion-cache-ocqkz7.e1f1d6gn4{
                    background-color: rgba(246, 253, 195, 0.8);
                    padding:5%;
                    border-radius: 15px 70px;
                    }
                </style>
                """, unsafe_allow_html = True)
                img_col, txt_col = st.columns([2, 3])
                image = Image.open(io.BytesIO(row['img']))
                img_col.image(image)
        
                txt_col.markdown(f"**{row['name']}**")
                txt_col.markdown(f"Experience Rating: {row['rating']} out of 5")
                txt_col.markdown(f"*\"*{row['testimonial']}*\"*")
                
            # for driver in self.driver_list:
            #     container = st.container()
            #     container.markdown("""
            #     <style>
            #         .st-emotion-cache-ocqkz7.e1f1d6gn4{
            #         background-color: rgba(246, 253, 195, 0.8);
            #         padding:5%;
            #         border-radius: 15px 70px;
            #         }
            #     </style>
            #     """, unsafe_allow_html = True)
            #     img_col, txt_col = st.columns([2, 3])
            #     image = Image.open(driver["img"])
            #     img_col.image(image)
        
            #     txt_col.markdown(f"**{driver['name']}**")
            #     txt_col.markdown(f"*\"*{driver['testimonial']}*\"*")
        
        with tab2:
            with st.form("Add testimonal", clear_on_submit = True):
                driver_name = st.text_input("Driver Name")
                driver_testimonial = st.text_area("What do you have to say about working with SpeedyDelivers?")
                rating = st.slider("Rate your experience as a SpeedyDelivers driver", 0, 5)
                uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg"], help="Upload a picture (png) clearly showing your face")
                st.form_submit_button("Submit", on_click=self.add_testimonial, args=(driver_name, driver_testimonial, rating, uploaded_file))
                              
                
            # if uploaded_file is not None:
            #     uploaded_image = Image.open(uploaded_file)
            #     img_col.image(uploaded_image)

    def add_testimonial(self, driver_name, driver_testimonial, rating, uploaded_file): 
        # with open(os.path.join("Data", uploaded_file.name), "wb") as f:
        #     f.write(uploaded_file.getbuffer())
        #     return st.success("Saved File:{} to Data".format(uploaded_file.name))
        # uploaded_image = Image.open(uploaded_file)
        # b="images/BlueM.jpg"
        if uploaded_file is not None:
            f = uploaded_file.read()
            b = bytearray(f)
        #     print(b)
        with self.conn.session as s:
            s.execute('INSERT INTO testimonials (name, img, testimonial, rating) VALUES (:name, :img, :testimonial, :rating);', params = dict(name=driver_name, img=b, testimonial=driver_testimonial, rating=rating))
            s.commit()    
        st.cache_data.clear()
        # st.write(driver_name)
        # st.write(driver_testimonial)
        # st.write(rating)  
        # st.write(uploaded_file)

Drivers = Drivers()
Drivers.disp_driver()

