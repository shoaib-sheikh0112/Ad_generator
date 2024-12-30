from PIL import Image, ImageDraw, ImageFont
import textwrap
import google.generativeai as genai
import streamlit as st

#Generating captions of the ad using google-gemini
genai.configure(api_key="AIzaSyB6EN4Nt7u-M-R_DgXFNgRPUsyVff6bOGo")
def caption_gemini(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt])
    return response.text

theme = st.sidebar.text_input("Enter Ad Theme:")
prompt = f"generate a catchy caption for speaker brand, for {theme} in 13 words (your caption is printing directly on the ad so don't use brand name and all)"
caption = caption_gemini(prompt)

ads = {
    "size1": {"dimensions": (320, 50), "creative_dimensions": (640, 100), "template": "template1"},
    "size2": {"dimensions": (300, 250), "creative_dimensions": (600, 500), "template": "template2"},
    "size3": {"dimensions": (728, 90), "creative_dimensions": (1456, 180), "template": "template3"},
    "size4": {"dimensions": (414, 125), "creative_dimensions": (828, 250), "template": "template4"},
}

try:
    font1 = ImageFont.truetype("Lora\Lora-VariableFont_wght.ttf", size=20) #Font which i am using is Lora
    font2 = ImageFont.truetype("Lora\static\Lora-BoldItalic.ttf", size=20)  

except IOError:
    print("Font file not found. Using default font.")
    font1 = ImageFont.load_default()
    font2 = ImageFont.load_default()

st.title("Ad Generator")
st.sidebar.header("Ad Sizes")

selected_size = st.sidebar.selectbox("Select Ad Size:", list(ads.keys()))
if st.sidebar.button("Generate Ad"):
    if selected_size in ads:
        ad = ads[selected_size]
        original_dimensions = ad["dimensions"]
        creative_dimensions = ad["creative_dimensions"]
        template = ad["template"]

        blank_image = Image.new('RGB', creative_dimensions, color='snow')

        try:
            product_image = Image.open("D:/Ads_generation/product_image.jpeg")

            product_width = int(creative_dimensions[0] * 0.3) # Here i am using 30% width of the ad size and 60% height
            product_height = int(creative_dimensions[1] * 0.6)  
            resized_product_image = product_image.resize((product_width, product_height))

            draw = ImageDraw.Draw(blank_image)

            if template == "template1":
                position = (
                    (creative_dimensions[0] - product_width) // 2,
                    (creative_dimensions[1] - product_height) // 2,
                )
                blank_image.paste(resized_product_image, position)

                caption_position = (20, creative_dimensions[1] - 97) 
                wrapped_caption = textwrap.fill(caption, width=23)  
                draw.text(caption_position, wrapped_caption, fill="black", font=font2)
                
                button_width = 110 
                button_height = 35  
                button_position = (creative_dimensions[0] - button_width - 20, creative_dimensions[1] - 50) 
                draw.ellipse(
                    [button_position, (button_position[0] + button_width, button_position[1] + button_height)],
                    fill="yellow"
                )
                draw.text(
                    (creative_dimensions[0] - button_width - 15, creative_dimensions[1] - 50), 
                    "Shop Now",
                    fill="red", 
                    font=font1
                )

                draw.text(
                    (creative_dimensions[0] - 200, creative_dimensions[1] - 90),
                    '''Best Deals of the 
Season! ''',
                    fill="blue",
                    font=font1,    
                )

            elif template == "template2":
        
                position = (60, (creative_dimensions[1] - product_height) // 2)
                blank_image.paste(resized_product_image, position)

                caption_position = (20, creative_dimensions[1] - 480)
                wrapped_caption = textwrap.fill(caption, width=40) 
                draw.text(caption_position, wrapped_caption, fill="black", font=ImageFont.truetype("Lora\static\Lora-BoldItalic.ttf", size=25))

                button_width = 140 
                button_height = 40 
                button_position = (creative_dimensions[0] - button_width - 150, creative_dimensions[1] - 200) 
                draw.ellipse(
                    [button_position, (button_position[0] + button_width, button_position[1] + button_height)],
                    fill="yellow" 
                )
                draw.text(
                    (creative_dimensions[0] - button_width - 130, creative_dimensions[1] - 200), 
                    "Shop Now",
                    fill="red",
                    font=font1
                )
                draw.text(
                    (creative_dimensions[0] - 300, creative_dimensions[1] - 350),
                    '''Best Deals of the season!
    Get assured discount on 
            all Products

            ''',
                    fill="blue",
                    font=ImageFont.truetype("Lora\Lora-VariableFont_wght.ttf", size=23), )  
                draw.text(
                    (creative_dimensions[0] - 480, creative_dimensions[1] - 90),
                    '''JBL: Engineered for Emotion ''',
                    fill="blue",
                    font=ImageFont.truetype("Lora\Lora-VariableFont_wght.ttf", size=25),  )


            elif template == "template3":
                position = (
                    (creative_dimensions[0] - product_width) // 2,
                    (creative_dimensions[1] - product_height) // 2,
                )
                blank_image.paste(resized_product_image, position)

                caption_position = (20, creative_dimensions[1] - 130)  
                wrapped_caption = textwrap.fill(caption, width=40)  
                draw.text(caption_position, wrapped_caption, fill="black", font=ImageFont.truetype("Lora\static\Lora-BoldItalic.ttf", size=25))
                
                button_width = 110 
                button_height = 35  
                button_position = (creative_dimensions[0] - button_width - 50, creative_dimensions[1] - 50) 
                draw.ellipse(
                    [button_position, (button_position[0] + button_width, button_position[1] + button_height)],
                    fill="yellow"
                )
                draw.text(
                    (creative_dimensions[0] - button_width - 45, creative_dimensions[1] - 50), 
                    "Shop Now",
                    fill="red", 
                    font=font1
                )
                draw.text(
                    (creative_dimensions[0] - 500, creative_dimensions[1] - 100),
                    '''Best Deals of the Season! 
            Get assured discount on 
                all Products''',
                    fill="blue",
                    font=ImageFont.truetype("Lora\Lora-VariableFont_wght.ttf", size=23),    
                )
                draw.text(
                    (creative_dimensions[0] - 500, creative_dimensions[1] - 160),
                    '''Live Louder with JBL''',
                    fill="blue",
                    font=ImageFont.truetype("Lora\Lora-VariableFont_wght.ttf", size=27),  )
                
            elif template == "template4":
                position = (
                    (creative_dimensions[0] - product_width) // 2,
                    (creative_dimensions[1] - product_height) // 2,
                )
                blank_image.paste(resized_product_image, position)

                caption_position = (20, creative_dimensions[1] - 200)
                wrapped_caption = textwrap.fill(caption, width=23)  
                draw.text(caption_position, wrapped_caption, fill="black", font=ImageFont.truetype("Lora\static\Lora-BoldItalic.ttf", size=25))
                
                button_width = 110 
                button_height = 35  
                button_position = (creative_dimensions[0] - button_width - 20, creative_dimensions[1] - 50)
                draw.ellipse(
                    [button_position, (button_position[0] + button_width, button_position[1] + button_height)],
                    fill="yellow"  
                )
                draw.text(
                    (creative_dimensions[0] - button_width - 15, creative_dimensions[1] - 50), 
                    "Shop Now",
                    fill="red", 
                    font=font1
                )
                draw.text(
                    (creative_dimensions[0] - 300, creative_dimensions[1] - 150),
                    '''Best Deals of the Season! 
            Get assured discount on 
                all Products''',
                    fill="blue",
                    font=ImageFont.truetype("Lora\Lora-VariableFont_wght.ttf", size=20),    
                )
                draw.text(
                    (creative_dimensions[0] - 300, creative_dimensions[1] - 220),
                    '''Live Louder with JBL''',
                    fill="black",
                    font=ImageFont.truetype("Lora\Lora-VariableFont_wght.ttf", size=26),  )

            final_image = blank_image.resize(original_dimensions, Image.LANCZOS)
            st.image(final_image, caption=f"Generated Ad ({selected_size})")
            final_image.save(f"ad_{selected_size}.png")
            final_image.show()

        except FileNotFoundError:
            print("The product image file was not found. Please check the file path.")

    else:
        print("Invalid size selection. Please choose from the available sizes.")