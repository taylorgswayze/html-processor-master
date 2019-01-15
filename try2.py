from flask import Flask, render_template, request
from bs4 import BeautifulSoup
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

        for i in range(1, (numlinks + 1)):
            linknames.append(request.form['linkname' + str(i)])
            urls.append(request.form['linkurl' + str(i)])

        if brand == 'cat':
            brandcolor = 'ffcb08'
            brandtextcolor = '000001'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3336688CATFOOTWEAR/B21328916.223455667;dc_trk_aid=421618445;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
        elif brand == 'hp':
            brandtextcolor = '707072'
            brandcolor = 'ffffff'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3336694HUSHPUPPIES/B21328916.223583574;dc_trk_aid=421618454;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
        elif brand == 'sperry':
            brandcolor = 'e04503'
            brandtextcolor = 'ffffff'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3356031SPERRYFOOTWEAR/B21328916.223354352;dc_trk_aid=421618748;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua='
        elif brand == 'merrell':
            brandtextcolor = 'ffffff'
            brandcolor = 'da4726'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3349655MERRELL/B21328916.223459126;dc_trk_aid=421618463;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'
        else:
            brandcolor = 'ffffff'
            dcparam = 'https://ad.doubleclick.net/ddm/trackclk/N800582.3336688CATFOOTWEAR/B21328916.223455667;dc_trk_aid=421618445;dc_trk_cid=102927023;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=?'

        # WRAP TAGGED IMAGES IN LINKS
        counter = 1
        for i in soup.find_all('img'):

            linkareas = soup.find_all(id="link" + str(counter))
            for img in linkareas:
                hrefd = '$clickthrough(' + linknames[counter - 1] + ',myURL=' + dcparam + urls[counter - 1] + '?tmemail=)$'
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

        soup = soup.prettify()
        return soup

    return render_template('my_form.html')

if __name__ == '__main__':
    app.run(debug=True)