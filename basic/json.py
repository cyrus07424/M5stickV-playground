#
# JSON.
#

##################################################
# import
##################################################
import ujson

##################################################
# initialize
##################################################
json_str = '''{
    "name": "sipeed",
    "babies": [
        {
            "name": "maixpy",
            "birthday": 2.9102,
            "sex": "unstable"
        }
    ]
}'''

##################################################
# main
##################################################
# JSON文字列を読み込み
obj = ujson.loads(json_str)

# 属性をコンソールに表示
print(obj["name"])
print(obj["babies"])
