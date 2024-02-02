import os
import openai
import copy
import glob
import shutil
openai.api_key = os.getenv("OPENAI_API_KEY")
from IPython.display import display, Code, Markdown
import matplotlib.pyplot as plt
import seaborn as sns
import time
import tiktoken

import numpy as np
import pandas as pd

import json
import io
import inspect
import requests
import re
import random
import string
import base64
import pymysql
import os.path
import matplotlib

from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaIoBaseUpload
import base64
import email
from email import policy
from email.parser import BytesParser
from email.mime.text import MIMEText
from openai.error import APIConnectionError

from bs4 import BeautifulSoup
import dateutil.parser as parser

import sys
from gptLearning import *
os.environ['SSL_VERSION'] = 'TLSv1_2'

import warnings
warnings.filterwarnings("ignore")

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from io import BytesIO
# 开启连接数据库模式
mategen_test = MateGen(api_key = os.getenv("OPENAI_API_KEY"),      # 设置api_key
                    model = "gpt-3.5-turbo-16k-0613",           # 设置模型
                    mysql_pw=os.getenv('MYSQL_PW'))             # 连接配置好的数据库，系统会自动开启MySQL外部函数
mategen_test.chat()
#InterProject类功能测试
# 本地存储测试
p1 = InterProject(project_name='测试项目', part_name='测试文档')
p1.folder_id
p1.update_doc_list()

# 表达式语句运行测试
code_str1 = '2 + 5'
python_inter(py_code = code_str1, g=globals())

# 赋值语句运行测试
code_str1 = 'a = 1'
python_inter(py_code = code_str1, g=globals())


# 数据字典文件
with open('telco_data_dictionary.md', 'r', encoding='utf-8') as f:
    data_dictionary = f.read()
# 基本问答效果测试
msg1 = ChatMessages(system_content_list=[data_dictionary], question="请帮我简单介绍下telco_db数据库中的这四张表")

# function call功能测试
msg2 = ChatMessages(system_content_list=[data_dictionary], question="请帮我查看user_demographics数据表中总共有多少条数据。")

msg3 = ChatMessages(system_content_list=[data_dictionary], question="请帮我查看user_demographics数据表中缺失值情况。")

# 开发者模式测试
msg4 = ChatMessages(system_content_list=[data_dictionary], question="请帮我查看user_demographics数据表中缺失值情况。")

msg5_response = get_gpt_response(model='gpt-4-0613', 
                                messages=msg5, 
                                available_functions=af,
                                is_developer_mode=False,
                                is_enhanced_mode=True)

#核心功能测试
msg = ChatMessages(system_content_list=[data_dictionary], question="请帮我查看user_demographics数据表中总共有多少条数据。")
msg_response = get_gpt_response(model='gpt-4-0613', 
                                messages=msg, 
                                available_functions=af)