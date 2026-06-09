from pathlib import Path
import base64

css_path = Path(r'C:/Users/Nick/Documents/Sample/design-to-web-hug/src/styles.css')
font_path = Path(r'C:/Users/Nick/Documents/Sample/design-to-web-hug/public/fonts/Timeless-Bold.ttf')
text = css_path.read_text(encoding='utf-8')
font_data = 'data:font/truetype;base64,' + base64.b64encode(font_path.read_bytes()).decode('ascii')

old1 = '''@font-face {
  font-family: "Timeless";
  src: url("/fonts/Timeless-Bold.ttf") format("truetype");
  font-weight: bold;
  font-style: normal;
}
'''
old2 = '''@font-face {
  font-family: 'Timeless';
  src: url('/fonts/Timeless-Bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
'''
new = f'''@font-face {{
  font-family: "Timeless";
  src: url("{font_data}") format("truetype");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}}
'''

if old1 in text:
    text = text.replace(old1, new)
elif old2 in text:
    text = text.replace(old2, new)

text = text.replace(
    'font-family: "Timeless", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;',
    'font-family: "Timeless" !important;'
)
text = text.replace('font-weight: 600;', 'font-weight: 700 !important;')

css_path.write_text(text, encoding='utf-8')
