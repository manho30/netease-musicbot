'''
@descrition: parse the object returned by searchMusic() into a number list 
@param: {object} musicInfo
@param: {int} start
@param: {int} end
@return: {string}
@return: {object}
'''


from sqlalchemy import null


def parseMusicList(musicInfo, start, end):
    # print the first element of the list
    txt = 'I found the following music for you:\n\n'
    txt += '✅ \n'
    
    button = []
    
    for i in range(start, end):
        
        # if i is equal to the index, then change the caractor to '└'
        if i == end - 1:
            txt += '└ *{}* *{}*\n'.format(i + 1, musicInfo['result']['songs'][i]['name'])
            txt += '     └ {}\n'.format(musicInfo['result']['songs'][i]['artists'][0]['name'])
            break
        
        txt += '├ *{}* *{}*\n'.format(i + 1, musicInfo['result']['songs'][i]['name'])
        txt += '│ └ {}\n'.format(musicInfo['result']['songs'][i]['artists'][0]['name'])
        
        button.append({
            'text': '{}'.format(i + 1),
            'callback_data': '{}'.format(musicInfo['result']['songs'][i]['id'])
        })
    print(txt)
    return txt, button


# for debug only!
if __name__ == '__main__':

    parseMusicList(
        {
            "result": {
                "songs": [
                    {
                        "id": 1867217766,
                        "name": "致你",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 131405806,
                            "name": "致你",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1628352000000,
                            "size": 2,
                            "copyrightId": 0,
                            "status": 0,
                            "picId": 109951166254691360,
                            "mark": 0
                        },
                        "duration": 271666,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [
                            "女声版"
                        ],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 0
                    },
                    {
                        "id": 1848190450,
                        "name": "银河与星斗",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 128013460,
                            "name": "银河与星斗",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1622304000000,
                            "size": 2,
                            "copyrightId": 7001,
                            "status": 0,
                            "picId": 109951166035185230,
                            "mark": 0
                        },
                        "duration": 194814,
                        "copyrightId": 7001,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 536879104
                    },
                    {
                        "id": 1939215517,
                        "name": "梁山伯与茱丽叶",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            {
                                "id": 30646978,
                                "name": "小包Zerinn",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 143632285,
                            "name": "梁山伯与茱丽叶",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1650211200000,
                            "size": 3,
                            "copyrightId": -1,
                            "status": 0,
                            "picId": 109951167308875650,
                            "mark": 0
                        },
                        "duration": 193461,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "transNames": [
                            "热恋版"
                        ],
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 536870912
                    },
                    {
                        "id": 1860614598,
                        "name": "如果呢（女声版）",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 130240689,
                            "name": "如果呢（女声版）",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1626105600000,
                            "size": 2,
                            "copyrightId": -1,
                            "status": 0,
                            "picId": 109951166171799950,
                            "mark": 0
                        },
                        "duration": 223550,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 536870912
                    },
                    {
                        "id": 1930790961,
                        "name": "麦浪",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 142272165,
                            "name": "麦浪",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1648051200000,
                            "size": 2,
                            "copyrightId": 7001,
                            "status": 0,
                            "picId": 109951167183782860,
                            "mark": 0
                        },
                        "duration": 185861,
                        "copyrightId": 7001,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 8192
                    },
                    {
                        "id": 1874972712,
                        "name": "苦茶 ",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            {
                                "id": 29235210,
                                "name": "Aioz",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 132690523,
                            "name": "苦茶",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1630598400000,
                            "size": 3,
                            "copyrightId": -1,
                            "status": 0,
                            "picId": 109951166350846820,
                            "mark": 0
                        },
                        "duration": 183867,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "transNames": [
                            "心动版"
                        ],
                        "mvid": 14492088,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 536879104
                    },
                    {
                        "id": 1889702364,
                        "name": "小雨天气",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            {
                                "id": 12084020,
                                "name": "嘿人李逵Noisemakers",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            {
                                "id": 12270985,
                                "name": "十七草",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 135228334,
                            "name": "小雨天气",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1635091200000,
                            "size": 2,
                            "copyrightId": 1419026,
                            "status": 0,
                            "picId": 109951166554719470,
                            "mark": 0
                        },
                        "duration": 159130,
                        "copyrightId": 1419026,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 536870912
                    },
                    {
                        "id": 1878315329,
                        "name": "就是爱你",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 133262146,
                            "name": "就是爱你",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1631635200000,
                            "size": 2,
                            "copyrightId": -1,
                            "status": 0,
                            "picId": 109951166396349180,
                            "mark": 0
                        },
                        "duration": 234155,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 536870912
                    },
                    {
                        "id": 1885427474,
                        "name": "都不懂",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 134515825,
                            "name": "都不懂",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1633968000000,
                            "size": 2,
                            "copyrightId": 7001,
                            "status": 0,
                            "picId": 109951166503956880,
                            "mark": 0
                        },
                        "duration": 152851,
                        "copyrightId": 7001,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 8192
                    },
                    {
                        "id": 1846094285,
                        "name": "我不要一直想你",
                        "artists": [
                            {
                                "id": 31051426,
                                "name": "杨胖雨",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 127632736,
                            "name": "我不要一直想你",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1621440000000,
                            "size": 3,
                            "copyrightId": -1,
                            "status": 0,
                            "picId": 109951165990481120,
                            "mark": 0
                        },
                        "duration": 186666,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 536870912
                    },
                    {
                        "id": 1863090822,
                        "name": "夏天的夏",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            {
                                "id": 34357551,
                                "name": "吴炳文Cookie",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 130722615,
                            "name": "夏天的夏",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1627228800000,
                            "size": 2,
                            "copyrightId": 1416649,
                            "status": 0,
                            "picId": 109951166201019280,
                            "mark": 0
                        },
                        "duration": 172681,
                        "copyrightId": 1416649,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 0
                    },
                    {
                        "id": 1885179171,
                        "name": "清醒",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 134460208,
                            "name": "清醒",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1633708800000,
                            "size": 2,
                            "copyrightId": 2708435,
                            "status": 1,
                            "picId": 109951166501835940,
                            "mark": 0
                        },
                        "duration": 239062,
                        "copyrightId": 2708435,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 262144
                    },
                    {
                        "id": 1941664399,
                        "name": "为什么不说话",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            {
                                "id": 37616858,
                                "name": "Bell玲惠",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 144014158,
                            "name": "为什么不说话",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1651161600000,
                            "size": 2,
                            "copyrightId": -1,
                            "status": 0,
                            "picId": 109951167342805550,
                            "mark": 0
                        },
                        "duration": 191598,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 536870912
                    },
                    {
                        "id": 1906045793,
                        "name": "漫天星光（纯音乐版）",
                        "artists": [
                            {
                                "id": 12157336,
                                "name": "CMJ",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 137926724,
                            "name": "漫天星光（网易云音乐2021年度听歌报告主题曲）",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1640534400000,
                            "size": 3,
                            "copyrightId": -1,
                            "status": 0,
                            "picId": 109951166789488660,
                            "mark": 0
                        },
                        "duration": 128160,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 537001984
                    },
                    {
                        "id": 1896469403,
                        "name": "月亮爱过日落",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 136377422,
                            "name": "月亮爱过日落",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1637683200000,
                            "size": 2,
                            "copyrightId": -1,
                            "status": 0,
                            "picId": 109951166639252700,
                            "mark": 0
                        },
                        "duration": 157568,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 0
                    },
                    {
                        "id": 1898189387,
                        "name": "病因",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 136638073,
                            "name": "病因",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1638201600000,
                            "size": 2,
                            "copyrightId": -1,
                            "status": 0,
                            "picId": 109951166671616020,
                            "mark": 0
                        },
                        "duration": 232500,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 536870912
                    },
                    {
                        "id": 1828747550,
                        "name": "没有意外（翻自 蔡徐坤）",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 124292004,
                            "name": "没有意外",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1615751799763,
                            "size": 1,
                            "copyrightId": 0,
                            "status": 0,
                            "picId": 109951165805519630,
                            "mark": 0
                        },
                        "duration": 28943,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 0,
                        "rUrl": null,
                        "mark": 128
                    },
                    {
                        "id": 1470130616,
                        "name": "想念拟人化",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 93720349,
                            "name": "想念拟人化",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1597130186707,
                            "size": 1,
                            "copyrightId": 0,
                            "status": 0,
                            "picId": 109951165224719580,
                            "mark": 0
                        },
                        "duration": 260202,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 0,
                        "rUrl": null,
                        "mark": 128
                    },
                    {
                        "id": 1844562141,
                        "name": "小宇",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 125556373,
                            "name": "抖音翻唱",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1617455972590,
                            "size": 14,
                            "copyrightId": 0,
                            "status": 0,
                            "picId": 109951166160332910,
                            "mark": 0
                        },
                        "duration": 30267,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 0,
                        "rUrl": null,
                        "mark": 128
                    },
                    {
                        "id": 1886384894,
                        "name": "苦茶（DJ版）",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            {
                                "id": 29235210,
                                "name": "Aioz",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 132690523,
                            "name": "苦茶",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1630598400000,
                            "size": 3,
                            "copyrightId": -1,
                            "status": 0,
                            "picId": 109951166350846820,
                            "mark": 0
                        },
                        "duration": 218222,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 0
                    },
                    {
                        "id": 1868872629,
                        "name": "银河与星斗（伴奏）",
                        "artists": [
                            {
                                "id": 49281759,
                                "name": "Yihuik",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 131678146,
                            "name": "银河与星斗",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1622304000000,
                            "size": 2,
                            "copyrightId": 7001,
                            "status": 1,
                            "picId": 109951166275223540,
                            "mark": 0
                        },
                        "duration": 194873,
                        "copyrightId": 7001,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 139264
                    },
                    {
                        "id": 1881719700,
                        "name": "遗失的解药",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 133836448,
                            "name": "遗失的解药",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1632717304441,
                            "size": 2,
                            "copyrightId": 0,
                            "status": 0,
                            "picId": 109951166459784020,
                            "mark": 0
                        },
                        "duration": 251072,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 0
                    },
                    {
                        "id": 1832643077,
                        "name": "就让我在你身边",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 125197307,
                            "name": "就让我在你身边",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1617292800000,
                            "size": 2,
                            "copyrightId": 1416618,
                            "status": 0,
                            "picId": 109951166214779630,
                            "mark": 0
                        },
                        "duration": 259090,
                        "copyrightId": 1416618,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 8192
                    },
                    {
                        "id": 1906045789,
                        "name": "漫天星光（演唱版）",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 137926724,
                            "name": "漫天星光（网易云音乐2021年度听歌报告主题曲）",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1640534400000,
                            "size": 3,
                            "copyrightId": -1,
                            "status": 0,
                            "picId": 109951166789488660,
                            "mark": 0
                        },
                        "duration": 232775,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 0
                    },
                    {
                        "id": 1844566133,
                        "name": "输入法打可爱按第五",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 125556373,
                            "name": "抖音翻唱",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1617455972590,
                            "size": 14,
                            "copyrightId": 0,
                            "status": 0,
                            "picId": 109951166160332910,
                            "mark": 0
                        },
                        "duration": 27376,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 0,
                        "rUrl": null,
                        "mark": 128
                    },
                    {
                        "id": 1834675802,
                        "name": "晚风",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 125556373,
                            "name": "抖音翻唱",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1617455972590,
                            "size": 14,
                            "copyrightId": 0,
                            "status": 0,
                            "picId": 109951166160332910,
                            "mark": 0
                        },
                        "duration": 25368,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 0,
                        "rUrl": null,
                        "mark": 128
                    },
                    {
                        "id": 1945241420,
                        "name": "专属天使（Cover yihuik苡慧）",
                        "artists": [
                            {
                                "id": 34178727,
                                "name": "池海秀bb",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 144483126,
                            "name": "藏不住的喜欢",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1651716182453,
                            "size": 4,
                            "copyrightId": 0,
                            "status": 0,
                            "picId": 109951167378723820,
                            "mark": 0
                        },
                        "duration": 251000,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 0,
                        "rUrl": null,
                        "mark": 128
                    },
                    {
                        "id": 1844584034,
                        "name": "老男孩",
                        "artists": [
                            {
                                "id": 36032190,
                                "name": "yihuik苡慧",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 125556373,
                            "name": "抖音翻唱",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1617455972590,
                            "size": 14,
                            "copyrightId": 0,
                            "status": 0,
                            "picId": 109951166160332910,
                            "mark": 0
                        },
                        "duration": 28107,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 0,
                        "rUrl": null,
                        "mark": 128
                    },
                    {
                        "id": 1934914514,
                        "name": "岁月神偷",
                        "artists": [
                            {
                                "id": 50381300,
                                "name": "星庆",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            {
                                "id": 0,
                                "name": "yihuik",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 135735308,
                            "name": "覆水难收",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1636106444032,
                            "size": 3,
                            "copyrightId": 0,
                            "status": 0,
                            "picId": 109951166878838820,
                            "mark": 0
                        },
                        "duration": 162800,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 0,
                        "rUrl": null,
                        "mark": 128
                    },
                    {
                        "id": 1854473737,
                        "name": "银河与星斗（温柔女生版）（翻自 yihuik苡慧 ）",
                        "artists": [
                            {
                                "id": 35293841,
                                "name": "予笙",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            }
                        ],
                        "album": {
                            "id": 129242797,
                            "name": "晚风依旧很温柔",
                            "artist": {
                                "id": 0,
                                "name": "",
                                "picUrl": null,
                                "alias": [],
                                "albumSize": 0,
                                "picId": 0,
                                "img1v1Url": "https://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
                                "img1v1": 0,
                                "trans": null
                            },
                            "publishTime": 1624009953455,
                            "size": 1,
                            "copyrightId": 0,
                            "status": 0,
                            "picId": 109951166099748620,
                            "mark": 0
                        },
                        "duration": 194954,
                        "copyrightId": 0,
                        "status": 0,
                        "alias": [],
                        "rtype": 0,
                        "ftype": 0,
                        "mvid": 0,
                        "fee": 8,
                        "rUrl": null,
                        "mark": 64
                    }
                ],
                "hasMore": True,
                "songCount": 173
            },
            "code": 200
        }, 20, 30
    )
