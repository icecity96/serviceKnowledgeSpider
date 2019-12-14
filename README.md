# ServiceKnowledgeSpider

## Introduction
This project is used to collect service-related entities information to build a service domain knowledge graph.

## Contribute
You are welcome to send a pull request or open an issue.

There are some problems need to be solved manually (maybe you can find an algorithm):

[-] In 100ec_enterprise, entities should be classified into Organization and channel. 

## Resources List
* **pedaily_enterprise**: https://zdb.pedaily.cn/enterprise
    
    | column | explanation |
    | ----| -------------------------------- |
    | fn | enterprise full name (e.g., 阿里巴巴集团控股有限公司) |
    | sn | enterprise short name (e.g., 阿里巴巴) |
    | loc | enterprise location (e.g., 余杭区) |
    | reg | enterprise registration location (e.g., 余杭区) |
    | cre | enterprise creation date (e.g., 1999年) |
    | dom | enterprise domain (e.g., B2B) |
    | web | enterprise web site (e.g., www.alibabagroup.com) |
    | intro| enterprise brief introduction (e.g.,阿里巴巴集团控股有限公司是一家电子商务企业，旗下拥有... )|
    
* **mi_appstore**: http://app.mi.com/

    | column | explanation | example |
    | --- | -------------- | ------- |
    | fn | app full name | 中国移动 |
    | dev | developer | 中国移动通信有限公司 |
    | url | url | http://app.mi.com/details?id=com.greenpoint.android.mc10086.activity |
    | ca | app category | 实用工具 |
    | sp | support platform | 手机 |
    | avs | app average score | 3 |
    | cn | comment number | 7519 |
    | size | app size | 34.32 M |
    | v | app version | 5.8.2 |
    | ut | update time | 2019-11-30|
    | pn | package name | com.greenpoint.android.mc10086.activity |
    | id | app ID | 51733 |
    | pm | app permissions | 蓝牙管理-录音-...|
    | intro | app introduction | .... |
    | new | what's new | ... |
    
* **100ec_enterprise**: http://www.100ec.cn/zt/qyk/

    | column | explanation | example |
    | ------ | ----------- | ------- |
    | Name | organization/channel name | 51信用卡管家 |
    | Category | domain name | 互联网金融 |
    | Subcategory | sub-domain name | 消费信贷 |
    | URL | Link to related news | ... |
    
* **itjuzi_deathcompany**: https://www.itjuzi.com/deathCompany
    
```json
{
  "com_id": 33468277, 
  "com_logo_archive": "44a2660ae9b2bb643b54b03a707f103f.png", 
  "com_name": "淘集集", 
  "com_change_close_date": "2019-12-09", 
  "com_born_year": 2017, 
  "com_born_month": 5, 
  "total_money": 27300, 
  "com_des": "淘集集是一个拼团社交电商平台，涵盖服饰鞋配、母婴、家纺、数码、食品等生活用品，用户邀请亲友参与拼团，满足人数要求后可享受低价购买的权利，同时可参加VIP会员，无需拼团即可享受低价。是一款基于补充线下零售门店销售场景的购物类APP，可以让会员不在门店的时候可以在线进行商品的购买，指引会员到店进行商品的体验，于2018年8月上线。", 
  "cat_name": "电子商务", 
  "se_cat_name": "生鲜食品", 
  "com_prov": "上海", 
  "com_fund_status_name": "A轮",
  "live_time": 952, 
  "born": "2017-05-01",
  "logo": "https://cdn.itjuzi.com/images/44a2660ae9b2bb643b54b03a707f103f.png?imageView2/0/q/100", 
  "live_date": [2, 7, 8], 
  "com_team": [
      {
        "id": 31580, 
        "name": "张正平", 
        "per_des": "张正平，淘集集CEO。连续创业者，曾在宝尊电商任职，任旗下品牌尾货特卖平台“卖客疯”CEO，闪电降价的前身，是宝尊电商旗下的电商平台“卖客疯”。", 
        "logo": "https://cdn.itjuzi.com/assets/front/images/img/icon-person.png", 
        "des": "CEO", 
        "per_state": 0}, 
      {
        "id": 114787, 
        "name": "苟晓辰", 
        "per_des": "苟晓辰，淘集集CTO。", 
        "logo": "https://cdn.itjuzi.com/assets/front/images/img/icon-person.png", 
        "des": "CTO", 
        "per_state": 0}], 
  "com_tag": [
      {
        "tag_id": 337, 
        "tag_name": "社交电商"}, 
      {
        "tag_id": 402,
        "tag_name": "B2B"}, 
      {
        "tag_id": 756, 
        "tag_name": "电子商务"}, 
      {
        "tag_id": 758, 
        "tag_name": "生鲜食品"}, 
      {
        "tag_id": 9083, 
        "tag_name": "拼团 "}], 
  "com_invst": [
      {
        "invst_id": 160, 
        "invst_name": "DST"}, 
      {
        "invst_id": 198, 
        "invst_name": "Tiger老虎基金(中国)"}, 
      {
        "invst_id": 6788, 
        "invst_name": "险峰旗云"}], 
  "closure_type": [
      {
        "id": 7, 
        "name": "团队能力不足", 
        "p_id": 22}, 
      {
        "id": 11, 
        "name": "烧钱", 
        "p_id": 24}, 
      {
        "id": 12, 
        "name": "现金流断裂", 
        "p_id": 24}]
}
```