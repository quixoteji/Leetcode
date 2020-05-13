from pathlib import Path
from os import getcwd
import pandas as pd

currentPath = getcwd() + '/test/'
# currentPath = '/content/test/'
pathlist = Path(currentPath).glob('**/*.lrmx')

df = pd.DataFrame([['', '', '', '', '', '', '', '', '', '', '', '', '']], columns = ['姓名', '性别', '出生年月', '党派', '籍贯', '全日制学历', '全日制学校', '在职学历', '在职学校', '专业技术职务', '参加工作时间', '任现职级时间', '工作单位及职务'])

def extract(s) :
    ans = ''
    for ch in s :
        if u'\u4e00' <= ch <= u'\u9fff' or ch.isdigit():
            ans += ch
    return ans

for path in pathlist:
    f = open(path)
    lines = f.readlines()
    data = pd.DataFrame([['', '', '', '', '', '', '', '', '', '', '', '', '']], columns = ['姓名', '性别', '出生年月', '党派', '籍贯', '全日制学历', '全日制学校', '在职学历', '在职学校', '专业技术职务', '参加工作时间', '任现职级时间', '工作单位及职务'])
    # data = dict()
    for line in lines :
        if line.startswith('  <XingMing>') :
            XingMing = extract(line)    
            data['姓名'] = XingMing
        if line.startswith('  <XingBie>') :
            XingBie = extract(line)
            data['性别'] = XingBie
        if line.startswith('  <ChuShengNianYue>') :
            ChuShengNianYue = extract(line)
            data['出生年月'] = ChuShengNianYue
        if line.startswith('  <MinZu>') :
            MinZu = extract(line)

        if line.startswith('  <JiGuan>') :
            JiGuan = extract(line)
            data['籍贯'] = JiGuan
        if line.startswith('  <ChuShengDi>') :
            ChuShengDi = extract(line)
            
        if line.startswith('  <RuDangShiJian>') :
            RuDangShiJian = extract(line)
            data['党派'] = RuDangShiJian
        if line.startswith('  <CanJiaGongZuoShiJian>') :
            CanJiaGongZuoShiJian = extract(line)

        if line.startswith('  <JianKangZhuangKuang>') :
            JianKangZhuangKuang = extract(line)

        if line.startswith('  <ZhuanYeJiShuZhiWu>') :
            ZhuanYeJiShuZhiWu = extract(line)
            data['专业技术职务'] = ZhuanYeJiShuZhiWu
        if line.startswith('  <ShuXiZhuanYeYouHeZhuanChang>') :
            ShuXiZhuanYeYouHeZhuanChang = extract(line)

        if line.startswith('  <QuanRiZhiJiaoYu_XueLi>') :
            QuanRiZhiJiaoYu_XueLi = extract(line)
            data['全日制学历'] = QuanRiZhiJiaoYu_XueLi
        if line.startswith('  <QuanRiZhiJiaoYu_XueWei>') :
            QuanRiZhiJiaoYu_XueWei = extract(line)

        if line.startswith('  <QuanRiZhiJiaoYu_XueLi_BiYeYuanXiaoXi>') :
            QuanRiZhiJiaoYu_XueLi_BiYeYuanXiaoXi = extract(line)

        if line.startswith('  <QuanRiZhiJiaoYu_XueWei_BiYeYuanXiaoXi>') :
            QuanRiZhiJiaoYu_XueWei_BiYeYuanXiaoXi = extract(line)
            data['全日制学校'] = QuanRiZhiJiaoYu_XueLi_BiYeYuanXiaoXi + QuanRiZhiJiaoYu_XueWei_BiYeYuanXiaoXi
        if line.startswith('  <ZaiZhiJiaoYu_XueLi>') :
            ZaiZhiJiaoYu_XueLi = extract(line)
            
            data['在职学历'] = ZaiZhiJiaoYu_XueLi
        if line.startswith('  <ZaiZhiJiaoYu_XueWei>') :
            ZaiZhiJiaoYu_XueWei = extract(line)
        
        if line.startswith('  <ZaiZhiJiaoYu_XueLi_BiYeYuanXiaoXi>') :
            ZaiZhiJiaoYu_XueLi_BiYeYuanXiaoXi = extract(line)
            data['在职学校'] = ZaiZhiJiaoYu_XueLi_BiYeYuanXiaoXi + ZaiZhiJiaoYu_XueWei
        if line.startswith('  <ZaiZhiJiaoYu_XueWei_BiYeYuanXiaoXi>') :
            ZaiZhiJiaoYu_XueWei_BiYeYuanXiaoXi = extract(line)
        
        if line.startswith('  <XianRenZhiWu>') :
            XianRenZhiWu = extract(line)
            data['工作单位及职务'] = XianRenZhiWu
        if line.startswith('  <NiRenZhiWu>') :
            NiRenZhiWu = extract(line)
        
        if line.startswith('  <NiMianZhiWu>') :
            NiMianZhiWu = extract(line)

        if line.startswith('  <JianLi>') :
            data['参加工作时间'] = line[10:17]

        if '</JianLi>' in line:
            data['任现职级时间'] = line[:7]
    # print(data)
    # print(type(data))
    df = df.append([data], ignore_index=True)
    # print(data)
# print(df)
df.to_excel('test.xlsx')