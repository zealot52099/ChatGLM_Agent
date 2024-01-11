class InterProject():
    """
    项目类：项目是每个分析任务的基础对象，换而言之，每个分析任务应该都是“挂靠”在某个项目中。\
    每个代码解释器必须说明所属项目，若无所属项目，则在代码解释器运行时会自动创建一个项目。\
    需要注意的是，项目不仅起到了说明和标注当前分析任务的作用，更关键的是，项目提供了每个分析任务的“长期记忆”，\
    即每个项目都有对应的谷歌云盘和谷歌云文档，用于保存在分析和建模工作过程中多轮对话内容，\
    此外，也可以选择借助本地文档进行存储。
    """

    def __init__(self, 
                 project_name, 
                 part_name, 
                 folder_id = None, 
                 doc_id = None, 
                 doc_content = None, 
                 upload_to_google_drive = False):
        
        # 项目名称，即项目文件夹名称
        self.project_name = project_name
        # 项目某部分名称，即项目文件名称
        self.part_name = part_name
        # 是否进行谷歌云文档存储
        self.upload_to_google_drive = upload_to_google_drive
        
        # 项目文件夹ID
        # 若项目文件夹ID为空，则获取项目文件夹ID
        if folder_id == None:
            folder_id = create_or_get_folder(folder_name=project_name,
                                             upload_to_google_drive = upload_to_google_drive)
        self.folder_id = folder_id
        
        # 创建时获取当前项目中其他文件名称列表
        self.doc_list = list_files_in_folder(folder_id, 
                                             upload_to_google_drive = upload_to_google_drive)
        
        # 项目文件ID
        # 若项目文件ID为空，则获取项目文件ID
        if doc_id == None:
            doc_id = create_or_get_doc(folder_id=folder_id, 
                                       doc_name=part_name, 
                                       upload_to_google_drive = upload_to_google_drive)
        self.doc_id = doc_id
        
        # 项目文件具体内容，相当于多轮对话内容
        self.doc_content = doc_content
        # 若初始content不为空，则将其追加入文档内
        if doc_content != None:
            append_content_in_doc(folder_id=folder_id, 
                                  doc_id=doc_id, 
                                  qa_string=doc_content, 
                                  upload_to_google_drive = upload_to_google_drive)
            

    def get_doc_content(self):
        """
        根据项目某文件的文件ID，获取对应的文件内容
        """     
        self.doc_content = get_file_content(file_id=self.doc_id, 
                                            upload_to_google_drive = self.upload_to_google_drive)

        return self.doc_content
    
    def append_doc_content(self, content):
        """
        根据项目某文件的文件ID，追加文件内容
        """  
        append_content_in_doc(folder_id=self.folder_id, 
                              doc_id=self.doc_id, 
                              dict_list=content, 
                              upload_to_google_drive = self.upload_to_google_drive)
    
    def clear_content(self):
        """
        清空某文件内的全部内容
        """  
        clear_content_in_doc(doc_id=self.doc_id, 
                             upload_to_google_drive = self.upload_to_google_drive)
        
    def delete_all_files(self):
        """
        删除当前项目文件夹内的全部文件
        """  
        delete_all_files_in_folder(folder_id=self.folder_id, 
                                   upload_to_google_drive = self.upload_to_google_drive)
        
    def update_doc_list(self):
        """
        更新当前项目文件夹内的全部文件名称
        """
        self.doc_list = list_files_in_folder(self.folder_id, 
                                             upload_to_google_drive = self.upload_to_google_drive)
    
    def rename_doc(self, new_name):
        """
        修改当前文件名称
        """
        self.part_name = rename_doc_in_drive(folder_id=self.folder_id, 
                                             doc_id=self.doc_id, 
                                             new_name=new_name, 
                                             upload_to_google_drive = self.upload_to_google_drive)