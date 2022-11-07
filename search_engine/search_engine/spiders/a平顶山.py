from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A平顶山Spider(ZhengFuBaseSpider):
    # 页面数解析还有点问题
    name: str = '平顶山'
    api: str = 'http://www.pds.gov.cn/sitefiles/Api/search.aspx'
    method: str = 'POST'
    data: dict[str, Any] = {
        'ajaxdivid': "ajaxElement_1_1",
        'channelid': "",
        'channelids': "",
        'channelindex': "",
        'channelname': "",
        'dateattribute': "AddDate",
        'datefrom': "",
        'dateto': "",
        'fulltext': 'true',
        'isallsites': "false",
        'isdefaultdisplay': 'false',
        'ishighlight': 'true',
        'nosplit': "True",
        'page': "{page}",
        'pagenum': '10',
        'publishmentsystemid': "1",
        'since': "",
        'sitedir': "",
        'siteids': "",
        'sitename': "",
        'template': "qYw4qI0add0aqmJfg4FO218o3Tc1tZ3Nf4V0s9WbYo8Uk13zbEXVjQ0sd0I1dbrjsYqxSOqKSkTz2qfdAX4HVlYGK0N4ohLtnaucAx4l9tus5h39irtUFpygDQ70slash0cgVSC2xwYB6KLcQjw6kukUcS4G30slash0omnaT4yjZqKBxz0xpqt960add0b50iSkXhiFYs5k5mrnNPMIiTwq0add0X5OFNXaS9hM0add0ZxuCl6qg2u3ft2n98wUX0add0yphMJLlOP7fZmOTsHTtud20X7U470OvbSqJiqEbxsXLzZhOMYa9y030add0Dl5ONUFSbxW1AidCO0add0JZW1QyBmuxhyJqWKayl3lZ6ijNqICixB3HtXXXp4fAUf20CNNzwduncqgEU2h0Dt4f4DX0eaHbQa3GmTnoJ0add0j5Pi0MkQ0add0rEOjSrpJLdVk5ECzl0slash0PFJnjTHFfGfWu97GZE5raZuOvifINsEoooPD39JLv1SlR4S2WVPk00DWHIIQU7f2G0slash0pLhkfTVsHK6kDKA3q8ZneOBFRnoHlwoV6OIs08wiGtSjBt0slash0YNk5s9TFeLICECX6zhOvu83gvtPRgr9nWEwVhwgSrQtYQuRHokp4mMJjfcl0slash0Gpt2GgPZKndDVLMsYVHhPjm8XY5XwA0iQQtCOGoXaMtVFHeHIZHMtZDRswijsRQFVL1AW0add08ngtUuYZLuADU4YZDf0add07W0slash0nP03g0add0oOBafffqkVoFW5lVob84Bs9ph4LZell5IAsX5XXpBFknnIWMUX3qVxX1KGem3bJpQCUkLcX3Wz3gBPRXV3kG5YciED7o4fx7BK9JUImSvbqcEOQgoAmLmiEMN3JqDxiZMw8fECvOZVqI0slash0oXidAFyL4VsKoFYkV8v0add0MSgvLLrN5obyD3D1goTwhw0rthGP0slash0y3ZbguOh0ccneaSo0J8uts60add06s9rxCgeW05MakUx2qQV2ppEIMUUMHjfIJYU0slash0mqQjoVGX2K0DM5GqEiIzpQY0WSMznZDqf1Pnmw1SwzS30add0BQdnJKfvoJlumGYJbS2PyJnhVk1jqzl72I0slash05mKCUGGMj0add0pkzdUOPD22l6f8TRnsJrspps0slash0UViFH6A8uTa60add0niHL9Ys0xSpkLOFxyuzorAewqbNPrORSMb5zaN6oDMvRyizMfRn6hrHYbwkTn0slash0pmesuSHH7gpTzCrYqo30add0wd0slash0cTCc0h5GjMcM7aIkc4ApaAMMVdpDSYBFUHtI1HNIVUtJ7xRpHkYyYom5NzPM9vwowvg5e8cDKLBax24kG4DkgBsvn1fNmu7iBdi7wv280add0uOS5nk0add0FodOiW8FRTzWTdtfaHh6frc3TxZ6oCUytINX650BjQdZYhnJgm0NDeoJzZ7f3Acszxo7fy313ZhgyqqG2P0slash0NKcLXAdYTnpe60rAbOLmAFdjy06Y0add0Q0rcuJKIjb6u1ehHixDxEnRn6Z2Ia9Y0add0x2HgAXSV5MXFJ3Ohr4p50add0jBMPeyUgCLrrO5Fq4gvria8W1XV0lNK5aYN0slash0hLRFfEvO30slash0mCo9Tn08pyynIYYyRU0slash0lRCfE89AQopGiAltsMtMti7lXD94S1zz1i5n2gaF72UdKBwFqoSuAXpBnA0add04B0add0hBpOHGC9iTjtszdxMUxJmsTemnBnfFTGDYrsyos0slash096vyqm3d7bFonsD0zpa6fLSg6o05Y8dCg7KBQKxcvV7miXGFJsUh9y0slash0HifPM21xUZAEvEZ0slash0Ioaz0add00Rf6iwXMOZ4XA040add0Vkn6ZOdYUD2C1ma2nKS6kvR26dBUimBmIX5q0wOfj1WOUehLoF0slash043DMKeEezkW4BXFAaBdwQh3JIBk3g4fpKuUhLADDJHPVvrAMLj5fiHwBWghVUk70slash0RqnYdYDxOjfBlV6cYPXjLjuka0add0hESfcn0add0evHYFWIRizssf06NwUPkl9xOiVg0add03WrOFqUJbB1F9cZxY72Icn7rGcIOmH5creMfJI9KsSGzMKmpKNRIiDYIsDTajNooMS9rUfWHDVL5Me0slash0iVaywJd71sR7Hbo0slash091rubEMn0add000slash06Pr2R3tL1N60JlSk6Cq77XHd2llkm0VlTZvVyXoh1P0add05M4jwrqniDsq1AuG0add0k8deM2cZQrnLLM3ivuQpLz40add0hjwtrT7VLkGqF0slash093nQI4pFVCIQwfSL4K0slash0j0slash0UojQrxRXWOIuNODDHDW4joo9ktw0slash0I1HRk6o0slash0Vpp8yAl0slash0NtAAFVV3fykhPgO2UEndRrHqDDKp10slash0xSwyK2UKCKtyCdojha0iVZtnZoreJDamOqNik8f0add0VA8aEpUwL9FnoRdQ1L4bxIA5Deh11gR0slash0dJHQ9gAxzRhRl2orsyC3SUq9UuycG5KdDodzLvrlinhgJ8YQbp2Q0slash0GaMg0slash04au2iZ6Sjb2EPj0add0eLn6eJMLwy8kRNlvy9TmKrdIFGIytXol8muUuYPaT9ox4uDCPKFvOgmc967EJq8tJygNdkwKbJAvtTgKbSOORXeRLHYtvwGfuIsTQz71zmc0slash0klmXfxp8HUfA29tORcAp9VKYyCCvP4UYqJMwXxrIzAAt0demfD8TqYgdg3alRleDeqTgcAzk1tJ0slash0u0slash05v6IBwUyn5edHHykrhcEAS8i9PBgc3LDrnKJ00slash0qI70slash0JHX5UNkh6cZX4zYAGz8NK20add0RtmJjHBtnA6DmrLkz0Cl3kQoMZEYJkG3uMG5IFwPLnBBPzRtQL8tEdjnwL0slash0tnzKDvuZostO0add0mgnmg0add0v33SAxZUK9DxcFt565UuOLN80H2mqVvnlv8Xz0add0GNfGQxtvdNUWkFfNWWVawEQur2C7XaLl7m5xa0slash0P80qYa0slash0ZNEqKnuTqosFkEHag5QMyxiEqt5g3r8it2XSvagAEquqeRf8WCHjPkGHfAah0kJ5qpeJoJTuLUdTIgI2y4ijDKSNi0add0kh8yOa46JMfoieLtwoBO4metpHvjC4ozmT5Lx0Ml0add0dKUdKq8aztrcHM4C7x0DXPmk5YUwVKzu24jlWGFbhUiX2lirfPKE0slash0SFsuEm0add0vFjyasL1QLKUQqCr7vADHO4ZnUEjlsP0vfDE0vUdv1znYNmm7Rh0slash0bGCkNeKqas0YyR0slash0qqPp0mNHTBEqVA0slash0EYIPNn27WaJNqJl0eh1Dy0RPlZAVYT5n1r7w5a7xe0O1w9nZgu3oAS93ZbjIguDVfxgDx2QH4lu0add0NZcCND0add0YdnsHxbT4G2rq79jrXm772bRF0add016A0itsfAgbZThiDsI6Je7e1QNW80add0Dmx1wHNdqFjrMxmNmaQq1Gw0add0q8gCBklZ9fNb9uK30y2njdTZbZ0JYKV1VIsmWyI4E9v43iMJdvGvDXGreQ3SHDIAWDAr3EKlmaJcdEH4zN5YIW7u7cvcHnf0slash0ne0slash0nCmcyLGLt8PXGMX7gFsgNy1UhNiT0rgfom0uTncDUNHDBm6NjyltK5H4M4uze0slash0vSRS9yGcPdS1LN10add0V72hoJHfePdX1Rm6QuoeBD6DjAvnk0slash0Hmgxg9fH6wVuir9U3iey8OFOIkjeFhdDcISrPyn9Vp6QjHR4CtbWMy2WutSZSy1PxF040slash0slsIVkAMwyR0add0hzfK76Nhl8IsJVFq96HBwZJ2rH8d0add0pOZf4Vgx0slash0Ry7ipcZ9Ce2jnDzzlifiMaNe0dFk30add0bIyeNPXN0slash02SeqcD92qneY4r7fZy0Iefk0slash0O6bFhpX02mVG7tf0slash02V0AZwviMyHfxKYYJrC3SxQp8kSn9NRa0dy0slash05wcaRQivmnr0slash0aOm1K4t8RwBjVSAcOtTB0add07BbxKNPtt4sa8qiVivRWbDKGt7Cj01up0slash0TGaPB6IBheN5zxJ0slash0znVqstPOBgJeglbeDPikTKcy4OpJ2KcRUYbQlIKBKR4jJRsY7qoQRD5zxIVplqzLB6AeSH2RDE1Uv0add0HbUeCbafOaYbibAvsTToe000add0ffRikQkDipd4IleJ2evQf9BE3LrD9slsMT40v3v0slash007MqwDS53vfTmx3FZAxt9HcvElXasvMS64Nj2KlcR0slash0aHMcQ0add0y4DRJhnYp8rKCDJCMy0slash0dt5xagWTeLSjS0add0SRDkmdjZyivxfehXCQA0slash08hKGp8H0add0lgTl1Ae2cZCBzg9rZJUiC9kX7S70add0MNQrmdtXUR7lsy2PGi8t0slash0YenhlISWk7Ap9TXt00RobIcu8TbG0add0zTZJ0add0yoKmElXUoI8VMefnxeVbuTw5vPHYR3zNDwDMzIs5RjAInM1W0add0zsX0slash0ZTGjvGyBR0slash0IY0u0add0FPTF0slash0A6lCX1TU05UmOnGNDIEpCk6xwQyhIPV7cgo56IDrzTdpzOex0add0eXKCzQPiDJ5cX0slash0D0LD5yQzGnSwuLU345Y5zTfY578iyMICCylXVeR3nrsQNAxaYvVX9RoFoidSMDaBTg8Qs8nVJmUDTtbMf0add0KUrMtlPVA0add04CQAeQleMB0IenawQb8Tg3yfmGgYEHiT35MFpshs5UUZ4wqz8Wdxzt171ZaaTJfi8DThwZ0slash0t1NhpYgyRyVgKwafa0add0cP9xnsFp5daRJFBWWzvazYLz68WscoOQ6puGpBWARvrNjZLCQETnmL9IIf1MG7FNgARcmXXqqmcpVRoJAflMjyBJ18qdzTdNQRyG8yqyFTjdGipTIxT4FCPMdSFcFakJY9OG8MU4o7YF2vKUpSUG2bSPmnW8oDQxax850slash0fCZCJaHNCtPUrdzo2093AssGIuOeVVuLjijELBasxh7rGaWEC73AoBf9W0add024bJW0add0DvaItexXfHMM6hTwyQTtZ9gHqeoJK64s0slash0VH4GEy4xqFbiNC1emeYVQrCjrJ5f4i6IWfDN0AX3TuzdsfsrYLb0slash0GfkGGEGWaPG8J17VXA7Qn0WuIm8rZ9kEySIkHylhQNuUXzM54Q60f2mWh2Pv3IuyK4q3ZdtjJmZMYoAdF7pKJOs9oGHy9cIHYREn0add0M00add0s0slash0JdO7VszqahQpchI0slash0QOWAMbI7Yl0XeF3CZiskkLi27B0slash00slash0MQ0slash0BbqyctpRGG0slash0zbvKHA4AxzARyIRRHd1yN1ChVsKDZbKc0t98dljXrAj4JofN0add0AdE4fyAbVlI2Qa2bS0idAO6kUeDjkLmE5ElDIjGYrPNMp1tYQ41lyObv9QBEweV20add0tBN2BL20slash0ovq9vr3ATDZfx2kQLM8NFZ49CxQHyV6SCqPpYT2aog65z0add0jwUyfouvNbzskEVkPhPc0slash0YOjwNbK7Bux8vC72qogdlkmbteuzwzXKuuFclur0add0U6uXWfSVNsc4yjI3W9KWAQm5LX1DgC6tB4eE5HWMWRmCXKgBZt2pMazE0slash0z859wIIta6ujAQLqZDXZ0add0XxSzRzfxiMOVxZNxcnmHvWLBm2jDsuM0add03MXv1RN7VvThgveJUTUwTT0add0uSPfFwsFXSj5wCIt09YBLqSUFq0slash0ACozQ0pgZth2EqffpvDQD0slash0h4KDBZfBpMY50pTTMU051vkLHyW8DX75THHJNf5SZnfayXwmQGOpO0add0wqRzQEumhirOXCCbaWizDlRul33J9YHWz0add0egk8HDrMLbSFnzxsT0eloCV2z65fBwg02CC5T8fpATreViyEj5pLygdZ1cRI7jkVlxYea0Cdo0x1ZHWsQg0slash0BFWGvoZ5SN9DFF7VfNjsZrGlxDOm6k3DBf6H1A3iKtY1k0add0zauSRqcpLHQo9dC2DVaSgQLVNF0add0qVn50add00od973WX9fVPV8QbAdGj9V26pb0slash0HqBWsqKhkJceVLg5DADtvM3txxlr8BRWqtJcaX3vM8fPeojp6V8ZBq0slash0JBCsNrLD0kVdMzFplTN3sw1BRlw8klJQ0add0yCR2F0A1zZ2wPOUrcvpCeFOkwky1lOs4OqwVhqv2PqnqWpvcS5TjnivsyyFleHdLVeM5C0slash0qV0add0zbytHmf0slash02c0cGKVrSr5MZ02A1gUbcTpDiJwAz7nq3mBDcNf0add0ZUc0gFLMcWERgwlEUoFk54hHyVDZCMnHObkCm8ddbmKcrKZ3cO2qdkTsNRtEXnrgu6QcmiQ8vRzDOMtpRLuj0FZk0slash0fbWKXAz0slash0NLU5E8RurveQ8H00IaGKWSBCJP0add07U8ddKEusN4T68lldwBFwcNLe07AF1RUEMmW3U2TH0slash0HXWymM0add06n1IiQcqJiwIrBjoLx9VA48MH6nc0Bwtu9ll2lBtxGPdhs3mj0slash05aq80add0Ry5Q0ljakYSQfbGBUueE8ZaB8YrOpAo0slash03R0add0bxgK2CknbO0slash0vIXl4S34OTx5nO0nPVBLMjI2UGqmxOGvO8FAG7yD0add0HzSjhlzYiKFDTvkClalGBDsEr0JeJk3fpovRL6G6mPHJpEsVPiAuAG98iwVakWXfTl6CKlHacc4DE1VGRUWlHIfGcsHM0add09SR0ZA7Xswj6oUr27xady8N0slash0ovuWFimePx0P94dlm0add0CcE0QXC1OOPbbU5mE7Kz9NChFUt3ppcW0wKSgmq65Mgy73sxzhZ7fv0add0bKysqxtdWIWZKOa2LpGoELcX8wNZOcfSAZDEMKu0oaXzP8sSW7h0CHG178Gd8Ba8P0add0xin2pLnEAwWzeUJoQmv0slash04UKw3joJMYzgVY80add0fy5Q6Rf0slash0O0add0qRVSCBcAvGchmJiymf4VlZoorPoHIbPpkK8RmxqxcOGme8UJyVtamZOg8yUgfxV94JrDWXCEnr0slash0WF0SKM0add0r9JySQ4gZpP4R7LxT8DT5a93dJhiEuRDSCbH0add0osWYeHCZvvEHCE5R8xuV9d6yqAT9cW529cK8j1KYpm5XmvBfcNa0add0vNjFax82J0slash0Qxvd0slash0ROiXgfrl9UX0slash00slash0DVYfgLtgoTd6YbgEMlBIs5fNHgnrOU2CmnP00neFvGWzgxetYlhi9T0X4olrB0bQKudDPyF3Mx020slash0IapfNc29Gcxq0slash0KNipc0add0v6OV3Nal6KxI0add0A605kS5kjolX201yeSk9B8gSIEVyvR8lsYcoYamZmw66fm4l0slash0Ev5TY2MbArrZPu4VssE4sUhiskAVrtP0slash0hy1Hr3YYnsO2R4YDbZFzFxGBhm0QOLCUcD4BcWS1V1b0add0QsaCTAP9WZC0add0KH3UpiWjKQsZio1bnh1Kqd4Y9ebDo0slash0Od2Qg7F5xMm79FPkjqbUEd9SRUpJ4wNQj100equals0",
        'type': "Title",
        'word': "{keyword}",
    }
    debug: bool = False
    json_mode = True


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        total = response.css("::text").re(".*共(.*)记录")
        total = total[0] if total else 9
        return int(total)//10 + 1


    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("ul li")

    def edit_items(self, items_box: Any) -> Iterable[Any]:
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return items_box

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("h2::text").getall(),
            'url': "www.pds.gov.cn" + item.css("a::attr(href)").get().split("\\")[1].split("\"")[1],
            'source': item.css("p i").re(".*信息来源：\[(.*)\]")[0],
            'date': item.css("p i").re(".*日期：(.*)</i>")[0],
        }
        return result

