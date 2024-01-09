def upload_image_to_drive(figure, folder_id = '1YstWRU-78JwTEQQA3vJokK3OF_F0djRH'):
    """
    将指定的fig对象上传至谷歌云盘
    """
    folder_id = folder_id        # 此处需要改为自己的谷歌云盘文件夹ID
    creds = Credentials.from_authorized_user_file('token.json')
    drive_service = build('drive', 'v3', credentials=creds)
    
    # 1. Save image to Google Drive
    buf = BytesIO()
    figure.savefig(buf, format='png')
    buf.seek(0)
    media = MediaIoBaseUpload(buf, mimetype='image/png', resumable=True)
    file_metadata = {
        'name': 'YourImageName.png',
        'parents': [folder_id],
        'mimeType': 'image/png'
    }
    image_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id,webContentLink'  # Specify the fields to be returned
    ).execute()
    
    return image_file["webContentLink"]

def fig_inter(py_code, fname, g='globals()'):
    """
    用于执行一段包含可视化绘图的Python代码，并最终获取一个图片类型对象
    :param py_code: 字符串形式的Python代码，用于根据需求进行绘图，代码中必须包含Figure对象创建过程
    :param fname: py_code代码中创建的Figure变量名，以字符串形式表示。
    :param g: g，字符串形式变量，表示环境变量，无需设置，保持默认参数即可
    :return：代码运行的最终结果
    """    
    # 保存当前的后端
    current_backend = matplotlib.get_backend()
    
    # 设置为Agg后端
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    # 创建一个字典，用于存储本地变量
    local_vars = {"plt": plt, "pd": pd, "sns": sns}
    
    try:
        exec(py_code, g, local_vars)       
    except Exception as e:
        return f"代码执行时报错{e}"
    
    # 回复默认后端
    matplotlib.use(current_backend)
    
    # 根据图片名称，获取图片对象
    fig = local_vars[fname]
    
    # 上传图片
    try:
        fig_url = upload_image_to_drive(fig)
        res = f"已经成功运行代码，并已将代码创建的图片存储至：{fig_url}"
        
    except Exception as e:
        res = "无法上传图片至谷歌云盘，请检查谷歌云盘文件夹ID，并检查当前网络情况"
        
    print(res)
    return res