llm_model_dict = {
    "chatglm-6b": {
        "local_model_path": "THUDM/chatglm-6b",
        "api_base_url": "http://localhost:8888/v1",  # "name"修改为fastchat服务中的"api_base_url"
        "api_key": "EMPTY"
    },

    "chatglm2-6b": {
        "local_model_path": "/home/doo/ChatGLM2-6B/chatglm2-6b",
        "api_base_url": "http://localhost:8888/v1",  # URL需要与运行fastchat服务端的server_config.FSCHAT_OPENAI_API一致
        "api_key": "EMPTY"
    },

    "chatglm2-6b-32k": {
        "local_model_path": "THUDM/chatglm2-6b-32k",  # "THUDM/chatglm2-6b-32k",
        "api_base_url": "http://localhost:8888/v1",  # "URL需要与运行fastchat服务端的server_config.FSCHAT_OPENAI_API一致
        "api_key": "EMPTY"
    },
}

print(type(llm_model_dict))

object()
