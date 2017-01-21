# -*-coding:utf-8 -*-
import unittest

from ddt import ddt, data, unpack
from papi.httprequest import SendHttpRequest

from apiFrame.papi.dataprase import jsonprase, xmlprase


@ddt
class TestSingleRequest(unittest.TestCase):
    #定义数据信息
    def setUp(self):
        self.url = "http://xxxxxxxxxxxxxxxxxxx/api/xxxxxx"
    @data(
        (32351, 6),
        (9555, 4)
    )
    @unpack
    def test_Single_right(self, sid, count):
        value = {"sid": sid, "count": count}
        data = SendHttpRequest(self.url).get(value)
        json_data = jsonprase(data)
        point_lat = json_data.find_json_node_by_xpath("/Point/Lat")#通过json_data包查找节点
        point_lng = json_data.find_json_node_by_xpath("/Point/Lng")
        is_exists_map = json_data.find_json_node_by_xpath("/Ptd/AmapGuideMap155/IsExistsMap")#导入正确的数据，从数据库中导入
        size = json_data.find_json_node_by_xpath("/Ptd/AmapGuideMap155/Size")
        # 断言
        assert float(point_lat) != 0 and float(point_lng) != 0
        # 断言
        assert json_data.find_json_node_by_xpath("/Ptd/AmapGuideMap155/DownUrl") is not None
        if is_exists_map == True:
            assert size != ""

    # 导常请求SingleRequest接口
    @data(
        ("abceeffffg", 6),
        (9555, "")
    )
    @unpack
    def test_Single_error(self, sid, count):
        value = {"sid": sid, "count": count}
        data = SendHttpRequest(self.url).get(value)
        self.assertEqual(data, u'{"Message":"请求无效。"}')

#另外一个测试用例方法
@ddt
class TourMaps(unittest.TestCase):
    def setUp(self):
        self.url = "http://xxxxxx/api/TourMap"

    @data(32351, 9555)
    def test_requests_online_xml(self, tourId):
        xml_url = self.url + "/%s" % tourId
        data = SendHttpRequest(xml_url).get()
        json_st = xmlprase(data).xml_to_json
        json_data = jsonprase(json_st)
        lng = json_data.find_json_node_by_xpath("/root/data/@lng")
        lat = json_data.find_json_node_by_xpath("/root/data/@lat")
        assert lng != "" and lat != ""
        son_tour = json_data.find_json_node_by_xpath("/root/data/data")
        assert len(son_tour) > 0

class TourData(unittest.TestCase):
    def setUp(self):
        self.url = "http://xxxxxx/api/xxx"

    @data(
        (),
        (),
        (),
    )
    @unpack
    def test_tourList_Location_in_open(self):
        pass

    def test_tourList_Location_not_open(self):
        pass

    def test_tour_open_city(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TourMaps, TestSingleRequest)
    unittest.TextTestRunner(verbosity=2).run(suite)