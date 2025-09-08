import requests
import json

def cpde_ollama(prompt,model='qwen3:1.7b',host="http://localhost:11434"):
    try:
        data={
            "model":model,
            "prompt":prompt,
            "stream":False, # 是否流式返回
            # "format":"json", # 响应格式
            # 模型参数
            "options":{
                # 其实就是表示 AI 输出的是保守一些的还是天马行空的
                "temperature":0.5,  # 温度  
                "top_p":0.5,  # 核采样  只输出高概率的词语，低概率的词语就不进行输出 0.5 就表示只获取最高的50%，剩下的词就不选了
                # "top_k":10,   # 核采样  只考虑概率高的词，剩下的就不选了   10 就表示只获取前 10个词，后面的就不学了
                "num_predict":1000,  # 最大预测长度  1000 就表示最大预测 1000 个词
            }
        }

        # 发送post 请求
        response = requests.post(
            url=f"{host}/api/generate",
            headers={"Content-Type":"application/json"},
            data=json.dumps(data),
            timeout=300
        )

        # 解析响应
        if response.status_code == 200:
            resp = response.json()
            return resp.get("response","未生成有效内容")
        else:
            return f"请求失败，状态码：{response.status_code}"

    except requests.exceptions.RequestException:
        return f"请求失败，状态码：{response.status_code}"
    except Exception as e:
        return f"请求失败，状态码：{e}"

if __name__ == '__main__':
    code_prompt = "请帮我生成一个输出 1-10 的python 程序"
    # 调用本地 ollama 生成这个程序
    resp = cpde_ollama(code_prompt,model='qwen3:1.7b')
    print(resp)
