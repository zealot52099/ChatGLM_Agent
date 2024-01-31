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
def python_inter(py_code, g='globals()'):
    """
    专门用于执行非绘图类python代码，并获取最终查询或处理结果。若是设计绘图操作的Python代码，则需要调用fig_inter函数来执行。
    :param py_code: 字符串形式的Python代码，用于执行对telco_db数据库中各张数据表进行操作
    :param g: g，字符串形式变量，表示环境变量，无需设置，保持默认参数即可
    :return：代码运行的最终结果
    """    
    
    global_vars_before = set(g.keys())
    try:
        exec(py_code, g)            
    except Exception as e:
        return f"代码执行时报错{e}"
    global_vars_after = set(g.keys())
    new_vars = global_vars_after - global_vars_before
    # 若存在新变量
    if new_vars:
        result = {var: g[var] for var in new_vars}
        return str(result)
    # 若不存在新变量，即有可能是代码是表达式，也有可能代码对相同变量重复赋值
    else:
        try:
            # 尝试如果是表达式，则返回表达式运行结果
            return str(eval(py_code, g))
        # 若报错，则先测试是否是对相同变量重复赋值
        except Exception as e:
            try:
                exec(py_code, g)
                return "已经顺利执行代码"
            except Exception as e:
                pass
            # 若不是重复赋值，则报错
            return f"代码执行时报错{e}"