from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.adapters import HTTPAdapter

from urllib3.util.ssl_ import create_urllib3_context
from urllib3.util.ssl_ import DEFAULT_CIPHERS

import os

from urllib.parse import urlparse

url = "http://api.todopago.com.ar"

CIPHERS = DEFAULT_CIPHERS + "HIGH:!DH:!aNULL"

class AFIPAdapter(HTTPAdapter):
    """@author: WhyNotHugo
    An adapter with reduced security so it'll work with AFIP.
    """

    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs["ssl_context"] = context
        return super().init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs["ssl_context"] = context
        return super().proxy_manager_for(*args, **kwargs)

wsdl = f'{os.getcwd()}/wsdl/Authorize.wsdl'



commerce = {
	'Merchant': "27144",
	"Security": "0702a46463bf40d69fac2916794d8c92",
	"EncodingMethod": "XML",
	"URL_OK": "http,//someurl.com/ok/",
	"URL_ERROR": "http,//someurl.com/fail/",
	# "EMAILCLIENTE": "email_cliente@dominio.com"
}

operation = {
"MERCHANT": "27144",
"OPERATIONID": "06",
"CURRENCYCODE": "032",
"AMOUNT": "54",
"CSBTCITY": "Villa General Belgrano",
"CSSTCITY": "Villa General Belgrano",
"CSMDD6" : "",
"CSBTCOUNTRY": "AR",
"CSSTCOUNTRY": "AR",

"CSBTEMAIL": "todopago@hotmail.com",
"CSSTEMAIL": "todopago@hotmail.com",

"CSBTFIRSTNAME": "Juan",
"CSSTFIRSTNAME": "Juan",

"CSBTLASTNAME": "Perez",
"CSSTLASTNAME": "Perez",

"CSBTPHONENUMBER": "541160913988",
"CSSTPHONENUMBER": "541160913988",

"CSBTPOSTALCODE": "1010",
"CSSTPOSTALCODE": "1010",

"CSBTSTATE": "B",
"CSSTSTATE": "B",

"CSBTSTREET1": "Cerrito 740",
"CSSTSTREET1": "Cerrito 740",


"CSBTSTREET2": "Cerrito 740",
"CSSTSTREET2": "Cerrito 740",

"CSBTCUSTOMERID": "453458",
"CSBTIPADDRESS": "192.0.0.4",
"CSPTCURRENCY": "ARS",
"CSPTGRANDTOTALAMOUNT": "125.38",
"CSMDD7": "",
"CSMDD8": "Y",
"CSMDD9": "",
"CSMDD10": "",
"CSMDD11": "",
"STCITY": "rosario",
"STCOUNTRY": "",
"STEMAIL": "jose@gmail.com",
"STFIRSTNAME": "Jose",
"STLASTNAME": "Perez",
"STPHONENUMBER": "541155893737",
"STPOSTALCODE": "1414",
"STSTATE": "D",
"STSTREET1": "San Martin 123",
"CSMDD12": "",
"CSMDD13": "",
"CSMDD14": "",
"CSMDD15": "",
"CSMDD16": "",
"CSITPRODUCTCODE": "electronic_good#electronic_good",
"CSITPRODUCTDESCRIPTION": "NOTEBOOK L845 #SP4304LA DF TOSHIBA",
"CSITPRODUCTNAME": "NOTEBOOK# L845 SP4304LA DF TOSHIBA",
"CSITPRODUCTSKU": "LEVJNS#L36GN",
"CSITTOTALAMOUNT": "1254.40#980.80",
"CSITQUANTITY": "1#2",
"CSITUNITPRICE": "1254.40#980.80"
}

with Session() as session:
        # For each WSDL, extract the domain, and add it as an exception:   
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    session.mount(base_url, AFIPAdapter())

    transport = Transport(session=session, timeout=5)
    client = Client(wsdl=wsdl)

    response = client.service.SendAuthorizeRequest(**commerce)
    print(response)
