from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from fragments import *
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        linknames =[]
        urls = []
        html = request.form['html']
        brand = request.form['brand']
        numlinks = int(request.form['numlinks'])
        soup = BeautifulSoup(html, 'html.parser')
        primarycolor = request.form['primarycolor']

        for i in range(1, (numlinks + 1)):
            linknames.append(request.form['linkname' + str(i)])
            urls.append(request.form['linkurl' + str(i)])

        if brand == 'cat':
            brandcolor = 'ffcb08'
            brandtextcolor = '000001'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3336688CATFOOTWEAR/B21328916.223455667;dc_trk_aid=421618445;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
            header = catheader
            footer = catfooter
        elif brand == 'bates':
            brandcolor = '4C6D8B'
            brandtextcolor = 'ffffff'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3356949BATES/B21328916.223351460;dc_trk_aid=421680288;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
        elif brand == 'chaco':
            brandcolor = 'e9d171'
            brandtextcolor = 'ffffff'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3336691CHACO/B21328916.223354301;dc_trk_aid=421618448;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
        elif brand == 'keds':
            brandcolor = 'ffffff'
            brandtextcolor = '000001'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3337588KEDS/B21328916.223584159;dc_trk_aid=421618466;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
        elif brand == 'hdf':
            brandcolor = 'E15700'
            brandtextcolor = 'ffffff'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3349652HARLEY/B21328916.223354859;dc_trk_aid=421618460;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
        elif brand == 'hp':
            brandtextcolor = 'ffffff'
            brandcolor = '707072'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3336694HUSHPUPPIES/B21328916.223583574;dc_trk_aid=421618454;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
            header = hpheader
            footer = hpfooter
        elif brand == 'sperry':
            brandcolor = 'e04503'
            brandtextcolor = 'ffffff'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3356031SPERRYFOOTWEAR/B21328916.223354352;dc_trk_aid=421618748;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
        elif brand == 'merrell':
            brandtextcolor = 'ffffff'
            brandcolor = 'da4726'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3349655MERRELL/B21328916.223459126;dc_trk_aid=421618463;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
            header = merrellheader
            footer = merrellfooter
        elif brand == 'merrelloutlet':
            brandtextcolor = 'ffffff'
            brandcolor = 'da4726'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3349655MERRELL/B21328916.223459126;dc_trk_aid=421618463;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
            header = merrelloutletheader
            footer = merrelloutletfooter
        elif brand == 'saucony':
            brandtextcolor = 'ffffff'
            brandcolor = '000001'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.159760SAUCONY/B21328916.223458955;dc_trk_aid=421618472;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
        elif brand == 'wolverine':
            brandcolor = 'A41E21'
            brandtextcolor = 'ffffff'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3345731WOLVERINE/B21328916.223354358;dc_trk_aid=421618751;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
        else:
            brandcolor = 'ffffff'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3336688CATFOOTWEAR/B21328916.223455667;dc_trk_aid=421618445;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'

        if primarycolor:
            brandcolor = primarycolor
        else:
            pass

        # WRAP TAGGED IMAGES IN LINKS
        counter = 1
        for i in soup.find_all('img'):

            linkareas = soup.find_all(id="link" + str(counter))
            for img in linkareas:
                chars = set('?')
                if any((c in chars) for c in urls[counter - 1]):
                    dcparamchar = '&'
                else:
                    dcparamchar = '?'
                hrefd = '$clickthrough(' + linknames[counter - 1] + ',myURL=' + dcparam + urls[counter - 1] + dcparamchar + 'tmemail=)$'
                img.wrap(soup.new_tag('a', href=hrefd))
            counter += 1

        # FORMAT A TAGS
        for i in soup.find_all('a'):
            i['style'] = 'text-decoration:none;color:#' + brandtextcolor + ';'
            i['target'] = '_blank'

        # displayblock images
        for i in soup.find_all('img'):
            i['style'] = 'display:block;'

        # WRAP ROWS IN TABLES
        for i in soup.find_all('tr'):
            i.wrap(soup.new_tag('table'))

        # TABLE FORMATTING
        for i in soup.find_all('table'):
            i['border'] = '0'
            i['cellpadding'] = '0'
            i['cellborder'] = '0'
            i['align'] = 'center'
            i['valign'] = 'top'
            i['style'] = 'border-collapse:collapse;font-family:arial,helvetica,sans-serif;font-weight:bold;color:#000001;'
            i['cellpadding'] = '0'

        # CELL FORMATTING
        for i in soup.find_all('td'):
            i['height'] = i.img['height']
            i['width'] = i.img['width']
            i['border'] = '0'
            i['cellpadding'] = '0'
            i['cellborder'] = '0'
            i['align'] = 'center'
            i['valign'] = 'top'
            i['bgcolor'] = 'ffffff'
            i['style'] = 'border-collapse:collapse;font-size:16px;'
            i['cellpadding'] = '0'


        # CTA FORMATTING
        for i in soup.find_all(id="CTA"):
            i['bgcolor'] = brandcolor
            i['valign'] = 'middle'
            i.img.replace_with('SHOP NOW')
            i['style'] = 'font-size:16px;color:#' + brandtextcolor

        # Text area formatting
        for i in soup.find_all(id="text"):
            i['bgcolor'] = 'ffffff'
            i['valign'] = 'top'
            i.img.replace_with('ProductName')
            i['style'] = 'font-size:18px;color:#' + brandtextcolor

        if header:
            soup.table.insert_before(header)
            soup.find_all('table')[-1].insert_after(footer)




        print(soup.prettify(formatter=None))
        return soup.prettify(formatter=None)

    return render_template('my_form.html')

if __name__ == '__main__':
    app.run(debug=True)
