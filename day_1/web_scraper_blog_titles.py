import requests
from bs4 import BeautifulSoup

# 目标 URL
url = 'https://example-blog.com'

# 发送 HTTP 请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析 HTML 内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 查找所有文章标题
    titles = soup.find_all('h2', class_='post-title')  # 假设文章标题在 h2 标签中，且类名为 post-title
    
    # 打印标题
    for idx, title in enumerate(titles, start=1):
        print(f"{idx}. {title.get_text().strip()}")
else:
    print(f"Failed to retrieve webpage. Status code: {response.status_code}")