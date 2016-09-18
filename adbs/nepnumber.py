# -*- coding: utf-8 -*-

nums = {
  '0': '०',
  '1': '१',
  '2': '२',
  '3': '३',
  '4': '४',
  '5': '५',
  '6': '६',
  '7': '७',
  '8': '८',
  '9': '९'
}


def get_nepali_num(strNum):
    num_list = list(str(strNum))
    return ''.join(nums[x] if x in list(nums.keys()) else x for x in num_list)
