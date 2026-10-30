from src.tools.tools import web_search, scrape_url
output = scrape_url.invoke("https://docs.langchain.com/build-overview")
print(output)