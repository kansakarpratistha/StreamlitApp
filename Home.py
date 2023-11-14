import streamlit as st 
from PIL import Image
def main():
    image = Image.open("images/logo.png")
    st.set_page_config(
    page_title="Speedy Delivers | Home",
    page_icon= image
    )
#     st.markdown("""
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
#     """, unsafe_allow_html=True)
#     st.markdown("""
#     <nav class="navbar fixed-top navbar-expand-lg bg-body-tertiary">
#   <div class="container-fluid">
#     <a class="navbar-brand" href="#">Navbar</a>
#     <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
#       <span class="navbar-toggler-icon"></span>
#     </button>
#     <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
#       <div class="navbar-nav">
#         <a class="nav-link active" aria-current="page" href="#">Home</a>
#         <a class="nav-link" href="#">Features</a>
#         <a class="nav-link" href="#">Pricing</a>
#         <a class="nav-link disabled" aria-disabled="true">Disabled</a>
#       </div>
#     </div>
#   </div>
# </nav>
#     """, unsafe_allow_html=True)
    st.markdown("""
    <style>
    .st-emotion-cache-18ni7ap{
        background-color: rgb(75,171,151)
    }
    [data-testid=stSidebar]{
        background-color: rgba(75,171,151, 0.8)
    }
    </style>""", unsafe_allow_html=True)
    
    col1, _, col2 = st.columns([1, 1, 20])
    with col1:
        st.markdown("""<style>
            padding-top: 2%
        </style>""", unsafe_allow_html=True)
        st.image('images/logo.png', width=60)
    with col2:
        st.title("Welcome to Speedy Delivers!")

    intro_txt = r'''At Speedy Delivers, we understand that timely and secure delivery 
    is the lifeline of businesses and individuals alike. With a commitment to 
    excellence and efficiency, we have positioned ourselves as a leading force in the 
    delivery industry. '''
    st.write(intro_txt)

    st.header("Our Mission")
    mission_txt = '''Our mission is simple yet profound - to connect people and 
    businesses by providing seamless and reliable delivery services. Whether you're a 
    small business looking to expand your reach or an individual in need of a swift and 
    secure delivery solution, Speedy Delivers is here to serve you.'''
    st.write(mission_txt)

    st.subheader("Why Choose Speedy Delivers?")
    why_txt = '''**1. Reliability**  
    We pride ourselves on being a delivery partner you can 
    trust. Our dedicated team works tirelessly to ensure that your packages reach their 
    destination safely and on time, every time.    
    \n**2. Technology-Driven Solutions**  
    Harnessing the power of cutting-edge technology, we streamline the delivery process
    for maximum efficiency. Track your packages in real-time, receive notifications, 
    and experience the convenience of modern logistics.  
    \n**3. Customer-Centric Approach**  
    Your satisfaction is our priority. Our customer support team is ready to assist you
    with any inquiries or concerns. We believe in open communication and transparency 
    throughout the delivery journey.  
    \n**4. Wide Range of Services**  
    From same-day deliveries to customized logistics solutions, we offer a diverse 
    range of services tailored to meet your unique needs. No delivery is too big or too 
    small for Speedy Delivers.
    '''
    st.markdown(why_txt)
        
    st.subheader("Experience Excellence in Every Delivery")
    end_txt = '''Discover a new standard of delivery services with Speedy Delivers. 
    We're not just a delivery company; we're your reliable partner in connecting people 
    and businesses through the art of efficient logistics.  
    \nThank you for choosing Speedy Delivers. Let's deliver success together!
    '''
    st.markdown(end_txt)

if __name__ == "__main__":
    main()