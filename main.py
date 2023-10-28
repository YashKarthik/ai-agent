from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI()
chat_model = ChatOpenAI()

text = "What kind of pizza would be good to eat right now?"

llm.predict(text)
chat_model.predict(text)

# import re
# from playwright.sync_api import Page, expect

# def test_has_title(page: Page):
#     page.goto("https://yashkarthik.xyz/")

#     expect(page).to_have_title(re.compile("Playwrite"))

# def test_get_started_link(page: Page):
#     page.goto("https://yashkarthik.xyz")
#     page.get_by_role("link", name="Projects").click()
#     expect(page.get_by_role("heading", name="Tiviem")).to_be_visible()

