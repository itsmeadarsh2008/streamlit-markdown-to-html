import streamlit as st
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin

md = (
    MarkdownIt('commonmark', {'breaks': True, 'html': True})
    .use(front_matter_plugin)
    .use(footnote_plugin)
    .enable('table')
    .enable('strikethrough')  # Enable table support
)

def markdown_to_html(markdown_text, css_content):
    html_content = md.render(markdown_text)
    complete_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Produced by Streamlit Markdown To HTML</title>
        <style>
            {css_content}
        </style>
    </head>
    <body class="markdown-body">
        {html_content}
    </body>
    </html>
    """
    return complete_html
# Read external CSS file
with open("styles.css", "r", encoding="utf-8") as css_file:
    css_content = css_file.read()
    css_file.close()


def main():
    st.title("Multiple Markdown to HTML Converter")
    columns1, column2 = st.columns(2)
    with columns1:
        uploaded_files = st.file_uploader(
        "Upload multiple Markdown files", type=["md"], accept_multiple_files=True)
        if uploaded_files:
            for uploaded_file in uploaded_files:
                try:
                    # Read uploaded Markdown file with utf-8 encoding
                    markdown_text = uploaded_file.read().decode("utf-8")
                    # Convert Markdown to HTML
                    html_output = markdown_to_html(markdown_text, css_content)
                    st.success("Conversion successful", icon="✅")
                except:
                    st.exception("Conversion failed")
                # Add a download button for the HTML file with utf-8 encoding
                st.download_button(
                    label=f"Download {uploaded_file.name.split('.')[0]}.html",
                    data=html_output.encode("utf-8"),
                    file_name=f"{uploaded_file.name.split('.')[0]}.html",
                    mime="text/html",
                    on_click=st.balloons,
                )
        st.markdown('''
![Python](https://img.shields.io/badge/MADE%20WITH%20PYTHON-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
                    
Welcome to our Streamlit Markdown to HTML Converter, where converting your Markdown files to HTML is a breeze! With our user-friendly interface and seamless functionality, you can transform your Markdown documents into HTML without a hitch. We understand the need for convenience, so we allow you to upload your Markdown files directly, eliminating the hassle of copying and pasting.
- **Effortless Upload ✨**
- **High-Speed Processing ⚡**
- **User-Friendly Interface 😊**
- **Customization Options 🎨**
- **Secure & Reliable 🔒 (Nothing is stored)**
- **Cross-Platform Compatibility 🌐**
- **Free Forever🆓**''')
    with column2:
        st.markdown('''<iframe src="https://nowpayments.io/embeds/donation-widget?api_key=2166K58-CTAMFFB-P8FYBJP-ZK66TW6&source=lk_donation&medium=referral" frameborder="0" scrolling="no" style="overflow-y: hidden;" width="354" height="680"></iframe>''',unsafe_allow_html=True)
    '''
    # Why Convert with Us?

    Markdown to HTML is a versatile tool that seamlessly transforms plain text notes into visually appealing and colorful web content. By converting markdown syntax into HTML code, it enhances readability and aesthetics. Users can create stunning documents, blogs, or websites effortlessly, adding vibrancy to their content while maintaining simplicity in the editing process. 🎨✨📝
    Experience the convenience of uploading your Markdown files and getting instant HTML output. Try our Streamlit Markdown to HTML Converter now and elevate your document processing efficiency!

    # Key Points
    1. **Effortless Upload:** Simply upload your Markdown file, and our converter will process it instantly. No manual copying and pasting required, ensuring a smooth experience.
    2. **High-Speed Processing:** Experience swift and efficient conversion. Your HTML file will be ready in no time, allowing you to focus on your tasks without delays.
    3. **User-Friendly Interface:** Our intuitive design ensures that anyone, regardless of technical expertise, can use our converter with ease. No steep learning curves here!
    4. **Customization Options:** Tailor your HTML output according to your preferences. Enjoy various formatting options and styles to make your content stand out.
    5. **Secure and Reliable:** Nothing is stored on our server.
    6. **Cross-Platform Compatibility:** Access our converter from any device or operating system. Whether you're using a computer, tablet, or smartphone, enjoy a seamless conversion experience.
    '''
if __name__ == "__main__":
    main()