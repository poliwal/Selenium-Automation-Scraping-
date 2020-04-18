from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
# from selenium.webdriver
browser = webdriver.Chrome()

url = 'https://google.com'
browser.get(url)

search = browser.find_element_by_name('q')
search.send_keys("moh ka arth")

submit_btn = browser.find_element_by_css_selector("input[type='submit']")
time.sleep(2)
submit_btn.click()


time.sleep(1.5)
more_btn = browser.find_element_by_xpath("//div[contains(text(), 'More definitions and word origin')]")
more_btn.click()

html_raw = browser.find_element_by_xpath('//ol[contains(@class, "eQJLDd")]')
# for i in range(len(html_raw)):
#     # print(html_raw[i].get_attribute("innerHTML"))
#     ss = html_raw[i].find_element_by_xpath('//div[contains(@data-dobid, "dfn")]')
#     print(ss)
# for html_ra in html_raw:
#     html = html_ra.get_attribute("innerHTML")
#     print('**************************************************')
# print(html_raw.get_attribute("innerHTML"))

souppp = soup(html_raw.get_attribute("innerHTML"), 'html.parser')
data_raw = souppp.find_all('span')
for i in range(1,len(data_raw),2):
    print(data_raw[i].text)
# print((list(data_raw)))
# for i in range(1,len(data),2):
#     data.append(data_raw[i])

# print(data)
"""
<div jsname="x3Eknd" class="VpH2eb vmod XpoqFe" data-topic="" data-hveid="CAQQAg"><div class="gycwpf hide-focus-ring D5gqpe" jscontroller="HLiDHf" data-animation-enabled="true" data-audio-play-tts="true" data-language-code="hi" data-tts-string="मोह" aria-label="Listen" role="button" tabindex="0" jsaction="rcuQ6b:npT2md;DiIjNc;xLXIyb:DGzHQ" data-ved="2ahUKEwib1bam7PHoAhUhmuYKHfsqDcYQlfQBMAB6BAgEEAM">  <div class="brWULd"> <audio jsname="QInZvb" preload="auto">  <source src="https://www.google.com/speech-api/v1/synthesize?text=%E0%A4%AE%E0%A5%8B%E0%A4%B9&amp;enc=mpeg&amp;lang=hi&amp;speed=0.4&amp;client=lr-language-tts&amp;use_google_only_voices=1" type="audio/mpeg"></audio> <div jsname="qpYryf" class="vfmVQ"></div> <div jsname="FJYLhd" class="KnZOyc"></div> <div class="pkt1Wd fjnQw"></div> <div jsname="m1xdOb" class="pkt1Wd nIW5Sd"></div> <div jsname="DFrD7b" class="pkt1Wd byDyWd"></div> </div> </div><div class="WI9k4c"><div class="GgmXif jY7QFf" style="margin-bottom:0;line-height:1.3"><div class="DgZBFd"><span data-dobid="hdw">मोह</span></div></div></div><div jsname="p0q1Sd" class="vmod ABgcGb"></div><div class="vmod"><div class="vk_gy"><span>Transliterated version: <span style="font-weight:bold">moh</span>.</span></div><div jsname="r5Nvmf" class="vmod" data-topic=""><div><div class="lW8rQd"><div class="vpx4Fd"><div class="pgRvse vdBwhd"><i><span>पुल्लिंग</span></i></div></div></div><ol class="eQJLDd"><li jsname="gskXhf"><div class="vmod"><div class="thODed Uekwlc XpoqFe"><div jsname="cJAsRb" data-topic=""><div style="float:left"><span>1</span>. </div><div style="margin-left:20px"><div class="QIclbb XpoqFe"><div style="display:inline" data-dobid="dfn"><span>अज्ञान, नासमझी।</span></div></div></div></div><div style="margin-left:20px"></div></div></div></li><li jsname="gskXhf"><div class="vmod"><div class="thODed Uekwlc XpoqFe"><div jsname="cJAsRb" data-topic=""><div style="float:left"><span>2</span>. </div><div style="margin-left:20px"><div class="QIclbb XpoqFe"><div style="display:inline" data-dobid="dfn"><span>मूर्खता, बेवकूफ़ी।</span></div></div></div></div><div style="margin-left:20px"></div></div></div></li><li jsname="gskXhf"><div class="xpdxpnd" data-mh="28" id="_EuGaXpuEA6G0mgf71bSwDA5" data-mhc="1" style="max-height: 28px;"><div class="thODed Uekwlc XpoqFe"><div jsname="cJAsRb" data-topic=""><div style="float:left"><span>3</span>. </div><div style="margin-left:20px"><div class="QIclbb XpoqFe"><div style="display:inline" data-dobid="dfn"><span>अविद्या।</span></div></div></div></div><div style="margin-left:20px"></div></div></div></li><li jsname="gskXhf"><div class="xpdxpnd" data-mh="28" id="_EuGaXpuEA6G0mgf71bSwDA7" data-mhc="1" style="max-height: 28px;"><div class="thODed Uekwlc XpoqFe"><div jsname="cJAsRb" data-topic=""><div style="float:left"><span>4</span>. </div><div style="margin-left:20px"><div class="QIclbb XpoqFe"><div style="display:inline" data-dobid="dfn"><span>ममता (जैसे—मोह माया, धन दौलत का मोह)।</span></div></div></div></div><div style="margin-left:20px"></div></div></div></li><li jsname="gskXhf"><div class="xpdxpnd" data-mh="28" id="_EuGaXpuEA6G0mgf71bSwDA9" data-mhc="1" style="max-height: 28px;"><div class="thODed Uekwlc XpoqFe"><div jsname="cJAsRb" data-topic=""><div style="float:left"><span>5</span>. </div><div style="margin-left:20px"><div class="QIclbb XpoqFe"><div style="display:inline" data-dobid="dfn"><span>भ्रांति (जैसे—सांसारिक मोह)।</span></div></div></div></div><div style="margin-left:20px"></div></div></div></li></ol></div></div></div><div jsname="Hqfs0d"><div class="xpdxpnd" data-mh="66" data-mhc="1" style="max-height: 66px;"><div id="_EuGaXpuEA6G0mgf71bSwDA11"><div class="vk_sh vk_gy" style="margin:20px 0 0">Origin</div><div style="margin-top:10px"><span>संस्कृत</span></div></div></div></div></div>
"""