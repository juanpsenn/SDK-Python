from zeep import Client, Settings

from typing import Union

import os

def object_to_xml(data: Union[dict, bool], root="object"):
    xml = f"<{root}>"
    if isinstance(data, dict):
        for key, value in data.items():
            xml += object_to_xml(value, key)

    elif isinstance(data, (list, tuple, set)):
        for item in data:
            xml += object_to_xml(item, "item")

    else:
        xml += str(data)

    xml += f"</{root}>"
    return xml


url = "https://apis.todopago.com.ar/services/t/1.1/Authorize"

wsdl = f"{os.getcwd()}/wsdl/Authorize.wsdl"

operation = {
    "MERCHANT": "2083247",
    "OPERATIONID": "01",
    "CURRENCYCODE": "032",
    "AMOUNT": "1",
    "CSBTCITY": "Villa General Belgrano",
    "CSSTCITY": "Villa General Belgrano",
    "CSMDD6": "",
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
    # "CSBTSTREET2": "Cerrito 740",
    # "CSSTSTREET2": "Cerrito 740",
    "CSBTCUSTOMERID": "JuanPerez",
    "CSBTIPADDRESS": "192.0.0.4",
    "CSPTCURRENCY": "ARS",
    "CSPTGRANDTOTALAMOUNT": "99.00",
    # "CSMDD7": "",
    # "CSMDD8": "Y",
    # "CSMDD9": "",
    # "CSMDD10": "",
    # "CSMDD11": "",
    # "STCITY": "rosario",
    # "STCOUNTRY": "",
    # "STEMAIL": "jose@gmail.com",
    # "STFIRSTNAME": "Jose",
    # "STLASTNAME": "Perez",
    # "STPHONENUMBER": "541155893737",
    # "STPOSTALCODE": "1414",
    # "STSTATE": "D",
    # "STSTREET1": "San Martin 123",
    # "CSMDD12": "",
    # "CSMDD13": "",
    # "CSMDD14": "",
    # "CSMDD15": "",
    # "CSMDD16": "",
    "CSITPRODUCTCODE": "electronic_good#electronic_good",
    "CSITPRODUCTDESCRIPTION": "NOTEBOOK L845 #SP4304LA DF TOSHIBA",
    "CSITPRODUCTNAME": "NOTEBOOK# L845 SP4304LA DF TOSHIBA",
    "CSITPRODUCTSKU": "LEVJNS#L36GN",
    "CSITTOTALAMOUNT": "1254.40#10.00",
    "CSITQUANTITY": "1#1",
    "CSITUNITPRICE": "1254.40#15.00",
}

commerce = {
    "Merchant": "",
    "Security": "",
    "EncodingMethod": "XML",
    "URL_OK": "http,//someurl.com/ok/",
    "URL_ERROR": "http,//someurl.com/fail/",
    "Payload": object_to_xml(operation, root="Request"),
}

http_header = {"Authorization": f"TODOPAGO "}
settings = Settings(
    extra_http_headers=http_header,
)

client = Client(wsdl=wsdl, settings=settings)
client.service._binding_options["address"] = url
response = client.service.SendAuthorizeRequest(**commerce)
print(response)
