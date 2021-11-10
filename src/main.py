import pydicom
import os

'''
改程序用来读取医学领域的dicom类型的数据，并将敏感信息进脱敏。

原始数据在data文件目录中，新生成的脱敏数据在data_desensize文件目录中
'''
def desensitization(prt, dcm_file_name, p3_path):
    '''
    对每输入的路径文件进行脱敏
    :param dcm_file_name:
    :return: 将文件信息进行脱敏，并进行保存
    '''

    ds = pydicom.dcmread(dcm_file_name)
    ds.InstitutionName = 'XXXXX'
    ds.InstitutionAddress = 'XXXXX'
    ds.InstitutionalDepartmentName = 'XXXXX'
    ds.PerformingPhysicianName = 'XXXXX'    #list
    ds.PatientName = 'XXXXX' #list
    ds.PatientID = 'XXXXX'
    ds.IssuerOfPatientID = 'XXXXX'
    ds.PatientBirthDate = 'XXXXX'
    ds.PatientSex = 'XXXXX'
    ds.PatientAge = 'XXXXX'
    ds.PatientSize = -1
    ds.PatientWeight = -1
    ds.PatientAddress = 'XXXXX'
    ds.PregnancyStatus = 0
    ds.PerformedProcedureStepStartDate = 'XXXXX'
    ds.PerformedProcedureStepStartTime = 'XXXXX'
    ds.PerformedProcedureStepID = 'XXXXX'
    name = dcm_file_name.split('\\')[-1]
    save_path = '../data_desensize' + p3_path[7:]
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    if prt:
        print(ds)
    ds.save_as(os.path.join(save_path, name))
    print(dcm_file_name + "     脱敏完成------")


def read_files(prt, root_path='../data/'):
    '''
    根据目录结构获取文件名称路径
    :param prt: 是否打印树脱敏后的数据
    :param root_path:
    :return: 文件名称路径
    '''
    name_list = os.listdir(root_path)  # 获取患者姓名
    for name in name_list:
        cate_path = os.path.join(root_path, name)
        cate_list = os.listdir(cate_path)  # 获取患者里面的第一次目录，["TIWI", "增强", "脂肪抑制"]
        for p1 in cate_list:
            p1_path = os.path.join(cate_path, p1)
            p1_list = os.listdir(p1_path) # 获取 ["T1-2323387"]
            for p2 in p1_list:
                p2_path = os.path.join(p1_path, p2)
                p2_list = os.listdir(p2_path) # 获取["dcm"] or ["dicom"]
                for p3 in p2_list:
                    p3_path = os.path.join(p2_path, p3)
                    p3_list = os.listdir(p3_path)
                for dcm_name in p3_list:
                    dcm_file_path = os.path.join(p3_path, dcm_name)
                    if os.path.splitext(dcm_file_path)[1] == '.dcm':
                        desensitization(prt, dcm_file_path, p3_path)

if __name__ == '__main__':
    read_files(prt=False)
# ds = pydicom.dcmread('../data/01张三/TIWI/T1-2323387/dcm/ser003img00001.dcm')
# dcm_file_name = r'../data/01张三/脂肪抑制/T2-2323387/dcm/ser007img00004.dcm'
# dcm_file_name ='../data/01张三/TIWI/T1-2323387/dcm/ser003img00001.dcm'
# desensitization(dcm_file_name)
