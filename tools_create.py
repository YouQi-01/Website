import json
import os
from datetime import datetime

def create_article():
    # 获取用户输入
    title = input("请输入文章标题: ")
    content = input("请输入文章内容: ")
    
    # 生成文章ID和文件名
    article_id = input("请输入文章ID(留空自动生成): ") or f"article_{int(datetime.now().timestamp())}"
    filename = f"{article_id}.md"
    
    # 创建markdown文件
    filepath = os.path.join("docs", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{content}")
    
    # 更新docs.json
    json_path = os.path.join("docs", "docs.json")
    articles = []
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            articles = json.load(f)
    
    new_article = {
        "id": article_id,
        "title": title,
        "path": filename,
        "time": datetime.now().isoformat()
    }
    articles.append(new_article)
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)
    
    print(f"文章创建成功: {filename}")

if __name__ == "__main__":
    create_article()
