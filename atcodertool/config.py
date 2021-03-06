import toml
import os

CONFIG_PATH = os.path.expanduser("~/.config/atcoder-tool.toml")
default_config = {
    "language": {
        "lang": "C++",
        "filename_ext": ".cpp",
        "compiling": True,
        "compile_cmd": "g++",
        "compile_opt": "-std=c++17",
        "exe_cmd": "./a.out",
    },
    "session": {
        "username": "",
        "cookie_file_path": "~/.cache/atcoder_tool_session.dump"
    },
    "template": {
        "template":""
    }
}
def config_update(newconfig):
    toml.dump(newconfig, open(CONFIG_PATH, mode="w"))

def read_config():
    if os.path.exists(CONFIG_PATH):
        config =  toml.load(open(CONFIG_PATH))
    else:
        config = default_config
        config_update(config)
    return config